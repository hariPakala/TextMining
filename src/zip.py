
'''
Created on Nov 26, 2016

@author: hari
'''


from __future__ import division
from itertools import *
from pylab import *
from nltk.corpus import brown
from string import lower
from collections import Counter
import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

corpusdir = '/home/hari/hari/DKE_Test/TTE' # Directory of corpus.

newcorpus = PlaintextCorpusReader(corpusdir, '.*')

# The data: token counts from the Brown corpus
tokens_with_count = Counter(imap(lower, newcorpus.words()))
counts = array(tokens_with_count.values())
tokens = tokens_with_count.keys()

# A Zipf plot
ranks = arange(1, len(counts)+1)
indices = argsort(-counts)
frequencies = counts[indices]
loglog(ranks, frequencies, marker=".")
title("Zipf plot for Brown corpus tokens")
xlabel("Frequency rank of token")
ylabel("Absolute frequency of token")
grid(True)
for n in list(logspace(-0.5, log10(len(counts)), 30).astype(int)):
    dummy = text(ranks[n], frequencies[n], " " + tokens[indices[n]], 
                 verticalalignment="bottom",
                 horizontalalignment="left")

show()
