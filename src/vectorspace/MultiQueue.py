from __future__ import division
import Queue
import threading
import urllib2
import re
import csv
from collections import defaultdict
from math import log10
from collections import Counter
tfscoreIII = ""
uniqueWordChecIII = ""
count12 = 0
class MultiQueue(object):
    '''
    In this class a word to vector concept is implemented.
    Weighted IDF score is assigned to each word of the uniqueWordList corpus 
    '''
    def __init__(self):
        '''
        Constructor
        '''
        global tfscoreIII 
        global uniqueWordChecIII
    counterList1 = []
    uniqueWordSET1 = set([])
    count1 = 0
    entryCount = 0        
    def tfidfWeightCreater(self,uniqueWordSET,allentries,counterList):
        tfScoreFile = open("/home/hari/hari/DKE_Test/data/tfScore.csv", 'w')
        uniqueWordCheckFile = open("/home/hari/hari/DKE_Test/data/uniqueWordCheck.csv", 'w')
        uniqueWordListFile = open('/home/hari/hari/DKE_Test/data/uniqueWordList.csv','r')
        uniqueWordsList = uniqueWordListFile.readline()
        uniqueWordListFile.close()
        f = open('/home/hari/hari/DKE_Test/data/test2.csv','r')
        global counterList1
        global uniqueWordSET1
        counterList1 = counterList
        uniqueWordSET1 = uniqueWordSET 
        #entries = f.readlines()
        q = Queue.Queue()
        for entry in allentries:
            q.put(entry)
        #load up a queue wit-h your data, this will handle locking
        def worker(queue):
            count1 = 0
            queue_full = True
            global entryCount
            global tfscoreIII
            global uniqueWordChecIII
            global count12
            while queue_full:
                try:
                    #get your data off the queue, and do some work
                    entry= queue.get(False)
                    data = entry
                    uniqueWordCheck = ""
                    tfCount = ""
                    uniquWC = 0
                    entryWords = entry.split(" ")
                    docfreq = len(entryWords)
                    count12 = count12 + 1
                    for uniqueWord in uniqueWordSET1:
                        freqCount  = entry.count(uniqueWord)
                        if freqCount != 0:
                            uniqueWordCheck = ",".join((uniqueWordCheck, "1"))
                            tfCount = tfCount + "," + str((1+log10(int(freqCount)/docfreq)))
                        else:
                            uniqueWordCheck = ",".join((uniqueWordCheck, "0"))
                            tfCount = tfCount + "," + str(0)
                        uniquWC = uniquWC + 1 
                    tf = tfCount.lstrip(',') + "\n"   
                    tfscoreIII = tfscoreIII + tf
                    uniqueWordChecIII = uniqueWordChecIII + uniqueWordCheck.lstrip(',')+"\n" 
                    count1  = count1 + 1    
                    #print(tf)
                    #xtfScoreFile.write(tf)
                except Queue.Empty: 
                    queue_full = False
        
        thread_count = 4
        for i in range(thread_count):
            t = threading.Thread(target=worker, args = (q,))
            t.start()    
        uniqueWordCheckFile.write(uniqueWordChecIII)
         
    #create as many threads as you want
    