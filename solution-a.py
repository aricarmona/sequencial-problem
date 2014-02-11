#!/usr/bin/env python
# -*- coding: latin1 -*-

import cli


# F(x) = 2x²
def calculate(number):
    return 2 * (number ** 2)


print calculate(cli.get_number())
