#! /usr/bin/python3
# -*- coding:utf-8 -*-

from gnttb import get

verse = get.get('010609')

print(verse)
print("({} words)".format(len(verse)))
