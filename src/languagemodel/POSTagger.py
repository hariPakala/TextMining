
'''
Created on Oct 12, 2016

@author: hari
'''
import nltk 
from nltk.tokenize import word_tokenize
import re

class POSTagger(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def posTag(self,filename,systemPath):
        import glob, os
        partSpeechFile = open(systemPath+"data/partSpeech_"+filename+".txt","w")
        allEntries = []
        correctEntryFile = open(systemPath+"data/"+filename+ ".csv",'r')
        correctEntries = correctEntryFile.readlines()
        for correctEntry in correctEntries:
            allEntries.append(correctEntry)
        correctEntryFile.close()
        pSpeech = []
        i = 0
        for entry in allEntries:
            cleanString = (re.sub('[^a-zA-Z]', ' ', entry))
            cleanString1 = (re.sub('#', "ff", cleanString))
            textTest = word_tokenize(cleanString1)
            pss = nltk.pos_tag(textTest)
            for ps in pss:
                ci = 0
                for s in ps:
                    if ci == 1:
                        pSpeech.append(s)
                    ci = ci + 1
            i = i +1
        print(i)
        bigram = nltk.bigrams(pSpeech)
        bigramList = []
        for bg in bigram:
            bigramList.append(bg[0]+":"+bg[1])
        print(len(pSpeech))
        for bgram in bigramList:
            print(bgram)
        partSpeechFile.write(','.join(bigramList))
        partSpeechFile.close()   
