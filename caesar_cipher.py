#!/usr/bin/env python
# coding=utf-8
"""Provides methods for ciphering and deciphering using Caesar's cipher."""

def shift(key, text, decrypt = 0):
    """Returns 'text' with characters rotated 'key' places in the alphabet."""
    if decrypt:
        key = -key
    r = ''
    for c in text:
        r += shift_char(key, c)
    return r

def shift_char(key, char):
    """Shifts 'char' by 'key' places."""
    if char.isupper():
        s = ord('A')
    elif char.islower():
        s = ord('a')
    else:
        return char
    return chr((ord(char) + key - s) % 26 + s)
