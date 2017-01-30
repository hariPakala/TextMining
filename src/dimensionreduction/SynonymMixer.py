'''
Created on Sep 28, 2016

@author: hari
'''
from nltk.corpus import wordnet as wn


class SynonymMixer:
    '''
    Here we try to reduce the dimensionality / the number of words in the corpus.
    Every word is queried against the wordnet, the results would be list of synonyms.
    This word would be replaced by either a noun, or the word which has least size.
    '''
    def __init__(self):
        '''
        Constructor
        '''
    def synonymExtracter(self, inputString, uniqueWordsList): 
        words = inputString.split()
        #print inputString
        newText = ""
        
        for wx in words:
            count = 0
            lw = len(wx)
            for x in (wn.synsets(wx)):
                count = count + 1
                #print x
                wrd = (x.name().split("."))[0]
                ps = (x.name().split("."))[1]
                lv = (x.name().split("."))[2]
                if lv == 0:
                    if  lw > len(wrd):
                        wx = wrd
            if count != 0:            
                uniqueWordsList.add(wx)
            newTe = " ".join((newText, wx.upper()))
            newText = newTe
        #print newText
        return newText,uniqueWordsList  



