#! /usr/bin/python3
# -*- coding:utf-8 -*-

from .sblgnt import morphgnt_rows
from .sblgnt import sblgnt_books
from .verse  import Verse

def search(lemma):
    """Produce the concordance of the given lemma searching it
    in the New Testament.
    """

    verses = []             # list of verses containing lemma
    last_bcv = ''           # bcv of the last read verse
    keep_verse = False      # rise this flag to keep the current verse

    current_verse = None
    
    for book_num in sblgnt_books.keys():
        # Verses are read word by word.
        # If a verse fills the search criteria, it is kept.
        for word in morphgnt_rows(book_num):
        
            if word['bcv'] != last_bcv:
                # This is the first word of a new verse.

                # Check if the previous verse should be kept.
                if keep_verse:
                    verses += [current_verse,]
                    keep_verse = False
        
                # Start a new verse.
                last_bcv = word['bcv']
                current_verse = Verse(word['bcv'])
        
        
            # Rise the keep_verse flag if the current word and
            # the searched one match.
            if word['lemma'] == lemma:
                keep_verse = True

            current_verse += word

        # Check if the last verse should be kept.
        if keep_verse:
            verses += [current_verse,]
            keep_verse = False

    return verses
