'''
Created on Sep 29, 2016

@author: hari
'''
from __future__ import division
import re
import csv
from collections import defaultdict
from math import log10
from collections import Counter


class Words2Vector(object):
    '''
    In this class a word to vector concept is implemented.
    Weighted IDF score is assigned to each word of the uniqueWordList corpus 
    '''
    def __init__(self):
        '''
        Constructor
        '''
    def tfidfWeightCreater(self,file2,uniqueWordSET,allentries,systemPath):
        tfScoreFile = open(systemPath+"data/wd/tfScore"+file2+".csv", 'w')
        tfCountFile = open(systemPath+"data/wd/tfCount"+file2+".csv", 'w')
        uniqueWordCheckFile = open(systemPath+"data/wd/uniqueWordCheck"+file2+".csv", 'w')
        uniqueWordListFile = open(systemPath+"data/Word/finalUniqueWordList.csv",'r')
        uniqueWordsList = uniqueWordListFile.readline()
        uniqueWordListFile.close()
        #f = open('/home/hari/hari/DKE_Test/data/test2.csv','r')
        count1 = 0
        tfscoreIII = []
        tfCountIII = []
        entryCount = 0
        uniqueWordChecIII = []
        for entry in allentries:
            uniqueWordCheck = []
            tfCount = []
            tfCount1 = []
            uniquWC = 0
            entryWords = entry.split(" ")
            counter1 = Counter(entryWords)
            docfreq = len(entryWords)
            for uniqueWord in uniqueWordSET:
                freqCount  = counter1.get(uniqueWord)
                if freqCount != None:
                    uniqueWordCheck.append("1")
                    tfCount.append(str((1+log10(int(freqCount)/docfreq))))
                    tfCount1.append(str(freqCount))
                else:
                    uniqueWordCheck.append("0")
                    tfCount.append("0")
                    tfCount1.append("0")
                uniquWC = uniquWC + 1 
            tfscoreIII.append( ','.join(tfCount))
            tfCountIII.append(",".join(tfCount1))
            uniqueWordChecIII.append(','.join(uniqueWordCheck)) 
            count1  = count1 + 1
            print(count1)
        tfScoreFile.write('\n'.join(tfscoreIII))    
        uniqueWordCheckFile.write('\n'.join(uniqueWordChecIII))
        tfCountFile.write('\n'.join(tfCountIII))
        tfScoreFile.close()
        uniqueWordCheckFile.close()
    
    def documentFrequencyCreator(self,systemPath):
        columns = defaultdict(list)
        numberofEntries = 0
        
        #totalWordCountFile = open('/home/hari/hari/DKE_Test/data/totalWordCount.csv','r')
        #twCount = int(totalWordCountFile.readline())
        #print twCount   
        
        with open(systemPath+'data/wd/1uniqueWordCheck.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                for (i,v) in enumerate(row):
                    columns[i].append(int(v))
                    numberofEntries = i
                    #print(columns[i])
        idfCount = ""
        entry = len(columns[1])
        print(entry)
        idfFrequency = ""
        for i in range(0,numberofEntries):
            sumT = sum(columns[i])
            if sumT != 0:
                idfCount = idfCount + str(sumT)
                #print(sumT)
                idfFrequency = idfFrequency + str(log10(entry/sumT)) + ","
            else:
                idfCount = idfCount + str(sumT)
                idfFrequency = idfFrequency + "0" + ","
        #print(idfCount)
        #print(idfFrequency)
        idfFrequencyCountFile = open(systemPath+'data/idfFrequencyCountFile.csv','w')
        idfFrequencyCountFile.write(idfFrequency.rstrip(','))
        idfFrequencyCountFile.close()
        
   