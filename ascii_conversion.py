#!/usr/bin/env python
# coding=utf-8
"""Provides method for converting text to its ASCII representation."""

def convert(mode, text):
    """Converts text to its ASCII representation."""
    r = ''
    if mode == 0:
        for c in text:
            r += '0' + bin(ord(c))[2:]
    elif mode == 1:
        for c in text:
            r += str(ord(c))
    elif mode == 2:
        for c in text:
            r += hex(ord(c))[2:]
    else:
        for c in text:
            r += oct(ord(c))[2:]
    return r
