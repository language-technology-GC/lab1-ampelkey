#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:46:55 2020

@author: andrewpelkey
"""
import nltk
#nltk.download('wordnet')
#nltk.download('wordnet_ic')
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic as wn_ic
from scipy import stats


#def score_sim(method): #making a function to use with various methods

path = wn.path_similarity
wup = wn.wup_similarity
lch = wn.lch_similarity
jcn = wn.jcn_similarity
res = wn.res_similarity
lin = wn.lin_similarity

brown_ic = wn_ic.ic('ic-brown.dat')

with open("/Users/andrewpelkey/Desktop/ws353.tsv", "r") as source:
    words_missing = 0
    human_scores = []
    sim_score = []
    for line in source.readlines():
        line = line.strip()
        entry = line.split('\t')
        human_scores.append(entry[2])      
        
        synset_1 = wn.synsets(entry[0])[0]
        synset_2 = wn.synsets(entry[1])[0]
             
        sim = path(synset_1, synset_2)
        sim_score.append(sim) 
        for i in range(0, len(sim_score)):
            if sim_score[i] is None:
                words_missing += 1                
                human_scores.pop(i)
                sim_score.pop(i)
        spearman = stats.spearmanr(human_scores, sim_score)
             
    print("Spearman correlation using Path Similarity: ", spearman[0].round(4))    
    print(words_missing)    
        

