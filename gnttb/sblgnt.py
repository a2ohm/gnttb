#! /usr/bin/python3
# -*- coding:utf-8 -*-

import os.path
import collections

# Define a namedtuple to store names of books in different edition
# of the New Testament.
BookNames = collections.namedtuple('BookNames', ['en', 'BJ'])

# List of books of the NT.
#   - abbrevations used in files names
#   - abbrevations used by the Bible de Jérusalem
sblgnt_books = collections.OrderedDict([
        ('01' , BookNames('Mt', 'Mt')),
        ('02' , BookNames('Mk', 'Mc')),
        ('03' , BookNames('Lk', 'Lc')),
        ('04' , BookNames('Jn', 'Jn')),
        ('05' , BookNames('Ac', 'Ac')),
        ('06' , BookNames('Ro', 'Ro')),
        ('07' , BookNames('1Co', '1Co')),
        ('08' , BookNames('2Co', '2Co')),
        ('09' , BookNames('Ga', 'Ga')),
        ('10' , BookNames('Eph', 'Ep')),
        ('11' , BookNames('Php', 'Ph')),
        ('12' , BookNames('Col', 'Col')),
        ('13' , BookNames('1Th', '1Th')),
        ('14' , BookNames('2Th', '2Th')),
        ('15' , BookNames('1Ti', '1Ti')),
        ('16' , BookNames('2Ti', '2Ti')),
        ('17' , BookNames('Tit', 'Tt')),
        ('18' , BookNames('Phm', 'Phm')),
        ('19' , BookNames('Heb', 'He')),
        ('20' , BookNames('Jas', 'Jc')),
        ('21' , BookNames('1Pe', '1P')),
        ('22' , BookNames('2Pe', '2P')),
        ('23' , BookNames('1Jn', '1Jn')),
        ('24' , BookNames('2Jn', '2Jn')),
        ('25' , BookNames('3Jn', '3Jn')),
        ('26' , BookNames('Jud', 'Jude')),
        ('27' , BookNames('Re', 'Ap'))])


def morphgnt_filename(book_id):
    """
    return the MorphGNT filename of the given book id.
    e.g. 1 will return "61-Mt-morphgnt.txt"

    book_id is supposed to be one of sblgnt_book's keys (ie a string)

    Fork from py-sblgnt by jtauber distributed under a MIT Licence (https://github.com/morphgnt/py-sblgnt)
    """

    return "sblgnt/{}-{}-morphgnt.txt".format(
        60 + int(book_id), sblgnt_books[book_id][0]
    )


def morphgnt_rows(book_id):
    """
    yield a dict for each MorphGNT/SBLGNT row in the given book id.

    Fork from py-sblgnt by jtauber distributed under a MIT Licence (https://github.com/morphgnt/py-sblgnt)
    """
    filename = os.path.join(
        os.path.dirname(__file__),
        morphgnt_filename(book_id),
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
