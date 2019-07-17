#! /usr/bin/python3
# -*- coding:utf-8 -*-

from .sblgnt import morphgnt_rows

# Define some functions.

def bcv2str(bcv):
    """Convert a bcv into a string using the BJ convention.
    """

    return '{} {}, {}'.format(bcv_books[bcv[0:2]], int(bcv[2:4]), int(bcv[4:6]))


def search(lemma):
    """Produce the concordance of the given lemma searching it
    in the New Testament.
    """

    verse = ''
    verses = []
    last_bcv = ''
    print_verse = False
    
    for book_num in range(1, 4):
        for row in morphgnt_rows(book_num):
        
            if row['bcv'] != last_bcv:
                # New verse
                if print_verse:
                    verses += [verse,]
                    #print('{} : {}'.format(bcv2str(last_bcv), verse))
                    print_verse = False
        
                last_bcv = row['bcv']
                verse = ''
        
        
            if row['lemma'] == lemma:
                print_verse = True

            verse += row['text']
            verse += ' '

    return verses
