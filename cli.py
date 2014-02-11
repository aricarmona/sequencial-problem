#!/usr/bin/env python
# -*- coding: latin1 -*-
#
# Function to get number from command line.

import sys
import getopt


def get_number():
    args = sys.argv[1:]

    try:
        opts, args = getopt.getopt(args, 'hn:', ['number='])
    except getopt.GetoptError:
        print 'Problemas com o comando.\nExemplo de uso: ciro.py -n number'
        sys.exit(2)

    opt, number = opts[0]
    return int(number)
