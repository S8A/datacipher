#!/usr/bin/env python
# coding=utf-8
"""Provides method for using Vigenère's cipher."""

import caesar_cipher

def cipher(key, text, decipher = 0):
    """Ciphers or deciphers 'text' using 'key'."""
    r = ''
    ki = 0
    for c in text:
        if c.isalpha():
            nki = (ord(key[ki].lower()) - 97) % 26
            if decipher:
                r += caesar_cipher.shift(nki, c, decipher=1)
            else:
                r += caesar_cipher.shift(nki, c)
            ki = (ki + 1) % len(key)
        else:
            r += c
    return r
