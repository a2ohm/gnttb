#! /usr/bin/python3
# -*- coding:utf-8 -*-

from .sblgnt import morphgnt_rows
from .verse  import Verse

def get(bcv):
    """Return a verse given its bcv.
    """

    verse = Verse()
    find_verse = False
    
    for row in morphgnt_rows(int(bcv[0:2])):
        if row['bcv'] == bcv:
            verse += row
            find_verse = True

        elif find_verse:
            break

    return verse
