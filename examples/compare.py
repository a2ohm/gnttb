#! /usr/bin/python3
# -*- coding:utf-8 -*-

from gnttb import compare
from gnttb import get

averse1, averse2 = compare.compare(get.get('011701'), get.get('020902'))

# By construction, averse1 and averse2 have the same length
for w1, w2 in zip(averse1, averse2):
    w1 = "x" if w1 is None else w1['text']
    w2 = "x" if w2 is None else w2['text']

    print("{:>14} − {}".format(w1, w2))
