#! /usr/bin/python3
# -*- coding:utf-8 -*-

from .sblgnt import morphgnt_rows
from .verse  import Verse
from .bcv import checkBcv, expandBcv, splitBcv

def get(bcv):
    """Return a group of verses given their bcv.

    bcv syntax:
        bbccvv          --> one verse
        bbccvv-bbccvv   --> group of verses
    """

    if checkBcv(bcv):
        bcv_start, bcv_end = splitBcv(bcv)
    else:
        return None

    verse = Verse(expandBcv(bcv))
    find_verse = False

    for row in morphgnt_rows(bcv[0:2]):
        if bcv_start <= row['bcv'] <= bcv_end:
            verse += row
            find_verse = True

        elif find_verse:
            break

    return verse
