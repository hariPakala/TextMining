'''
Created on Oct 10, 2016

@author: hari
'''

import numpy as np
from collections import Counter
import statistics as st   
    
class StatistiK(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def sentenceLen(self,systemPath):
        import glob, os
        allEntries = []
        os.chdir(systemPath+"data/Word/")
        for file1 in glob.glob("*CorrectEntries.txt"):
            print(file1)
            correctEntryFile = open(systemPath+'data/Word/'+file1,'r')
            correctEntries = correctEntryFile.readlines()
            for correctEntry in correctEntries:
                allEntries.append(correctEntry)
            correctEntryFile.close()
        #goodEntriesFile = open('/home/hari/hari/DKE_Test/data/GoodEntrys.txt','r')
        print(len(allEntries))
        sentenceLength = 0
        sentenceLengthArray = []
        sentenceLengthStore = ""
        i = 0
        for entry in allEntries:
            sentences = entry.split('.')
            for sentence in sentences:
                senLen = len(sentence.split(" "))
                if senLen not in (1,2):
                    sentenceLength = sentenceLength + senLen
                    sentenceLengthStore = sentenceLengthStore + str(senLen) + ","
                    sentenceLengthArray.append(senLen)
                    i = i +1    
        #print(sentenceLengthArray)
        print(i)
        for go in sentenceLengthArray:
            print(go)
        counts= Counter(sentenceLengthArray)
        newlist = [s for s in sentenceLengthArray if  counts[s] >  4]  
        print(st.stdev(newlist),"std")
        #print(sentenceLengthStore.rstrip(','))
        print(sentenceLength / i)
        print(Counter(newlist))
        print(st.mean(newlist))
        goodList = [s for s in newlist if  s  >=  11 and s <= 33]
        badList1 = [s for s in newlist if  s <  11]
        badList2 = [s for s in newlist if  s > 33]
        for go in badList1:
            print(go)
        #print(badList)
        print(st.stdev(goodList),"Standard deviation of GoodList")
        print(st.mean(goodList),"Mean of Good List")
        print(st.stdev(badList1),"Standard deviation of BadList 1")
        print(st.mean(badList1),"Mean of BadList 1")
        print(st.stdev(badList2),"Standard deviation of BadList 2")
        print(st.mean(badList2),"Mean of BadList 2")
        
    
         