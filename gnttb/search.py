#! /usr/bin/python3
# -*- coding:utf-8 -*-

from .sblgnt import morphgnt_rows
from .sblgnt import sblgnt_books
from .verse  import Verse

def search(lemma, ccatParse_ref = '', books = sblgnt_books.keys()):
    """Produce the concordance of the given lemma searching it
    in given books (default: all books of the NT).

    ccat-parse: results can be filtered by a parsing code
    books: list of ids of books where the lemma is searched

    Notice: about parsing code, see the README.md file of the
            sblgnt library.
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
                # If set, apply the parsing code filter
                if ccatParse_ref != '':
                    keep_verse = compare_ccatParse(ccatParse_ref, word['ccat-parse'])
                else:
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

def compare_ccatParse(ref, ccatParse):
    """Compare a parsing code (ccat-parse) to a reference.
    Wildcard (*) accepted.

    A parsing code is a 8-char word:
        person (1=1st, 2=2nd, 3=3rd)
        tense (P=present, I=imperfect, F=future, A=aorist, X=perfect, Y=pluperfect)
        voice (A=active, M=middle, P=passive)
        mood (I=indicative, D=imperative, S=subjunctive, O=optative, N=infinitive, P=participle)
        case (N=nominative, G=genitive, D=dative, A=accusative)
        number (S=singular, P=plural)
        gender (M=masculine, F=feminine, N=neuter)
        degree (C=comparative, S=superlative)

    Examples:
        compare_ccatParsr('*PAI-*--', '1PAI-S--') --> True
        compare_ccatParsr('****-P--', '1PAI-S--') --> False

    Notice: about parsing code, see the README.md file of the
            sblgnt library.
    """

    for i, j in zip(ref, ccatParse):
        if i == '*': continue
        if i != j : return False

    return True
