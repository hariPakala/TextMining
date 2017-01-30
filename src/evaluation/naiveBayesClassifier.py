'''
Created on Nov 16, 2016

@author: hari
'''
from __future__ import division
import math

class naiveBayesClassifier(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def getProbabilties(self, bigramList,systemPath):
        
        goodEntriesFile = open(systemPath+"data/probabilities_GoodEntries.txt","r")
        badEntriesFile = open(systemPath+"data/probabilities_BadEntries.txt","r")

        goodEntries = goodEntriesFile.readlines()
        badEntries = badEntriesFile.readlines()
        goodEntriesFile.close()
        badEntriesFile.close()
        goodProbability = 0.0000
        badProbability = 0.0000
        for bg in bigramList:
            gcount = 0
            bcount = 0
            for gEnt in goodEntries:
                ge = gEnt.split(',')
                if bg == ge[0]:
                    gcount = 1
                    x = float(ge[1].rstrip('\n'))
                    goodProbability = goodProbability + (math.log10(x))
            if gcount == 0:
                goodProbability = goodProbability + math.log10(0.0000000001)
            for bEnt in badEntries:
                be = bEnt.split(',')
                if bg == be[0]:
                    bcount = 1
                    y = float(be[1].rstrip('\n'))
                    badProbability = goodProbability + (math.log10(y))
            if bcount == 0:
                goodProbability = goodProbability + math.log10(0.0000000001)
        return goodProbability,badProbability 
                    