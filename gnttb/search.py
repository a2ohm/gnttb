#! /usr/bin/python3
# -*- coding:utf-8 -*-

from .sblgnt import morphgnt_rows
from .verse  import Verse

def search(lemma):
    """Produce the concordance of the given lemma searching it
    in the New Testament.
    """

    verses = []             # list of verses containing lemma
    last_bcv = ''           # bcv of the last read verse
    keep_verse = False      # rise this flag to keep the current verse

    current_verse = None
    
    for book_num in range(1, 4):
        for row in morphgnt_rows(book_num):
        
            if row['bcv'] != last_bcv:
                # This is a new verse.

                # Check if the previous verse should be kept.
                if keep_verse:
                    verses += [current_verse,]
                    keep_verse = False
        
                last_bcv = row['bcv']
                current_verse = Verse(row['bcv'])
        
        
            if row['lemma'] == lemma:
                keep_verse = True

            current_verse += row

        # Check if the last verse should be kept.
        if keep_verse:
            verses += [current_verse,]
            keep_verse = False

    return verses
