'''

Created on Oct 4, 2016u
@author: hari

from dataextraction.DataExtracter import DataExtracter
d1 = DataExtracter()
counterList,uniqueWordSET,totalCount,allentries = d1.dataExtracter("xml20")
'''

import time

import os

systemPath = (os.getcwd()[:-3]) 


totalCounter = []

from dataextraction.DataExtracter import DataExtracter
import multiprocessing
import sys
THREADS = 1
GLOBALLOCK = multiprocessing.Lock()

def func1(test1):
    d1 = DataExtracter()
    counterList,uniqueWordSET,totalCount,allentries,tc,correctEntries = d1.dataExtracter(test1)
    descFile = open(systemPath+"data/wd/"+test1+".csv","w")
    uniqueWordFile = open(systemPath+"data/Word/"+test1+"Unique.txt","w")
    correctEntriesFile = open(systemPath+"data/Word/"+test1+"CorrectEntries_4400.txt","w")
    descFile.write(allentries)
    uniqueWordFile.write(uniqueWordSET)
    descFile.close()
    uniqueWordFile.close()
    correctEntriesFile.write(correctEntries)
    print(tc,"Test")   
pool = multiprocessing.Pool(THREADS)


func_args = [('xml20'),
             #('xml21'),('xml22'),('xml23'),('xml24'),('xml25'),
              # ('xml26'),('xml27'),
              #('xml28'),('xml29'),('xml30'),
              #('xml31'),('xml32'),('xml33'),('xml34'),('xml35')
              #,('xml36'),('xml37'),('xml38'),('xml39'),('xml40'),
              #('xml41'),('xml42'),('xml43'),
#              ('xml44'),('xml45'),('xml46'),('xml47'),('xml48'),('xml49'),('xml50'),
            ]
try:
    pool.map_async(func1, func_args).get(9999999)
except KeyboardInterrupt:
        # Allow ^C to interrupt from any thread.
        sys.stdout.write('\033[0m')
        sys.stdout.write('User Interupt\n')
pool.close()

print(totalCounter)


uniqueWordListSET = set([])

import glob, os
os.chdir(systemPath+"data/Word/")
for file1 in glob.glob("*.txt"):
    print(file1)
    uniqueWordListFile = open(systemPath+'/data/Word/'+file1,'r')
    uniqueWordEntry = (uniqueWordListFile.readline()).split(' ')
    print(len(uniqueWordEntry))
    for uniqueWord in uniqueWordEntry:
        uniqueWordListSET.add(uniqueWord)
uniqueFinal = open(systemPath+"data/Word/finalUniqueWordList.csv","w")
print(len(uniqueWordListSET)) 
uniqueFinal.write('\n'.join(uniqueWordListSET))
uniqueFinal.close()


import multiprocessing
import sys
from vectorspace.Words2Vector import Words2Vector

THREADS = 11
GLOBALLOCK = multiprocessing.Lock()

def func2(test1):
    allEntries = []
    partition = open(systemPath+'data/wd/'+test1+'.csv','r')
    partitionEntries = partition.readlines()
    for partitionEntry in partitionEntries:
        allEntries.append(partitionEntry)
    q1 =Words2Vector()
    q1.tfidfWeightCreater(test1,uniqueWordListSET,allEntries,systemPath)

pool = multiprocessing.Pool(THREADS)

func_args = [('xml20')
             #,('xml21'),('xml22'),('xml23'),('xml24'),('xml25'),
               #('xml26'),('xml27'),
#              ('xml28'),('xml29'),('xml30'),('xml31'),('xml32'),('xml33'),('xml34'),('xml35'),
#              ('xml36'),('xml37'),('xml38'),('xml39'),('xml40'),('xml41'),('xml42'),('xml43'),
#              ('xml44'),('xml45'),('xml46'),('xml47'),('xml48'),('xml49'),('xml50'),
            ]
try:
    pool.map_async(func2, func_args).get(9999999)
except KeyboardInterrupt:
        # Allow ^C to interrupt from any thread.
        sys.stdout.write('\033[0m')
        sys.stdout.write('User Interupt\n')
pool.close()


import glob,os
os.chdir(systemPath+"data/wd/")
uniqueWordCheckEntries = ""
for file1 in glob.glob("uniqueWordCheck*.csv"):
    print(file1)
    uniqueWordListFile = open(systemPath+'data/wd/'+file1,'r')
    uniqueWordcheckEnts = uniqueWordListFile.readlines()
    unq = ""
    for uniqueWordcheckEnt in uniqueWordcheckEnts:
        unq1 = uniqueWordcheckEnt  
        unq = unq + unq1
    uniqueWordCheckEntries = uniqueWordCheckEntries + unq + "\n"
uniqueWordCheckFile = open(systemPath+"data/wd/1uniqueWordCheck.csv", 'w')
uniqueWordCheckFile.write(uniqueWordCheckEntries)
uniqueWordCheckFile.close()

print("HI")
from vectorspace.Words2Vector import Words2Vector
q1 =Words2Vector()
#q1.tfidfWeightCreater(uniqueWordListSET,allEntries)
q1.documentFrequencyCreator(systemPath)

import glob,os
os.chdir(systemPath+"data/wd/")
tfScoreEntry = ""
for file1 in glob.glob("tfScorexml*.csv"):
    print(file1)
    tfScoreEntryFile = open(systemPath+'data/wd/'+file1,'r')
    tfScoreEntries = tfScoreEntryFile.readlines()
    tfq = ""
    for tfScoreEnt in tfScoreEntries:
        tfq = tfq + tfScoreEnt 
    tfScoreEntry = tfScoreEntry + tfq + "\n"
tfScoreEntryFile1 = open(systemPath+"data/wd/tfScore123.csv", 'w')
tfScoreEntryFile1.write(tfScoreEntry)
tfScoreEntryFile1.close()

import glob,os
os.chdir(systemPath+"data/wd/")
tfCountEntry = ""
for file1 in glob.glob("tfCount*.csv"):
    print(file1)
    tfCountEntryFile = open(systemPath+'data/wd/'+file1,'r')
    tfCountEntries = tfCountEntryFile.readlines()
    tfq = ""
    for tfCountEnt in tfCountEntries:
        tfq = tfq + tfCountEnt 
    tfCountEntry = tfCountEntry + tfq + "\n"
tfCountEntryFile = open(systemPath+"data/wd/tfCount1234.csv", 'w')
tfCountEntryFile.write(tfCountEntry)
tfCountEntryFile.close()



import multiprocessing
import sys
from vectorspace.AttributeMatrixCreator import AttributeMatrixCreator 

THREADS = 11
GLOBALLOCK = multiprocessing.Lock()

def func3(file1):
    tfScoreEntryFile = open(systemPath+'data/wd/'+file1+ ".csv",'r')
    tfScoreEntries = tfScoreEntryFile.readlines()
    tfentries = []
    for tfEntry in tfScoreEntries:
        tfentries.append(tfEntry)
    a1 = AttributeMatrixCreator()
    a1.weightedTFIDMatrixCreator(tfentries,file1,systemPath)

pool = multiprocessing.Pool(THREADS)

    # Define two jobs, each with two args.

''' ,'''
func_args = [('tfScorexml20'),
             #('tfScorexml21'),('tfScorexml22'),('tfScorexml23'),
             #('tfScorexml24'),('tfScorexml25'),
               #('tfScorexml26'),('tfScorexml27'),
#              ('tfScorexml28'),('tfScorexml29'),('tfScorexml30'),('tfScorexml31'),
#              ('tfScorexml32'),('tfScorexml33'),('tfScorexml34'),('tfScorexml35'),
#              ('tfScorexml36'),('tfScorexml37'),('tfScorexml38'),('tfScorexml39'),
#              ('tfScorexml40'),('tfScorexml41'),('tfScorexml42'),('tfScorexml43'),
#              ('tfScorexml44'),('tfScorexml45'),('tfScorexml46'),('tfScorexml47'),
#              ('tfScorexml48'),('tfScorexml49'),('tfScorexml50'),
            ]
try:
    pool.map_async(func3, func_args).get(9999999)
except KeyboardInterrupt:
        # Allow ^C to interrupt from any thread.
        sys.stdout.write('\033[0m')
        sys.stdout.write('User Interupt\n')
pool.close()


import glob,os
os.chdir(systemPath+"data/jhg/")
wtfidfEntryF = ""
for file1 in glob.glob("*.csv"):
    print(file1)
    wtfidfEntryFile = open(systemPath+'data/jhg/'+file1,'r')
    wtfidfEntires = wtfidfEntryFile.readlines()
    tfq = ""
    for wtfidfEntry in wtfidfEntires:
        tfq1 = wtfidfEntry 
        tfq = tfq + tfq1
    wtfidfEntryF = wtfidfEntryF + tfq + "\n"
wtfidFile = open(systemPath+"data/wd/wtfidf123444.csv", 'w')
wtfidFile.write(wtfidfEntryF)
wtfidFile.close()

from dimensionreduction.SVDimensionality import SVDimensionality
start_time = time.time()
sv = SVDimensionality()
sv.performSVD(systemPath)
print("--- %s seconds ---" % (time.time() - start_time))

'''
from SentenceModel.StatistiK import StatistiK

sm = StatistiK()
sm.sentenceLen(systemPath)



from languagemodel.POSTagger import POSTagger

pos = POSTagger()
pos.posTag(systemPath)


# from categorization.LDA1 import LDA1
# 
# ld = LDA1()
# ld.makeLDA()

'''