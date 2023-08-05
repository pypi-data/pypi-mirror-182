#!/usr/bin/env python3
from typing import List, Union, Callable, Set, Dict, Tuple, Optional


def extract_bio(text: str) -> List[str]:
    """ Get NER BIO sequence from text
    """
    text = text.strip()
    if not text:
        return []
    bio = []
    amid = False
    for c in text:
        if c == '[':
            amid = True
        elif c == ']':
            amid = False
        else:
            if amid:
                bio.append('B' if bio and bio[-1] == 'O' else 'I')
            else:
                bio.append('O')
    return bio


def extract_bioe(text: str) -> List[str]:
    """ Get NER BIOE sequence from text
    """
    text = text.strip()
    bioe, stack = [], []
    i = 0
    while i < len(text):
        c = text[i]
        if c == '[':
            i += 1
            while i < len(text) and text[i] != ']':
                stack.append(c)
                i += 1
            if len(stack) == 1:
                bioe.append('B')
            elif len(stack) == 2:
                bioe.extend(['B', 'E'])
            else:
                bioe.extend(['B'] + ['I'] * (len(stack) - 2) + ['E'])
        else:
            bioe.append('O')
        i += 1

    return bioe
