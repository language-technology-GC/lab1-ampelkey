#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:07:11 2020

@author: andrewpelkey
"""

from scipy import stats

ppmi = []
human_score = []

from_ppmi_pairs = []
from_source_pairs = []

with open("ws353.tsv", "r") as compare: #need to learn convention for 
                                        #when I have two source files like this
    pairs = {}
    for line in compare:
        line = line.casefold().strip().split('\t')
        pairs[(line[0], line[1])] = line[2]   

    with open("results.txt", "r") as source:
        counter = 0
        for line in source:
            counter += 1
            line = line.strip().split('\t')
            for i in pairs:
                if i == (line[0], line[1]):
                    human_score.append(pairs[i])
                    ppmi.append(line[2])
                    break
                if i == (line[1], line[0]):
                    human_score.append(pairs[i])
                    ppmi.append(line[2])
                    

print(stats.spearmanr(human_score, ppmi)[0].round(4))
print(len(ppmi))
print(len(human_score))
print(counter)
            

