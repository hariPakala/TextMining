===================================

DKE Project Document

libraries used

numpy, scipy, pandas, lda, collections, nltk, re, 
json, csv, glob, os, xml.etree.ElementTree, math,
matplotlib, sklearn, multiprocessing, sys, time


Data Extraction

1) DataExtracter 
    This class is used for raw Data Extraction. Entries are extracted
    from the XML files present in the given folder.
    
    From each entry description part is only considered.
    
    From this Description all the special characters are
    removed and also the stop words (This is for Data Mining Purpose)
    
    We have do store the raw text from description entry for further processing.
    
2) datasetLoad
	This is class prepared exclusively for Latent Dirichlet Allocation Purpose (LDA).

3) StopWords
	This class contains a list of Stop Words, used stop word removal around 238 
	stop words are gathered.

Dimensionality Reduction

1) Ontology Reduction
	This class create a reduce list of unique words from the processed entries
	
2) Synonym Mixer
	Here every in the entry is queried againt wordnet ontology
	and simplest form of the word is returned.

3) SVD
	Singular Value Decomposition is performed in this class

Vector Space

1) Words2Vector    
	In this class a word to vector concept is implemented.

2) AttributeMatrixCreator
	A TFIDF matrix is created using this class

Clustering

1) KMeans
	K Means algorithm is implemented.
2) BKMeans
	Bisecting KMeans is implemented.
Both of the class are modified version of the one available on git hub.

Categorization

1) LDA
	LDA is implemented in this class.

Sentence Model

1) Statistik
	In this we attempt to create distribution of sentence lengths
	among all the entries (120000)
	Three sets are created bad1(< mean - Standard Deviation),
	bad2(> mean + Standard Deviation) and good (> mean - Standard Deviation 
	and < mean + Standard Deviation)
2) sentenceModelScoring
	Using the distribution created in the proir class.
	In every new entry sentence score is evaluated using the sentence model.

 Language Model
 
 1) POSTagger
 	 Around 100 good and 100 bad entries are randomly selected
 	 from the entire repository. 
 	 All the words in both of the classes tagged with 
 	 respective parts of speech.
 2) naiveBayesModel
 	 A bigram pos based naive bayes model is created.
 
 Evaluation
 
 1) naivesBayesClassifier
 	 New test entries are classified using this class,
 	 by the model created in the language model step
 
 2) sentenceScoring
 	 New test entries are classified based on the 
 	 sentence model created in the earlier step
 
 3) SilhoutteCoefficient
 	 K Means and Bisecting K Means are performed 
 	 here and the respective silhoutte coefficients are estimated.
 	 
 4) plotRegression
 		Graphs for all the evaluations are plotted usign this class