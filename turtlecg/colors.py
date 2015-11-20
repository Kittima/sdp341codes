# -*- coding: utf-8 -*-
import random

'''
Generate a rondom color in Hex
'''


def randomcolor():
    r = lambda: random.randint(0, 255)
    return('#%02X%02X%02X' % (r(), r(), r()))
