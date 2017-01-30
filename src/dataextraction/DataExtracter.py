'''
Created on Sep 26, 2016

@author: harish
'''

import xml.etree.ElementTree as ET

import glob, os
import re
from nltk.tokenize import word_tokenize
from dataextraction.StopWords import StopWords
from collections import Counter
from dimensionreduction.SynonymMixer import SynonymMixer
class DataExtracter:
    '''
    
    This class is used for raw Data Extraction. Entries are extracted
    from the XML files
    
    '''
    def __init__(self):
        '''
        Constructor
        '''
    def dataExtracter(self,folder):
        systemPath = (os.getcwd()[:-3]) 
        os.chdir(systemPath+"data/wd/dt/"+folder)
        counterList = []
        uniqueWordList = set([])
        allentries = []
        correctEntries = []
        finalStringFile = []
        rawString = []
        totalCount = 0
        tc = 0
        sMixer = SynonymMixer()
        stopset1 = StopWords()
        stopset = stopset1.getStopWordList()
        for fileXml in glob.glob("*.xml"): 
            '''  Considering all the xml files in the given folder '''
            tree = ET.parse(fileXml)
            root = tree.getroot()
            for child in root:
                '''Here we extract the description of each Entry with in an XML File'''
                for x in child.iter('{http://purl.org/dc/elements/1.1/}description'):
                    if x.text != None:
                        f1 = str(x.text.encode('utf8'))
                        f1 = (re.sub('#', "ff", f1))
                        correctEntries .append(f1)
                        cleanString = (re.sub('[^a-zA-Z]', " ", f1)).split()
                        '''
                        From this Description all the special characters are
                        removed and also the stop words (This is for Data Mining Purpose)
                        '''
                        cleanString  = [word for word in cleanString if ((word.upper() not in stopset)  & (len(word) not in {1,2} )) ]
                        cleanString1 = ' '.join(str(item).upper() for item in cleanString)
                        if cleanString1 !="":
                            tc = tc + 1
                            ors,uniqueWordList = sMixer.synonymExtracter(cleanString1,uniqueWordList)
                            counts = Counter(ors.split())
                            counterList.append(counts)
                            totalCount = totalCount + len(ors.split())
                            allentries.append(ors.encode('utf8'))
                            finalStringFile.append(ors.encode('utf8'))
                            #print(tc)
        return counterList,' '.join(uniqueWordList),totalCount,'\n'.join(finalStringFile),tc,'\n'.join(correctEntries)
        
#     def cleaning(self):
#         f = open('/home/hari/hari/DKE_Test/data/dfdfd.txt','r')
#         entries = f.readlines()
#         descFile = open("/home/hari/hari/DKE_Test/data/test1.csv","w")
#         stopset1 = StopWords()
#         stopset = stopset1.getStopWordList()
#         for x in entries:
#             f1 = str(x)
#             cleanString = (re.sub('[^a-zA-Z]', ' ', f1)).split()
#             cleanString  = [word for word in cleanString if ((word.upper() not in stopset)  & (len(word) not in {1,2} )) ]
#             cleanString1 = ' '.join(str(item).upper() for item in cleanString)
#             descFile.write(cleanString1.encode('utf8')+"\n")
#         descFile.close()