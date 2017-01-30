'''
Created on Sep 30, 2016

@author: hari
'''
import csv
from collections import defaultdict
import json


class AttributeMatrixCreator(object):
    '''
    In this class Weighted TF-IDF matrix is created for the entire document collection
    '''
    def __init__(self):
        '''
        Constructor
        '''
    def weightedTFIDMatrixCreator(self,tfentries,file1,systemPath):
        columns = defaultdict(list)
        weightedtfIdfI = ""
        with open(systemPath+'data/idfFrequencyCountFile.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                for (i,v) in enumerate(row):
                    columns[i].append(float(v.replace(" ","")))
        #tfScoreFile = open("/home/hari/hari/DKE_Test/data/wd/tfScore123.csv", 'r')
        wtfidfScoreFile = open(systemPath+"data/jhg/wtfidfScore_"+file1+".csv", 'w')
        #entries = tfScoreFile.readlines()
        j = 0
        for entry in tfentries:
            i = 0
            weightedtfIdf = ""
            tfwords = entry.split(",")
            for tfword in tfwords:
                weightedtfIdf = weightedtfIdf + "," + str(float(tfword.replace(" ", "")) *  sum(columns[i]))  
                i = i + 1
            j = j + 1
            print(j)   
            weightedtfIdfI = weightedtfIdfI + weightedtfIdf.lstrip(',') + "\n"    
        wtfidfScoreFile.write(weightedtfIdfI) 
        wtfidfScoreFile.close()
               