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


'''
with open("news.2013.en.shuffled.deduped", "r") as source:
    with open ("tokens.txt", "w") as sink:
        for line in source:
            words = nltk.word_tokenize(line.strip())
            print(" ".join(words), file=sink)

'''
with open("/Users/andrewpelkey/Desktop/ws353.tsv", "r") as source:
    with open("/Users/andrewpelkey/Desktop/ws353_pairs.tsv", "w") as sink:
        for line in source.readlines():
            line = line.split('\t')
            pair = []
            pair.append(line[0])
            pair.append(line[1])
            print("\t".join(pair), file=sink)