#!/usr/bin/env python3
# coding=utf-8
"""Command line version of the DataCipher text ciphering tool."""

import ascii_conversion as ascii
import atbash_cipher as atbsh
import caesar_cipher as caesr
import col_transposition as coltr
import re
import sys
import vigenere_cipher as vignr

__author__ = "Samuel Ochoa"
__mantainer__ = "Samuel Ochoa"
__email__ = "samuelochoap@gmail.com"

helps = [''] * 6
helps[0] = '.: ASCII conversion :.\n>> ascii <mode> <text>\n'
helps[0] += '<mode>:\n0\tbinary\n1\tdecimal\n2\thexadecimal\n3\toctal\n'
helps[1] = '.: Atbash cipher :.\n>> atbsh <text>\n'
helps[2] = '.: Caesar cipher :.\n>> caesr <mode> <key> <text>\n'
helps[2] += '<mode>:\n0\tciphering\n1\tdeciphering\n2\tbrute force\n'
helps[2] += '<key> is a number (1-26). If <mode> is 2, DO NOT write one.\n'
helps[3] = '.: Columnar transposition cipher :.\n>> coltr <mode> <key> '
helps[3] += '<text>\n<mode>:\n0\tciphering\n1\tdeciphering.\n'
helps[3] += '<key> is a number (1-99).\n'
helps[4] = '.: Vigenere cipher :.\n>> vignr <mode> <key> <text>\n'
helps[4] += '<mode>:\n0\tciphering\n1\tdeciphering.'
helps[4] += '<key> is a string without spaces.\n'
helps[5] = '.: Other commands :.\n'
helps[5] += '>> help\tInformation about this program.\n'
helps[5] += '>> help <command>\tInformation about <command>.\n>> exit\n'


def cli(in_cmd):
    if re.match('^(exit)', in_cmd):
        exit()
    elif re.match('^(ascii)', in_cmd):
        cmd = in_cmd.split(' ')
        cmd[2:] = [' '.join(cmd[2:])]
        print(ascii.convert(int(cmd[1]), cmd[2]))
    elif re.match('^(atbsh)', in_cmd):
        cmd = in_cmd.split(' ')
        cmd[1:] = [' '.join(cmd[1:])]
        print(atbsh.cipher(cmd[1]))
    elif re.match('^(caesr)', in_cmd):
        cmd = in_cmd.split(' ')
        r = ''
        if len(cmd) != 3 and cmd[1] != '2':
            cmd[3:] = [' '.join(cmd[3:])]
            r += caesr.shift(int(cmd[2]), cmd[3], int(cmd[1]))
        else:
            cmd[2:] = [' '.join(cmd[2:])]
            for k in range(1, 27):
                r += str(k) + ': ' + caesr.shift(k, cmd[2], 1) + '.\n'
        print(r)
    elif re.match('^(coltr)', in_cmd):
        cmd = in_cmd.split(' ')
        cmd[3:] = [' '.join(cmd[3:])]
        r = ''
        if cmd[1] == '1':
            r += coltr.reverse(int(cmd[2]), cmd[3])
        else:
            r += coltr.cipher(int(cmd[2]), cmd[3])
        print(r)
    elif re.match('^(vignr)', in_cmd):
        cmd = in_cmd.split(' ')
        cmd[3:] = [' '.join(cmd[3:])]
        print(vignr.cipher(cmd[2], cmd[3], int(cmd[1])))
    elif re.match('^(help)', in_cmd):
        print('..:: HELP ::..\n')
        cmd = in_cmd.split(' ')
        if len(cmd) == 1:
            for h in helps:
                print(h)
        else:
            if cmd[1] == 'ascii':
                print(helps[0])
            elif cmd[1] == 'atbsh':
                print(helps[1])
            elif cmd[1] == 'caesr':
                print(helps[2])
            elif cmd[1] == 'coltr':
                print(helps[3])
            elif cmd[1] == 'vignr':
                print(helps[4])
            else:
                print(cmd[1], 'is not a command. Try "help".\n')
    else:
        print('Wrong command. Write "help" without quotes.\n')


if __name__ == '__main__':
    if len(sys.argv) > 2:
        what_to_do = ' '.join(sys.argv[1:])
        cli(what_to_do)
    else:
        while True:
            what_to_do = input('>> ')
            cli(what_to_do)

