#! /usr/bin/python3
# -*- coding:utf-8 -*-

import os.path

# List of books of the NT.
#   - abbrevations used in files names
#   - abbrevations used by the Bible de Jérusalem
sblgnt_books = {
        '01' : ('Mt', 'Mt'),
        '02' : ('Mk', 'Mc'),
        '03' : ('Lk', 'Lc'),
        '04' : ('Jn', 'Jn'),
        '05' : ('Ac', 'Ac'),
        '06' : ('Ro', 'Ro'),
        '07' : ('1Co', '1Co'),
        '08' : ('2Co', '2Co'),
        '09' : ('Ga', 'Ga'),
        '10' : ('Eph', 'Ep'),
        '11' : ('Php', 'Ph'),
        '12' : ('Col', 'Col'),
        '13' : ('1Th', '1Th'),
        '14' : ('2Th', '2Th'),
        '15' : ('1Ti', '1Ti'),
        '16' : ('2Ti', '2Ti'),
        '17' : ('Tit', 'Tt'),
        '18' : ('Phm', 'Phm'),
        '19' : ('Heb', 'He'),
        '20' : ('Jas', 'Jc'),
        '21' : ('1Pe', '1P'),
        '22' : ('2Pe', '2P'),
        '23' : ('1Jn', '1Jn'),
        '24' : ('2Jn', '2Jn'),
        '25' : ('3Jn', '3Jn'),
        '26' : ('Jud', 'Jude'),
        '27' : ('Re', 'Ap')}


def morphgnt_filename(book_num):
    """
    return the MorphGNT filename of the given book number.
    e.g. 1 will return "61-Mt-morphgnt.txt"

    Fork from py-sblgnt by jtauber distributed under a MIT Licence (https://github.com/morphgnt/py-sblgnt)
    """

    return "sblgnt/{}-{}-morphgnt.txt".format(
        60 + book_num, sblgnt_books["{:0>2}".format(book_num)][0]
    )


def morphgnt_rows(book_num):
    """
    yield a dict for each MorphGNT/SBLGNT row in the given book number.

    Fork from py-sblgnt by jtauber distributed under a MIT Licence (https://github.com/morphgnt/py-sblgnt)
    """
    filename = os.path.join(
        os.path.dirname(__file__),
        morphgnt_filename(book_num),
    )

    with open(filename) as f:
        for line in f:
            yield dict(zip(
                (
                    "bcv", "ccat-pos", "ccat-parse", #"robinson",
                    "text", "word", "norm", "lemma"
                ),
                line.strip().split()
            ))
