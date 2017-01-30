'''
Created on Nov 16, 2016

@author: hari
'''
import nltk 
from nltk.tokenize import word_tokenize
import re
from evaluation.naiveBayesClassifier import naiveBayesClassifier
from SentenceModel.setenceModelScoring import setenceModelScoring
class sentenceScoring(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def sentenceScore(self,systemPath):
        
        nbC = naiveBayesClassifier()
        smc = setenceModelScoring()
                
        checkEntriesfile = open(systemPath+"data/Word/xml20CorrectEntries_4400.txt","r")
        naiveClassEntriesfile = open(systemPath+"data/Word/naiveClass_4400.txt","w")
        setenceEntriesfile = open(systemPath+"data/Word/sentenceClass_4400.txt","w")
        naiveSetenceEntriesfile = open(systemPath+"data/Word/naiveSenetence_4400.txt","w")
        finalScorefile = open(systemPath+"data/Word/finalScore_4400.txt","w")
        allEntries = checkEntriesfile.readlines()
        i = 0
        naiveClass = []
        sentenceClass = []
        naiveSentenceClass = []
        finalScores = []
        for entry in allEntries:
            pSpeech = []
            cleanString = (re.sub('#', "ff", entry))
            cleanString1 = (re.sub('[^a-zA-Z]', ' ', cleanString))
            
            textTest = word_tokenize(cleanString1)
            pss = nltk.pos_tag(textTest)
            for ps in pss:
                ci = 0
                for s in ps:
                    if ci == 1:
                        pSpeech.append(s)
                    ci = ci + 1
            i = i +1
            bigram = nltk.bigrams(pSpeech)
            bigramList = []
            for bg in bigram:
                bgL = bg[0]+":"+bg[1]
                bigramList.append(bgL)
            goodProbability,badProbability = nbC.getProbabilties(bigramList,systemPath)
            goodSentenceScore,badSentenceScore1,badSentenceScore2 = smc.getSentenceScore(cleanString)
            #print(goodSentenceScore,badSentenceScore1,badSentenceScore2)
            x = badSentenceScore1 if badSentenceScore1 > badSentenceScore2 else badSentenceScore2
            naiveClass.append("Good" if goodProbability > badProbability else "Bad")
            sentenceClass.append("Good" if goodSentenceScore > x else "Bad")
            goodnaiveSetenceScore = 0.91 * goodProbability + 0.09 * goodSentenceScore
            baddnaiveSetenceScore = 0.91 * badProbability + 0.09 * x  
            naiveSentenceClass.append("Good" if goodnaiveSetenceScore > baddnaiveSetenceScore else "Bad")
            finalScores.append(str(goodnaiveSetenceScore) if goodnaiveSetenceScore > baddnaiveSetenceScore else str(baddnaiveSetenceScore))
            #print(goodSentenceScore,",",x,",",goodProbability,",",badProbability,",",goodnaiveSetenceScore,",",baddnaiveSetenceScore)
            print()
        naiveClassEntriesfile.write('\n'.join(naiveClass))
        setenceEntriesfile.write('\n'.join(sentenceClass))
        naiveSetenceEntriesfile.write('\n'.join(naiveSentenceClass))
        finalScorefile.write('\n'.join(finalScores))
        
        naiveClassEntriesfile.close()
        setenceEntriesfile.close()
        naiveSetenceEntriesfile.close()
        finalScorefile.close()