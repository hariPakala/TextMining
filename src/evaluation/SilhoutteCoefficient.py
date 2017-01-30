
from __future__ import print_function

from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from sklearn.datasets import load_digits
from sklearn.preprocessing import scale
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster.spectral import SpectralClustering
from clustering.BisectKmeans import BisectKMeans
from clustering.Kmeans import KMeans


df = pandas.read_table('/home/hari/hari/DKE_Test/data/UMatrix1.csv', sep=',', lineterminator='\n', header=None)
X1 = df.iloc[:,:].values

import time

print("Data Loaded")

'''''''''''''''''''''''''''
#KMeans

'''''''''''''''''''''''''''

silhouette_KMeans = []
silhouette_BKMeans = []
#        print("KMeans")

cluster_n = [5]
start_time = time.time()
for n_cluster in cluster_n:
    clustererk = KMeans(n_clusters=n_cluster)
    print("Clustering Started")
    cluster_labelsk = clustererk.fit_predict(df.iloc[:,:].values)
    
    silhouette_avg_k = silhouette_score(X1, cluster_labelsk)
    silhouette_KMeans.append(silhouette_avg_k)
    labelKM = open("/home/hari/hari/DKE_Test/data/wd/clusterlabel/label_"+str(n_cluster)+"_kMeans.csv","w")
    labelsff = ""
    print("--- %s seconds ---" % (time.time() - start_time))
    for label in cluster_labelsk:
        #print(label)
        labelsff =labelsff + str(label) + "\n"
    print("Silhoutte Coeffecient for k = " + str(n_cluster) +"is = " + str(silhouette_avg_k))
    labelKM.write(labelsff)
    labelKM.close()
    print("Clustering Finished")

'''''''''''''''''''''''''''
#Bisecting KMeans

'''''''''''''''''''''''''''
start_time1 = time.time()
print("Bisecting KMeans")

for n_cluster in cluster_n:
    clustererk = BisectKMeans(n_clusters=n_cluster)
    print("Clustering Started")
    cluster_labelsk = clustererk.fit_predict(df.iloc[:,:].values)
    print("Clustering Finished")
    silhouette_avg_k = silhouette_score(X1, cluster_labelsk)
    silhouette_BKMeans.append(silhouette_avg_k)
    labelBKF = open("/home/hari/hari/DKE_Test/data/wd/clusterlabel/label_"+str(n_cluster)+"_BkMeans.csv","w")
    labelsbk = ""
    print("--- %s seconds ---" % (time.time() - start_time1))
    for label in cluster_labelsk:
        #print(label)
        labelsbk =labelsbk + str(label) + "\n"
    print("Silhoutte Coeffecient BKMeans for k = " +str(n_cluster) +"is = " + str(silhouette_avg_k))
    labelBKF.write(labelsbk)
    labelBKF.close()

