'''
Created on Nov 7, 2016

@author: hari
'''
from __future__ import absolute_import, unicode_literals  # noqa

import os

import lda.utils
import numpy
from numpy import dtype

class datasetLoad_LDA:    
    
    def __init__(self):
        '''
        Constructor
        '''
        '''
            This is class prepared exclusively for Latent Dirichlet Allocation Purpose (LDA)
        '''
    
    '''
    Loading the data set
    '''
    def load_reuters1(self,systemPath):
            dtm = numpy.loadtxt(systemPath+"data/wd/tfCount1234.csv", dtype = int, delimiter = ",")
            print(dtm)
            return dtm
    
    '''
    Loading all the uniqueWords
    '''
    
    def load_reuters_vocab1(self,systemPath):
            _test_dir = os.path.join(os.path.dirname(__file__), 'tests')
            reuters_vocab_fn = os.path.join(systemPath+"data/Word/", 'finalUniqueWordList.csv')
            with open(reuters_vocab_fn) as f:
                vocab = tuple(f.read().split())
            return vocab
    
    '''
    Loading all the titles
    '''
    
    def load_reuters_titles1(self,systemPath):
            _test_dir = os.path.join(os.path.dirname(__file__), 'tests')
            reuters_titles_fn = os.path.join(systemPath+"data/wd/", 'xml20.csv')
            with open(reuters_titles_fn) as f:
                titles = tuple(line.strip() for line in f.readlines())
            return titles