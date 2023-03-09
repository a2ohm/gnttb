#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Define functions relative to bcv.
"""

from .sblgnt import sblgnt_books

import re

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

def bcv2str(bcv, bookNamesFamily = 'BJ'):
    """Convert a bcv into a string using the BJ convention.
    """

    if len(bcv) == 6:
        return '{} {}, {}'.format(
                getattr(sblgnt_books[bcv[0:2]], bookNamesFamily),
                int(bcv[2:4]),
                int(bcv[4:6]))
    else:
        bcv_start, bcv_end = splitBcv(bcv)

        if bcv_start[2:4] == bcv_end[2:4]:
            # same chapter
            return '{} {}, {}-{}'.format(
                    getattr(sblgnt_books[bcv_start[0:2]], bookNamesFamily),
                    int(bcv_start[2:4]),
                    int(bcv_start[4:6]), int(bcv_end[4:6]))

        else:
            # different chapter
            return '{} {}, {} − {}, {}'.format(
                    getattr(sblgnt_books[bcv_start[0:2]], bookNamesFamily),
                    int(bcv_start[2:4]), int(bcv_start[4:6]), 
                    int(bcv_end[2:4]) ,int(bcv_end[4:6]))

def str2bcv(ref):
    """Convert a string reference to a bcv.
    """

    r_ref = r"(?P<book>[A-Z]\w{1,2}) (?P<chapter>\d+)(?:\s?,\s?(?P<verse_a>\d+)(?:\s?[-:]\s?(?P<verse_b>\d+))?)?"
    p_ref = re.compile(r_ref)
    m_ref = p_ref.match(ref)

    if m_ref:
        bookId = None

        # Get the book id
        for i, names in sblgnt_books.items():
            if m_ref['book'] in names:
                bookId = i
                break

        # Return the bcv
        if bookId:
            if m_ref['verse_b']:
                # bcv: BBCCVV-vv
                return "{}{:02}{:02}-{:02}".format(bookId, int(m_ref['chapter']), int(m_ref['verse_a']), int(m_ref['verse_b']))
            elif m_ref['verse_a']:
                # bcv: BBCCVV
                return "{}{:02}{:02}".format(bookId, int(m_ref['chapter']), int(m_ref['verse_a']))
            else:
                # bcv: BBCC
                return "{}{:02}".format(bookId, int(m_ref['chapter']))

    return None

