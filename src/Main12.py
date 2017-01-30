
import os

systemPath = (os.getcwd()[:-3]) 


from SentenceModel.StatistiK import StatistiK
sm = StatistiK()
sm.sentenceLen(systemPath)

from languagemodel.POSTagger import POSTagger
pst = POSTagger()
pst.posTag("GoodEntrys",systemPath)
pst.posTag("BadEntries",systemPath)

from languagemodel.naiveBayesModel import naiveBayesModel

nbc = naiveBayesModel()
nbc.createProbabilities(systemPath)

from evaluation.sentenceScoring import sentenceScoring

smS = sentenceScoring()
smS.sentenceScore(systemPath)
