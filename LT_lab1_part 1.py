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


def score_sim(source_path, method, ic=brown_ic): #gives default value to make this IC arg optional     

    with open(source_path, "r") as source:
        words_missing = 0
        human_scores = []
        sim_score = []
        
        #read in the source file of word pairs
        for line in source.readlines():
            line = line.strip()
            entry = line.split('\t')
                
            synsets_1 = {}
            synsets_2 = {}
            
            #save all of the available synsets for each word in the pair to a dictionary
            synsets_1[entry[0]] = wn.synsets(entry[0])
            synsets_2[entry[1]] = wn.synsets(entry[1])
            
    
            #extract list value from each dictionary entry and assign to new list
            for key in synsets_1:
                set_1 = synsets_1[key]
            for key in synsets_2:
                set_2 = synsets_2[key]
    

            #get rid of adjective entries for methods that don't cover adjectives
            if method == "jcn" or "res" or "lin":                
                for i in set_1:
                    if i.pos() == "a":
                        print(entry)
                        words_missing += 1           
                        break #go back to top 
                for i in set_2:
                    if i.pos() == "a":
#                        print(entry)
                        words_missing += 1
                        break
            
            #if entry remains, save the human score from each line
                human_scores.append(entry[2])      
                            
                int_pairs = [(syn1, syn2) for syn1 in set_1 for syn2 in set_2]
                
                int_pairs_2 = []
                
                for (a, b) in int_pairs:
                    if a.pos() == b.pos():
                        int_pairs_2.append((a, b))
                
                int_scores = {} #interim scores list to take max values from
         
            
                for (a, b) in int_pairs_2:
                    int_scores[(a, b)] = method(a, b, brown_ic)
                    if int_scores[(a, b)] is None:
                        del(int_scores[(a,b)])
    #                if a.pos() == "a" or b.pos() == "a":
    #                    print(entry)
                                
                scores = int_scores.values()
                
                max_score = max(scores)
                sim_score.append(max_score)
        
        spearman = stats.spearmanr(human_scores, sim_score)
        return(spearman[0].round(4))
        
print("Spearman Rho correlation using Path Similarity: ", score_sim("/Users/andrewpelkey/Desktop/ws353.tsv", path))
print("Spearman Rho correlation using Wu-Palmer Similarity: ", score_sim("/Users/andrewpelkey/Desktop/ws353.tsv", wup))
print("Spearman Rho correlation using Leacock-Chodorow Similarity: ", score_sim("/Users/andrewpelkey/Desktop/ws353.tsv", lch))
print("Spearman Rho correlation using Jiang-Conrath Similarity: ", score_sim("/Users/andrewpelkey/Desktop/ws353.tsv", jcn))
print("Spearman Rho correlation using Resnik Similarity: ", score_sim("/Users/andrewpelkey/Desktop/ws353.tsv", res))
print("Spearman Rho correlation using Lin Similarity: ", score_sim("/Users/andrewpelkey/Desktop/ws353.tsv", lin))


           
