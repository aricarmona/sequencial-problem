#!/usr/bin/env python
# -*- coding: latin1 -*-

import cli


# F(1) = 2;
# F(2) = 8;
# F(N) = 2 x F(N-1) - F(N-2) + 4
def calculate(number):
    if number == 1:
        return 2
    elif number == 2:
        return 8
    else:
        return 2 * calculate(number - 1) - calculate(number - 2) + 4


print calculate(cli.get_number())
