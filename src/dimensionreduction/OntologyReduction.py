'''
Created on Sep 29, 2016

@author: hari
'''
from collections import Counter
from dimensionreduction.SynonymMixer import SynonymMixer

class OntologyReduction:
    '''
    In this class we consume the raw data that is cleaned from special characters
    and punctuation marks in the previous task, attempt to reduce the Dimensionality
    of the word corpus.
    Another part of this module is to create word list corpus of unique words  
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
    def OntoReduction1(self,systemPath):
        counterList = []
        uniqueWordList = set([])
        sMixer = SynonymMixer()
        descFile = open(systemPath+"data/t222.csv","w")
        with open(systemPath+"data/test2.csv") as fp:
            for line in fp:
                print line
                if line != None:
                    ors,uniqueWordList = sMixer.synonymExtracter(line,uniqueWordList) 
                    ontologyReducedSting = ors +  "\n"
                    descFile.write(ontologyReducedSting)
                    counts = Counter(ontologyReducedSting.split())
                    counterList.append(counts)
        descFile.close()
        print("End Ontology")
        return counterList, uniqueWordList
    def uniqueWordExtracter(self,systemPath):
        f = open(systemPath+"data/test2.csv","r")
        entries = f.readlines()
        f.close()
        uniqueWordList = []
        uniqueWordListFile1 = ""
        totalwordCount = 0
        totalUniqueWordCount = 0
        for entry in entries:
            wordEntries = entry.split()
            for wordEntry in wordEntries:
                totalwordCount = totalwordCount + 1
                if wordEntry not in uniqueWordList:
                    uniqueWordList.append(wordEntry)
                    uniqueWordListFile1 = " ".join((uniqueWordListFile1, wordEntry))
                    totalUniqueWordCount = totalUniqueWordCount + 1
        #print str(totalUniqueWordCount) + "," + str(totalwordCount)
        uniqueWordListFile = open(systemPath+"data/uniqueWordList.csv", 'w')
        uniqueWordCountFile = open(systemPath+"data/uniqueWordCount.csv", 'w')
        totalWordCountFile = open(systemPath+"data/totalWordCount.csv", 'w')
        uniqueWordListFile.write(uniqueWordListFile1)
        uniqueWordCountFile.write(str(totalwordCount))
        totalWordCountFile.write(str(totalUniqueWordCount))
        
        uniqueWordListFile.close()
        uniqueWordCountFile.close()
        totalWordCountFile.close()
        