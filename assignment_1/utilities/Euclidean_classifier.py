import numpy as np
import pandas as pd

class euclidean_2d_classifier:
    def __init__(self):
        center1=[np.random.uniform(0,1),np.random.uniform(0,1)]
        center2=[np.random.uniform(0,1),np.random.uniform(0,1)]
        pass
    def train(self,xes,y):
        cluster1=np.array([xes[i] for i in range(len(xes)) if y[i]==0])
        cluster2=np.array([xes[i] for i in range(len(xes)) if y[i]==1])
        self.center1=[np.mean(ax) for ax in cluster1.T]
        self.center2=[np.mean(ax) for ax in cluster2.T]
    def predict(self,X):
        dist1=np.sum(np.array([(X[i]-self.center1[i])**2 for i in range(len(self.center1))]))
        dist2=np.sum(np.array([(X[i]-self.center2[i])**2 for i in range(len(self.center2))]))
        if dist1>dist2:
            return 1
        else:
            return 0
        
# classifier=euclidean_2d_classifier()
# classifier.train(xes,y)
# print(classifier.center1,classifier.center2)
# classifier.predict([4,6.5])