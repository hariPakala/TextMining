'''
Created on Nov 15, 2016

@author: hari
'''
from __future__ import division
import math
import re
class setenceModelScoring(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def getsenCalc(self,sentend,sentenceLen,std,mean):
        t1 = 1 / (math.sqrt(2*3.14*std))
        s1 = math.pow((sentenceLen - mean),2)
        s12 = 2*std*std
        x = s1 / s12
        e1 = math.exp(-x)
        h = t1*e1
        test = math.log10(h)
        return test
    
    def getSentenceScore(self, rawString):
        sentenceStd = [5.93,2.6,10.49]
        sentenceMean = [20.87,6.36,42.41]
        sentences = rawString.split('.')
        count = 0
        goodSentenceScore = 0
        badSentenceScore1 = 0
        badSentenceScore2 = 0
        for sentend1 in sentences:
            sentend = (re.sub('[^a-zA-Z]', ' ', sentend1))
            sentenceLen = len(sentend.split())
            if sentenceLen != 0 :
                if sentenceLen < 40:
                    x = self.getsenCalc(sentend,sentenceLen,sentenceStd[0],sentenceMean[0])
                    y = self.getsenCalc(sentend,sentenceLen,sentenceStd[1],sentenceMean[1])
                    z = self.getsenCalc(sentend,sentenceLen,sentenceStd[2],sentenceMean[2])
                    if count == 1:  
                        if x > goodSentenceScore: goodSentenceScore = x
                        if y > badSentenceScore1: badSentenceScore1 = y
                        if z > badSentenceScore2: badSentenceScore2 = z
                    else :
                        goodSentenceScore = x
                        badSentenceScore1 = y
                        badSentenceScore2 = z
                    count = 1
                else:
                    return 0,0,40    
        return goodSentenceScore,badSentenceScore1,badSentenceScore2 