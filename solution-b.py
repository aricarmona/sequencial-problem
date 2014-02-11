#!/usr/bin/env python
# -*- coding: latin1 -*-

import cli


# F(1) = 2;
# F(i) = F(i-1) + i*4 - 2
def calculate(number):
    if number == 1:
        return 2
    else:
        return calculate(number - 1) + number * 4 - 2


print calculate(cli.get_number())
