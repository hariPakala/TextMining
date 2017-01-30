'''
Created on Nov 5, 2016

@author: hari
'''
import matplotlib.patches as mpatches
import numpy as np
import matplotlib.pyplot as plt


def python1PerformPlot():
    x = [962,1947,2929,3914,4889,5861,6830,7506,8477,9454,10433,11416,12401] 
    y = [103.77,164.58,221.89,240.00,243.35,235.09,235.51,236.03,227.32,240.43,238.85,230.53,224.61]
    
    
    # fit_fn is now a function which takes in x and returns an estimate for y
    fig, ax = plt.subplots()
    fit = np.polyfit(x,y,1)
    fit_fn = np.poly1d(fit) 
    ax.plot(x,y, 'ro', x, fit_fn(x), color='red')
    ax.scatter(x, y)
    
    ax.set_xlabel('Total number of Entries')
    ax.set_ylabel('Number of Entries processed per second ')
    #plt.title("An average of 953,92 Records per each Fragment and one Thread for each Fragment")
    ax.text(5000, 120, 'An average of 953,92 Records\n per each  Fragment \n and one Thread for each Fragment', style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    ax.annotate('Peak Performance at 5 Fragments, \n at one Thread for each Fragment', xy=(4889,243.35), xytext=(3000,175),
            arrowprops=dict(facecolor='black', shrink=0.001),
            )
    plt.title('Performance analysis in Python')
    y_mean = [np.mean(y) for i in x]
    mean_line = ax.plot(x,y_mean, label='Mean', linestyle='--')
    fig.show()
    plt.show()



def python2PerformPlot():
    x = [5368,10736,21472,24640,32208,42944,53680] 
    y = [142.16,219.23,343.88,372.77,398.76,391.03,371.77]
    
    
    # fit_fn is now a function which takes in x and returns an estimate for y
    fig, ax = plt.subplots()
    fit = np.polyfit(x,y,5)
    fit_fn = np.poly1d(fit) 
    ax.plot(x,y, 'ro', x, fit_fn(x), color='red')
    ax.scatter(x, y)
    
    ax.set_xlabel('Total number of Entries in all the 11 Fragments')
    ax.set_ylabel('Number of Entries processed per second ')
    #plt.title("An average of 953,92 Records per each Fragment and one Thread for each Fragment")
    #ax.text(17000, 120, 'An average of 953,92 Records\n per each  Fragment \n and one Thread for each Fragment', style='italic',
     #   bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    ax.annotate('Peak Performance at 2928 Entries per Fragment, \n at one Thread for each of 11 Fragments', xy=(32208,398.76), xytext=(17000,250),
            arrowprops=dict(facecolor='black', shrink=0.001),
            )
    plt.title('Performance analysis in Python 2')
    y_mean = [np.mean(y) for i in x]
    mean_line = ax.plot(x,y_mean, label='Mean', linestyle='--')
    fig.show()
    plt.show()


#python2PerformPlot()


def ClusteringPerformancePlot1():
    x = [498,981,1473,1966,2457,3433,3913,4400]
    y = [4.8847849369,11.505874157,28.3299460411,37.8939170837,50.2645189762,69.1701610088,83.3787078857,115.727949142]
    y1 =[2.87973809242,6.08334112167,24.225924015,24.3887488842,32.2741391659,62.0001311302,61.8257069588,86.0516450405]        
    # fit_fn is now a function which takes in x and returns an estimate for y
    fig, ax = plt.subplots()
    fit = np.polyfit(x,y,8)
    fit_fn = np.poly1d(fit) 
    ax.plot( x, fit_fn(x), color='red', label = "K Means")
    ax.scatter(x, y, color = 'red')
    
    fit = np.polyfit(x,y1,8)
    fit_fn = np.poly1d(fit) 
    ax.plot(x, fit_fn(x), color='blue', label = "Bisecting K Means")
    ax.scatter(x, y1, color = 'blue')
    
    
    ax.set_xlabel('Number of Entries invloved in Clustering')
    ax.set_ylabel('Time in Seconds')
    #plt.title("An average of 953,92 Records per each Fragment and one Thread for each Fragment")
    ax.text(2700, 10, 'Vector Space for Clustering \n is created using \n TFIDF Weighing Score', style='italic',
      bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    #ax.annotate('Peak Performance at 5 Fragments, \n at one Thread for each Fragment', xy=(4889,243.35), xytext=(3000,175),
     #       arrowprops=dict(facecolor='black', shrink=0.001),
      #      )
    plt.title('Performance analysis of Clustering Algorithms')
    plt.legend(bbox_to_anchor=(0.55, 0.9), loc=1, borderaxespad=0.)
    fig.show()
    plt.show()

def ClusteringPerformancePlot2():
    x = [498,981,1473,1966,2457,3433,3913,4400]
    y = [4.81576299667,11.5385780334,11.5385780334,34.5306921005,49.0629148483,71.9618589878,85.6255021095,105.16543293]
    y1 =[3.15663385391,5.7970559597,5.7970559597,23.5135498047,41.2791769505,37.3306250572,44.3177471161,84.9565758705]        
    # fit_fn is now a function which takes in x and returns an estimate for y
    fig, ax = plt.subplots()
    fit = np.polyfit(x,y,8)
    fit_fn = np.poly1d(fit) 
    ax.plot( x, fit_fn(x), color='red', label = "K Means")
    ax.scatter(x, y, color = 'red')
    
    fit = np.polyfit(x,y1,8)
    fit_fn = np.poly1d(fit) 
    ax.plot(x, fit_fn(x), color='blue', label = "Bisecting K Means")
    ax.scatter(x, y1, color = 'blue')
    
    
    ax.set_xlabel('Number of Entries invloved in Clustering')
    ax.set_ylabel('Time in Seconds')
    #plt.title("An average of 953,92 Records per each Fragment and one Thread for each Fragment")
    ax.text(2700, 10, 'Vector Space for Clustering \n is created using \n TF Weighing Score', style='italic',
      bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    #ax.annotate('Peak Performance at 5 Fragments, \n at one Thread for each Fragment', xy=(4889,243.35), xytext=(3000,175),
     #       arrowprops=dict(facecolor='black', shrink=0.001),
      #      )
    plt.title('Performance analysis of Clustering Algorithms')
    plt.legend(bbox_to_anchor=(0.55, 0.9), loc=1, borderaxespad=0.)
    fig.show()
    plt.show()

def ClusteringPerformancePlot3():
    x = [498,981,1473,1966,2457,3433,3913,4400]
    y = [0.289753913879,0.736919164658,1.60685992241,2.84462094307,2.84462094307,8.72462511063,11.8668959141,11.8668959141]
    y1 =[0.544680118561,1.39919805527,3.24374008179,6.10799789429,10.6029200554,18.285836935,23.977533102,23.977533102]        
    # fit_fn is now a function which takes in x and returns an estimate for y
    fig, ax = plt.subplots()
    fit = np.polyfit(x,y,8)
    fit_fn = np.poly1d(fit) 
    ax.plot( x, fit_fn(x), color='red', label = "K Means")
    ax.scatter(x, y, color = 'red')
    
    fit = np.polyfit(x,y1,8)
    fit_fn = np.poly1d(fit) 
    ax.plot(x, fit_fn(x), color='blue', label = "Bisecting K Means")
    ax.scatter(x, y1, color = 'blue')
    
    
    ax.set_xlabel('Number of Entries invloved in Clustering')
    ax.set_ylabel('Time in Seconds')
    #plt.title("An average of 953,92 Records per each Fragment and one Thread for each Fragment")
    ax.text(700, 18, 'Vector Space for Clustering \n is created using \n TFIDF Weighing Score after SVD', style='italic',
      bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    #ax.annotate('Peak Performance at 5 Fragments, \n at one Thread for each Fragment', xy=(4889,243.35), xytext=(3000,175),
     #       arrowprops=dict(facecolor='black', shrink=0.001),
      #      )
    plt.title('Performance analysis of Clustering Algorithms')
    plt.legend(bbox_to_anchor=(0.98, 0.2), loc=1, borderaxespad=0.)
    fig.show()
    plt.show()


def sentenceLengthPlot():
    x = [19,18,20,17,16,21,22,15,23,14,24,25,13,26,12,27,3,28,11,29,30,10,31,32,9,4,33,8,34,35,6,7,36,5,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,69,71,72,73,74,76,75,77,78,79,82,86,84,83,80,81,85,88,94,87,92,89,90,95,91,97,93,96,98,99,101,100,103,108,109,102,105,104,123,106,107,117,111,114,113,126,110,116,120,122,140,115,118,121,125,129,132,137,130,138,112,119,127,133,135]
    y = [30205,30188,29804,29720,29033,28776,27423,27373,26210,25607,24775,23253,23063,21463,20476,19919,19098,17990,17297,16407,14824,14249,13289,12204,11728,11290,10705,9447,9419,8661,7960,7570,7506,7204,6717,5852,5169,4415,3945,3423,3039,2724,2297,2131,1834,1605,1490,1267,1120,962,856,752,691,616,533,507,440,380,344,341,311,244,233,227,192,174,165,155,138,137,120,116,115,107,99,90,81,81,56,54,53,50,49,44,44,44,43,42,39,34,34,31,29,28,27,27,26,23,18,18,18,18,17,17,14,14,13,13,12,11,11,10,10,9,9,8,8,8,7,7,7,7,7,7,7,6,6,5,5,5,5,5]
    #x = [19,18,20,17,16,21,22,15,23,14,24,25,13,26,12,27,3,28,11,29,30,10,31,32,9,4,33,8,34,35,6,7,36,5,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,69,71,72,73,74,76,75,77,78,79,82,86,84,83,80,81,85,88,94,87,92,89,90,95,91,97,93,96,98,99,101,100,103,108,109,102,105,104,123,106,107,117,111,114,113,126,110,116,120,122,140,115,118,121,125,129,132,137,130,138,112,119,127,133,135,124,131,136,146,148,151,152,128,134,139,141,142,149,153,161,163,178,180,182,216,144,145,150,156,158,159,165,170,173,175,181,186,187,189,204,205,213,270,154,162,164,166,168,171,172,174,176,177,179,185,188,191,195,197,201,206,212,217,220,228,231,232,233,236,242,245,248,249,256,258,260,269,273,275,286,293,301,315,317,320,352,1411,426,437]
    #y = [30205,30188,29804,29720,29033,28776,27423,27373,26210,25607,24775,23253,23063,21463,20476,19919,19098,17990,17297,16407,14824,14249,13289,12204,11728,11290,10705,9447,9419,8661,7960,7570,7506,7204,6717,5852,5169,4415,3945,3423,3039,2724,2297,2131,1834,1605,1490,1267,1120,962,856,752,691,616,533,507,440,380,344,341,311,244,233,227,192,174,165,155,138,137,120,116,115,107,99,90,81,81,56,54,53,50,49,44,44,44,43,42,39,34,34,31,29,28,27,27,26,23,18,18,18,18,17,17,14,14,13,13,12,11,11,10,10,9,9,8,8,8,7,7,7,7,7,7,7,6,6,5,5,5,5,5,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] 
    # fit_fn is now a function which takes in x and returns an estimate for y
    fig, ax = plt.subplots()
    fit = np.polyfit(x,y,1)
    fit_fn = np.poly1d(fit) 
    #ax.plot( x, fit_fn(x), color='red', label = "Sentence Length")
    ax.scatter(x, y, color = 'red')
    
    
    ax.set_xlabel('Sentence Length')
    ax.set_ylabel('Number of Sentences')
    #plt.title("An average of 953,92 Records per each Fragment and one Thread for each Fragment")
   # ax.text(700, 18, 'Vector Space for Clustering \n is created using \n TFIDF Weighing Score after SVD', style='italic',
    #  bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    #ax.annotate('Mean Sentence Length 21.629', xy=(21.629,30205), xytext=(50,15000),
           # arrowprops=dict(facecolor='black', shrink=0.001),
           # )
    plt.plot([10.56,10.56],[0,31010.56], 'k-', lw=2)
    plt.plot([32.7,32.7],[0,31032.7], 'k-')
    #plt.plot([33,1, 30033,1],[0,0], 'k-', lw=2)
    plt.plot([21.63,21.63],[0,31021.63], 'k-', lw=2)
    plt.title('Plotting Sentence Length Versus Number of Sentences')
    plt.legend(bbox_to_anchor=(0.98, 0.2), loc=1, borderaxespad=0.)
    fig.show()
    plt.show()

from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def plotsilhoutte():
    fig, (ax1) = plt.subplots()
    fig.set_size_inches(7,6)
    ax1.axvline(x=-0.071955107, color="red", linestyle="--")
    ax1.axvline(x=0, color="black", linestyle="-")
    ax1.set_xlim([-0.5, 0.5])

    ax1.set_yticks([])  # Clear the yaxis labels / ticks
   

    ax1.set_title("The silhouette plot for various clusters using Kmeans"+ 
    "\n Vector space using TF-IDF Weighing")
    ax1.set_xlabel("The silhouette coefficient values")
    ax1.set_ylabel("Cluster label")

    color = cm.spectral(10)
    ax1.fill_betweenx(np.arange(1, 10), -0.0195800123247,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 5 ,str('3 Clusters'))
    ax1.text(-0.3, 5 ,str('-0.0195800123247'))
    color = cm.spectral(200)
    ax1.fill_betweenx(np.arange(10, 20),-0.053779611944,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 15 ,str('5 Clusters'))
    ax1.text(-0.3, 15 ,str('-0.053779611944'))
    color = cm.spectral(30)
    ax1.fill_betweenx(np.arange(20, 30),-0.0838937743842,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 25 ,str('7 CLusters'))
    ax1.text(-0.3, 25 ,str('-0.0838937743842'))
    color = cm.spectral(400)
    ax1.fill_betweenx(np.arange(30, 40),-0.346432352873,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 35 ,str('9 CLusters'))
    ax1.text(-0.3, 35 ,str('-0.346432352873'))
    '''color = cm.spectral(4)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.0736025205365,facecolor=color, 
                      edgecolor=color, alpha=0.7)
    color = cm.spectral(5)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.364788899547,facecolor=color, 
                      edgecolor=color, alpha=0.7)
    color = cm.spectral(6)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.373854095606,facecolor=color, 
                      edgecolor=color, alpha=0.7)
      color = cm.spectral(7)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.224075723598,facecolor=color, 
                      edgecolor=color, alpha=0.7) '''
    plt.show()
def plotsilhoutte1():
    fig, (ax1) = plt.subplots()
    fig.set_size_inches(7,6)
    ax1.axvline(x=-0.25908031, color="red", linestyle="--")
    ax1.axvline(x=0, color="black", linestyle="-")
    ax1.set_xlim([-0.5, 0.5])

    ax1.set_yticks([])  # Clear the yaxis labels / ticks
   

    ax1.set_title("The silhouette plot for the various clusters using Bisecting Kmeans"+ 
    "\n Vector space using TF-IDF Weighing")
    ax1.set_xlabel("The silhouette coefficient values")
    ax1.set_ylabel("Cluster label")

    color = cm.spectral(10)
    ax1.fill_betweenx(np.arange(1, 10), -0.0736025205365,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 5 ,str('3 Clusters'))
    ax1.text(-0.3, 5 ,str('-0.0736025205365'))
    color = cm.spectral(200)
    ax1.fill_betweenx(np.arange(10, 20),-0.364788899547,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 15 ,str('5 Clusters'))
    ax1.text(-0.3, 15 ,str('-0.364788899547'))
    color = cm.spectral(30)
    ax1.fill_betweenx(np.arange(20, 30),-0.373854095606,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 25 ,str('7 CLusters'))
    ax1.text(-0.3, 25 ,str('-0.373854095606'))
    color = cm.spectral(400)
    ax1.fill_betweenx(np.arange(30, 40),-0.224075723598,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 35 ,str('9 CLusters'))
    ax1.text(-0.3, 35 ,str('-0.224075723598'))
    '''color = cm.spectral(4)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.0736025205365,facecolor=color, 
                      edgecolor=color, alpha=0.7)
    color = cm.spectral(5)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.364788899547,facecolor=color, 
                      edgecolor=color, alpha=0.7)
    color = cm.spectral(6)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.373854095606,facecolor=color, 
                      edgecolor=color, alpha=0.7)
      color = cm.spectral(7)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.224075723598,facecolor=color, 
                      edgecolor=color, alpha=0.7) '''
    plt.show()

def plotsilhoutte2():
    fig, (ax1) = plt.subplots()
    fig.set_size_inches(7,6)
    ax1.axvline(x=-0.111670438, color="red", linestyle="--")
    ax1.axvline(x=0, color="black", linestyle="-")
    ax1.set_xlim([-0.5, 0.5])

    ax1.set_yticks([])  # Clear the yaxis labels / ticks
   

    ax1.set_title("The silhouette plot for the various clusters.")
    ax1.set_xlabel("The silhouette coefficient values")
    ax1.set_ylabel("Cluster label")

    color = cm.spectral(10)
    ax1.fill_betweenx(np.arange(1, 10), -0.00215706055144,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 5 ,str('3 Clusters'))
    ax1.text(-0.3, 5 ,str('-0.00215706055144'))
    color = cm.spectral(200)
    ax1.fill_betweenx(np.arange(10, 20),-0.0208730905983,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 15 ,str('5 Clusters'))
    ax1.text(-0.3, 15 ,str('-0.0208730905983'))
    color = cm.spectral(30)
    ax1.fill_betweenx(np.arange(20, 30),-0.333474448624,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 25 ,str('7 CLusters'))
    ax1.text(-0.3, 25 ,str('-0.333474448624'))
    color = cm.spectral(400)
    ax1.fill_betweenx(np.arange(30, 40),-0.0901771502548,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 35 ,str('9 CLusters'))
    ax1.text(-0.3, 35 ,str('-0.0901771502548'))
    '''color = cm.spectral(4)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.0736025205365,facecolor=color, 
                      edgecolor=color, alpha=0.7)
    color = cm.spectral(5)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.364788899547,facecolor=color, 
                      edgecolor=color, alpha=0.7)
    color = cm.spectral(6)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.373854095606,facecolor=color, 
                      edgecolor=color, alpha=0.7)
      color = cm.spectral(7)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.224075723598,facecolor=color, 
                      edgecolor=color, alpha=0.7) '''
    plt.show()

def plotsilhoutte3():
    fig, (ax1) = plt.subplots()
    fig.set_size_inches(7,6)
    ax1.axvline(x=-0.230711355, color="red", linestyle="--")
    ax1.axvline(x=0, color="black", linestyle="-")
    ax1.set_xlim([-0.5, 0.5])

    ax1.set_yticks([])  # Clear the yaxis labels / ticks
   

    ax1.set_title("The silhouette plot for the various clusters.")
    ax1.set_xlabel("The silhouette coefficient values")
    ax1.set_ylabel("Cluster label")

    color = cm.spectral(10)
    ax1.fill_betweenx(np.arange(1, 10),-0.0350654536167,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 5 ,str('3 Clusters'))
    ax1.text(-0.3, 5 ,str('-0.0350654536167'))
    color = cm.spectral(200)
    ax1.fill_betweenx(np.arange(10, 20),-0.16705666335,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 15 ,str('5 Clusters'))
    ax1.text(-0.3, 15 ,str('-0.16705666335'))
    color = cm.spectral(30)
    ax1.fill_betweenx(np.arange(20, 30),-0.360360820592,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 25 ,str('7 CLusters'))
    ax1.text(-0.3, 25 ,str('-0.360360820592'))
    color = cm.spectral(400)
    ax1.fill_betweenx(np.arange(30, 40),-0.360362484042,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 35 ,str('9 CLusters'))
    ax1.text(-0.3, 35 ,str('-0.360362484042'))
    '''color = cm.spectral(4)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.0736025205365,facecolor=color, 
                      edgecolor=color, alpha=0.7)
    color = cm.spectral(5)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.364788899547,facecolor=color, 
                      edgecolor=color, alpha=0.7)
    color = cm.spectral(6)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.373854095606,facecolor=color, 
                      edgecolor=color, alpha=0.7)
      color = cm.spectral(7)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.224075723598,facecolor=color, 
                      edgecolor=color, alpha=0.7) '''
    plt.show()
def plotsilhoutte4():
    fig, (ax1) = plt.subplots()
    fig.set_size_inches(7,6)
    ax1.axvline(x=-0.230711355, color="red", linestyle="--")
    ax1.axvline(x=0, color="black", linestyle="-")
    ax1.set_xlim([-0.3, 0.3])

    ax1.set_yticks([])  # Clear the yaxis labels / ticks
   

    ax1.set_title("The silhouette plot for the various clusters, \n for vector space using TF-IDF Weighing")
    ax1.set_xlabel("The silhouette coefficient values")
    ax1.set_ylabel("Cluster label")

    color = cm.spectral(10)
    ax1.fill_betweenx(np.arange(1, 10),-7.34934511828e-15,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 5 ,str('3 Clusters'))
    ax1.text(-0.3, 5 ,str('-7.34934511828e-15'))
    color = cm.spectral(200)
    ax1.fill_betweenx(np.arange(10, 20),-7.22274541034e-15,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 15 ,str('5 Clusters'))
    ax1.text(-0.3, 15 ,str('-7.22274541034e-15'))
    color = cm.spectral(30)
    ax1.fill_betweenx(np.arange(20, 30),-0.360360820592,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 25 ,str('7 CLusters'))
    ax1.text(-0.3, 25 ,str('-0.360360820592'))
    color = cm.spectral(400)
    ax1.fill_betweenx(np.arange(30, 40),-0.360362484042,0,facecolor=color, 
                      edgecolor=color)
    ax1.text(0.01, 35 ,str('9 CLusters'))
    ax1.text(-0.3, 35 ,str('-0.360362484042'))
    '''color = cm.spectral(4)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.0736025205365,facecolor=color, 
                      edgecolor=color, alpha=0.7)
    color = cm.spectral(5)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.364788899547,facecolor=color, 
                      edgecolor=color, alpha=0.7)
    color = cm.spectral(6)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.373854095606,facecolor=color, 
                      edgecolor=color, alpha=0.7)
      color = cm.spectral(7)
    ax1.fill_betweenx(np.arange(y_lower, y_upper),0, -0.224075723598,facecolor=color, 
                      edgecolor=color, alpha=0.7) '''
    plt.show()
    #ClusteringPerformancePlot1()
#ClusteringPerformancePlot2()
#sentenceLengthPlot()
plotsilhoutte2()