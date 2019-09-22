#! /usr/bin/python3
# -*- coding:utf-8 -*-

from .sblgnt import morphgnt_rows
from .get import get

# ###
# TMP
# def printM(m):
#     for row in m:
#         for e in row:
#             print("{:=3d} ".format(e), end='')
#         print()
# ###

def compare(verse1, verse2):
    """Using the Needleman–Wunsch algorithm, compare two verses given their bcv.
    """

    # Init the scoring matrix
    m = [[ 0 for _ in range(len(verse1) + 1)] for _ in range(len(verse2) + 1)]

    # Set scores
    sc_match = 2
    sc_smallmatch = 1
    sc_mismatch = -1
    sc_indel = -1

    # Fill the first row of the scoring matrix
    for x in range(1, len(verse1) + 1):
        m[0][x] = x*sc_indel

    # Fill the first column of the scoring matrix
    for y in range(1, len(verse2) + 1):
        m[y][0] = y*sc_indel

    # Fill the rest of the scoring matrix
    for y in range(1, len(verse2) + 1):
        for x in range(1, len(verse1) + 1):
            # score from left
            sc_left = m[y][x-1] + sc_indel

            # score from top
            sc_top = m[y-1][x] + sc_indel

            # score from top-left
            if verse1[x-1]['lemma'] == verse2[y-1]['lemma']:
                # Small matches receive a lower score
                if len(verse1[x-1]['lemma']) > 3:
                    sc_tl = m[y-1][x-1] + sc_match
                else:
                    sc_tl = m[y-1][x-1] + sc_smallmatch
            else:
                sc_tl = m[y-1][x-1] + sc_mismatch
            
            m[y][x] = max(sc_left, sc_top, sc_tl)

    # Rebuild aligned verse

    x = len(verse1)
    y = len(verse2)

    ## Init aligned verses
    averse1 = []
    averse2 = []

    while x > 0 or y > 0:
        # Update x and y looking at surounding scores
        sc_left = m[y][x-1]
        sc_top = m[y-1][x]
        sc_tl = m[y-1][x-1]

        if sc_tl >= max(sc_left, sc_top):
            # Update aligned verses
            averse1 += [verse1[x -1], ]
            averse2 += [verse2[y -1], ]

            x -= 1
            y -= 1

        elif sc_left > sc_top:
            # Update aligned verses
            averse1 += [verse1[x -1], ]
            averse2 += [None, ]

            x -= 1

        else:
            # Update aligned verses
            averse1 += [None, ]
            averse2 += [verse2[y -1], ]

            y -= 1

    averse1.reverse()
    averse2.reverse()

    return (averse1, averse2)
