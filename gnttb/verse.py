#! /usr/bin/python3
# -*- coding:utf-8 -*-

class Verse:
    """Custom data structure to store and manipulate a verse.
    """

    def __init__(self, bcv):
        # List of words in sentence order.
        # Each word is a dict as returned by sblgnt.morphgnt_rows()
        self.morph_words = []
        self.bcv = bcv

    def append(self, morph_word):
        """Append a word at the end of the verse.
        """

        self.morph_words += [morph_word, ]
        return self

    def __iadd__(self, morph_word):
        """The += arithmetic assignement calls the append method.
        """

        return self.append(morph_word)

    def __getitem__(self, n):
        """Get the word in n position.
        """

        return self.morph_words[n]

    def __len__(self):
        """Len of the verse.
        """

        return len(self.morph_words)

    def __str__(self):
        """Display the verse.
        """

        # Recover the list of words in sentence order from morph_words
        return ' '.join([w['text'] for w in self.morph_words])
