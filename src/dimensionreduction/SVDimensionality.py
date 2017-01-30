'''
Created on Sep 30, 2016

@author: hari
'''

from numpy import *
import operator
from os import listdir
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from numpy.linalg import *
from scipy.stats.stats import pearsonr
from numpy import linalg as la
import pandas as pd
class SVDimensionality(object):
    '''
    Singluar Value decomposition is performed
    SVD from numpy library is used.
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def performSVD(self,systemPath):    
        raw_data = loadtxt(systemPath+'data/wd/tfCount1234.csv',delimiter=',')
        #print raw_data       
        #normalize and remove mean
        data = mat(raw_data[:,:])
        #calculate SVD
        print "Hi"
        U, s, V = linalg.svd( data )
        print "Hi"
        
        dataframe = pd.DataFrame(data=U.astype(float))
        dataframe.to_csv(systemPath+'data/UMatrix1.csv', sep=',', header=False,  index=False)
        dataframe = pd.DataFrame(data=V.astype(float))
        dataframe.to_csv(systemPath+'data/VMatrix1.csv', sep=',', header=False,  index=False)
        