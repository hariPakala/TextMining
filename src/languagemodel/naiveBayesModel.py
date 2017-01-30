'''
Created on Nov 15, 2016

@author: hari
'''
from __future__ import division
from collections import Counter

class naiveBayesModel(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def createProbabilities(self,systemPath):
        
        goodEntriesFile = open(systemPath+"data/partSpeech_GoodEntrys.txt","r")
        badEntriesFile = open(systemPath+"data/partSpeech_BadEntries.txt","r")
        
        goodEntries = (goodEntriesFile.readline()).split(',')
        badEntries = (badEntriesFile.readline()).split(',')

        
        uniquegoodEntries = set([])
        for ge in goodEntries:
            uniquegoodEntries.add(ge)             
        print(uniquegoodEntries)
        
        uniquebadEntries = set([])
        for be in badEntries:
            uniquebadEntries.add(be)             
        print(uniquebadEntries)
        
        goodEntriesCounter = Counter(goodEntries)
        badEntriesCounter =  Counter(badEntries)
        
        goodEntriesCount = len(goodEntries) 
        badEntriesCount = len(badEntries)
        
        probabilityGoodEntry = []
        
        for uge in uniquegoodEntries:
            x = goodEntriesCounter[uge]
            probabilityGoodEntry.append(uge+","+str(x/goodEntriesCount))
        
        probabilityBadEntry = []
        
        for ube in uniquebadEntries:
            x = badEntriesCounter[ube]
            probabilityBadEntry.append(ube+","+str(x/badEntriesCount))
            
        probabilityGoodEntryFile = open(systemPath+"data/probabilities_GoodEntries.txt","w")
        probabilityGoodEntryFile.write('\n'.join(probabilityGoodEntry)) 
        
        probabilityBadEntryFile = open(systemPath+"data/probabilities_BadEntries.txt","w")
        probabilityBadEntryFile.write('\n'.join(probabilityBadEntry)) 
        probabilityGoodEntryFile.close()
        probabilityBadEntryFile.close()