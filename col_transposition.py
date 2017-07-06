#!/usr/bin/env python3
# coding=utf-8
"""Provides methods for columnar transposition ciphering."""

import math

def encrypt(key, text):
    """Ciphers 'text' using a columnar transposition cipher."""
    r = [''] * key
    for c in range(key):
        p = c
        while p < len(text):
            r[c] += text[p]
            p += key
    return ''.join(r)

def reverse(key, text):
    """Reverses the columnar transposition process in a given 'text'."""
    nc = math.ceil(len(text) / key)
    nr = key
    sb = (nc * nr) - len(text)
    f = [''] * nc
    c = 0
    r = 0
    for i in text:
        f[c] += i
        c += 1
        if c == nc or (c == nc-1 and r >= nr-sb):
            c = 0
            r += 1
    return ''.join(f)
