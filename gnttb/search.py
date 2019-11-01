#! /usr/bin/python3
# -*- coding:utf-8 -*-

from .sblgnt import morphgnt_rows
from .sblgnt import sblgnt_books
from .verse  import Verse

def search(lemma, books = sblgnt_books.keys()):
    """Produce the concordance of the given lemma searching it
    in given books (default: all books of the NT).

    books: list of ids of books where the lemma is searched
    """

    results = []            # list book by book verses containing
                            # the lemma
    last_bcv = ''           # bcv of the last read verse
    keep_verse = False      # rise this flag to keep the current verse

    current_verse = None
    
    for book_id in books:
        # Verses are read word by word.
        # If a verse fills the search criteria, it is kept.

        verses = []             # list of verses of this book
                                # containing the lemma

        for word in morphgnt_rows(book_id):
        
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

        # if verses were found, push them in results
        if len(verses) > 0:
            results += [(book_id, verses),]

    return results
