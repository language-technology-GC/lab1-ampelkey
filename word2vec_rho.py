#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:46:55 2020

@author: andrewpelkey
"""
from scipy import stats

word2vec = "/Users/andrewpelkey/.spyder-py3/gensim_results.txt"
ws353 = "/Users/andrewpelkey/.spyder-py3/ws353.tsv"

human = []
gensim = []

with open(ws353, "r") as source:
    for line in source:
        line = line.strip().split('\t')
        human.append(line[2])
        
with open(word2vec, "r") as source:
    for line in source:
        line = line.strip().split('\t')
        gensim.append(line[2])

spearman = stats.spearmanr(human, gensim)
print(spearman[0].round(4))
        
