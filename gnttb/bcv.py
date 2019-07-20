#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define functions relative to bcv.
"""

def checkBcv(bcv):
    """Check that a bcv is valid.

    Valid syntax:
        BBCCVV
        BBCCVV-vv
        BBCCVV-ccvv
        BBCCVV-BBccvv
    """

    if len(bcv) == 6:
        return True

    elif len(bcv) == 9:
        return bcv[4:6] < bcv[7:9]

    elif len(bcv) == 11:
        return bcv[2:4] < bcv[7:9] or (bcv[2:4] == bcv[7:9] and bcv[4:6] < bcv[9:11])

    elif len(bcv) == 13:
        return bcv[0:2] == bcv[7:9] and (bcv[2:4] < bcv[9:11] or (bcv[2:4] == bcv[9:11] and bcv[4:6] < bcv[11:13]))

    else:
        return False

def expandBcv(bcv):
    """If the bcv is an interval, expand if.
    """

    if len(bcv) == 6:
        return bcv
    else:
        return "-".join(splitBcv(bcv))

def splitBcv(bcv):
    """Split a valid bcv interval.
    """

    if len(bcv) == 6:
        return bcv, bcv

    elif len(bcv) == 9:
        return bcv[0:6], bcv[0:4]+bcv[7:9]

    elif len(bcv) == 11:
        return bcv[0:6], bcv[0:2]+bcv[7:11]

    elif len(bcv) == 13:
        return bcv[0:6], bcv[7:13]

    else:
        None, None
