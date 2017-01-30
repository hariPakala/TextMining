'''
Created on Nov 6, 2016

@author: hari
'''
import numpy as np
import lda
import lda.datasets
import os


from dataextraction.datasetLoad_LDA import datasetLoad_LDA

class LDA1(object):
    '''
    Class for LDA implementation
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def makeLDA(self):
        
        systemPath = (os.getcwd()[:-3]) 
        ld2 = datasetLoad_LDA()
        
        X = ld2.load_reuters1(systemPath)
        vocab = ld2.load_reuters_vocab1(systemPath)
        titles = ld2.load_reuters_titles1(systemPath)
            
        X.shape
        (395, 4258)
        model = lda.LDA(n_topics=5, n_iter=500, random_state=1)
        model.fit(X)
        topic_word = model.topic_word_  # model.components_ also works
        n_top_words = 250
        i = 0
        for nd in model.nz_:
            i = i +1
            print(nd)
        print(i)
        for i, topic_dist in enumerate(topic_word):
            topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
            print('Topic {}: {}'.format(i, ' '.join(topic_words)))
            
        doc_topic = model.doc_topic_
        print("type(doc_topic): {}".format(type(doc_topic)))
        print("shape: {}".format(doc_topic.shape))
        
        ldaLabels = ""

        for n in range(4400):
            topic_most_pr = doc_topic[n].argmax()
            ldaLabels = ldaLabels + str(topic_most_pr) + "\n"
            print("doc: {} topic: {}\n{}...".format(n,
                                            topic_most_pr,
                                            titles[n][:50]))
        ldaLabelsFile = open(systemPath+"data/wd/DataSetLabels/ldaLables.csv","w")
        ldaLabelsFile.write(ldaLabels)
        ldaLabelsFile.close()