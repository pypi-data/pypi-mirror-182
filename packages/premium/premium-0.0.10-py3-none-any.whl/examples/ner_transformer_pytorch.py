#!/usr/bin/env python
import os

import codefast as cf
import numpy as np
import pandas as pd
import torch
from codefast.decorators import cachedclassproperty, cachedproperty, classproperty
from torch.optim import SGD, Adam
from torch.utils.data import DataLoader
from tqdm import tqdm
from transformers import BertForTokenClassification, BertTokenizerFast
import premium as pm
from premium.data.loader import load_yaml, loader
from premium.data.utils import make_obj

# refer: https://towardsdatascience.com/named-entity-recognition-with-bert-in-pytorch-a454405e0b6a
os.environ["TOKENIZERS_PARALLELISM"] = "false"

Cfg = load_yaml('data/config/ner_bert.yaml')
Cfg.use_cuda = torch.cuda.is_available()
cf.info(f'config is {Cfg}')


class Properties(object):
    @cachedclassproperty
    def df(cls):
        # data backup: https://host.ddot.cc/ner_demo.csv
        path_ = loader('ner_en')
        return pd.read_csv(path_).sample(10000)

    @cachedclassproperty
    def labels(cls):
        labels = [v.split() for v in cls.df.labels.values]
        # Check how many labels are there in the dataset
        unique_labels = set()
        for lb in labels:
            for i in lb:
                unique_labels.add(i)

        # Map each label into its id representation and vice versa
        labels_to_ids = {k: v for v, k in enumerate(sorted(unique_labels))}
        ids_to_labels = {v: k for v, k in enumerate(sorted(unique_labels))}
        return make_obj(
            dict(to_ids=labels_to_ids,
                 to_labels=ids_to_labels,
                 unique=unique_labels,
                 values=labels))

    @cachedclassproperty
    def tokenizer(cls):
        return BertTokenizerFast.from_pretrained(Cfg.model_name)

    @cachedclassproperty
    def dataset(cls):
        df_train, df_val, df_test = np.split(
            cls.df.sample(frac=1, random_state=42),
            [int(.8 * len(cls.df)),
             int(.9 * len(cls.df))])

        return make_obj(dict(train=df_train, val=df_val, test=df_test))

    @cachedclassproperty
    def ds(cls):
        # alias of dataset
        return cls.dataset


class Per(Properties):
    ...


def align_label(texts, labels, label_all_tokens: bool = True):
    tokenized_inputs = Per.tokenizer(texts,
                                     padding='max_length',
                                     max_length=Cfg.max_length,
                                     truncation=True)

    word_ids = tokenized_inputs.word_ids()
    previous_word_idx = None
    label_ids = []

    for word_idx in word_ids:
        if word_idx is None:
            label_ids.append(-100)
        elif word_idx != previous_word_idx:
            try:
                label_ids.append(Per.labels.to_ids[labels[word_idx]])
            except:
                label_ids.append(-100)
        else:
            try:
                label_ids.append(Per.labels.to_ids[labels[word_idx]]
                                 if label_all_tokens else -100)
            except:
                label_ids.append(-100)
        previous_word_idx = word_idx

    return label_ids


class DataSequence(torch.utils.data.Dataset):
    def __init__(self, df):
        self.texts = [
            Per.tokenizer(str(t),
                          padding='max_length',
                          max_length=Cfg.max_length,
                          truncation=True,
                          return_tensors="pt") for t in df.text
        ]
        lb = map(str.split, df.labels)
        self.labels = [align_label(t, b) for t, b in zip(df.text, lb)]

    def __len__(self):
        return len(self.labels)

    def get_batch_data(self, idx):
        return self.texts[idx]

    def get_batch_labels(self, idx):
        return torch.LongTensor(self.labels[idx])

    def __getitem__(self, idx):
        batch_data = self.get_batch_data(idx)
        batch_labels = self.get_batch_labels(idx)

        return batch_data, batch_labels


class BertModel(torch.nn.Module):
    def __init__(self):
        super(BertModel, self).__init__()
        self.bert = BertForTokenClassification.from_pretrained(
            Cfg.model_name, num_labels=len(Per.labels.unique))

    def forward(self, input_id, mask, label):
        return self.bert(input_ids=input_id,
                         attention_mask=mask,
                         labels=label,
                         return_dict=False)


class NerModel(object):
    @classmethod
    def _load_data(cls, df_, batch_size: int = 32):
        _seq = DataSequence(df_)
        return DataLoader(_seq, num_workers=4, batch_size=batch_size)

    @classmethod
    def _update(cls,
                model,
                dataloader,
                optimizer,
                trainable=False,
                calculate_loss=False):
        """
        Args:
            model(BertModel):
            dataloader(DataLoader):
        """
        device = torch.device("cuda" if Cfg.use_cuda else "cpu")
        _acc, _loss = 0, 0

        for data, label in tqdm(dataloader):
            label = label.to(device)
            input_id = data['input_ids'].squeeze(1).to(device)
            mask = data['attention_mask'].squeeze(1).to(device)
            if trainable:
                optimizer.zero_grad()
            loss, logits = model(input_id, mask, label)

            for i in range(logits.shape[0]):
                logits_clean = logits[i][label[i] != -100]
                label_clean = label[i][label[i] != -100]

                predictions = logits_clean.argmax(dim=1)
                _acc += (predictions == label_clean).float().mean()
                if calculate_loss:
                    _loss += loss.item()
            if trainable:
                loss.backward()
                optimizer.step()
        return make_obj(dict(model=model, acc=_acc, loss=_loss))

    @classmethod
    def train(cls,
              model,
              df_train,
              df_val,
              epochs: int = 10,
              batch_size: int = 8):
        optimizer = SGD(model.parameters(), lr=Cfg.learning_rate)

        if Cfg.use_cuda:
            model = model.cuda()

        for epoch_num in range(epochs):
            model.train()
            r_train = cls._update(model,
                                  cls._load_data(df_train, batch_size),
                                  optimizer,
                                  trainable=True,
                                  calculate_loss=True)

            model.eval()
            r_val = cls._update(model,
                                cls._load_data(df_val, batch_size),
                                optimizer,
                                trainable=False,
                                calculate_loss=True)

            cf.info({
                'epoch': epoch_num + 1,
                'loss': '{:.3f}'.format(r_train.loss / len(df_train)),
                'accuracy': "{:.3f}".format(r_train.acc / len(df_train)),
                'val_loss': "{:.3f}".format(r_val.loss / len(df_val)),
                'val_accuracy': "{:.3f}".format(r_val.acc / len(df_val))
            })

    @classmethod
    def evaluate(cls, model, df_test):
        if Cfg.use_cuda:
            model = model.cuda()

        r_eva = cls._update(model, cls._load_data(df_test), optimizer=None)
        val_accuracy = r_eva.acc / len(df_test)
        cf.info({'test_acc': '{:<.3f}'.format(val_accuracy)})


if __name__ == '__main__':
    model = BertModel()
    NerModel.train(model,
                   Per.ds.train,
                   Per.ds.test,
                   epochs=Cfg.epochs,
                   batch_size=Cfg.batch_size)
    torch.save(model.state_dict(), Cfg.model_path)
