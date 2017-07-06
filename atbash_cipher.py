#!/usr/bin/env python
# coding=utf-8
"""Provides method for using the Atbash cipher."""

def cipher(text):
    """Returns a copy of 'text' where A-Za-z is transformed to Z-Az-a."""
    r = ''
    for c in text:
        if c.isalpha():
            if c.isupper():
                up = 32
            elif c.islower():
                up = 0
            r += chr(ord('z') - (ord(c.lower()) - ord('a')) - up)
        else:
            r += c
    return r
