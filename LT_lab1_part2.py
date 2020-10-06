#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 09:50:46 2020

@author: andrewpelkey
"""

import nltk
from nltk import word_tokenize
from nltk.util import ngrams
import csv


with open("/Users/andrewpelkey/Desktop/news.2013.en.shuffled.deduped", "r") as source:
    while True:
        text = source.readline()
        words = nltk.word_tokenize(text.strip())
        bigrams = nltk.ngrams(words, 2)
        with open("/Users/andrewpelkey/Desktop/bigrams.tsv", "a+") as f_out:
                f_out.write('\n'.join('{}''\t''{}'.format(x[0],x[1]) for x in list(bigrams)))          
        if text == '':
            break
        else:
            continue
