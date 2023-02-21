import pandas as pd
import numpy as np

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

def generate_nd_normal_uncorrleated(number, mus, sigmas):
    data=np.array([np.random.normal(m,s,number) for m,s in zip(mus,sigmas)])
    return data.T

def generate_data_uncorrleated(numbers,mus,sigmas):
    data=[]
    for idx,mu in enumerate(mus):
        a=generate_nd_normal_uncorrleated(numbers[idx],mu,sigmas[idx])
        b=np.hstack((a,[[idx]]*len(a)))
        try:
            data=np.concatenate((data,b))
        except:
            data=b
    return data


def misclf_rate(y_true, y_pred):
    total_class1 = y_true.count(0)
    total_class2 = y_true.count(1)
    misclf_class1 = 0 
    misclf_class2 = 0
    
    tn, fp, fn, tp = confusion_matrix(y_true,y_pred).ravel()
    
    total_misclassification_rate = (fp+fn)/(tn+fp+fn+tp)
    
    for i in range(len(y_true)):
        if y_true[i] != y_pred[i]:
            if y_true[i] == 1:
                misclf_class1 += 1
            elif y_true[i] == 0:
                misclf_class2 += 1
                
    class1_misclf_rate = misclf_class1/total_class1
    class2_misclf_rate = misclf_class2/total_class2
                
    
    return class1_misclf_rate,class2_misclf_rate,total_misclassification_rate


def visualize(df, model):
    X1 = df.to_numpy()
    x, y = X1[:,:2],X1[:,-1]
    
    model.fit(x,y)
    
    x_min, x_max = x[:, 0].min() - 0.1, x[:,0].max() + 0.1
    y_min, y_max = x[:, 1].min() - 0.1, x[:, 1].max() + 0.1

    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))

    x_in = np.c_[xx.ravel(), yy.ravel()]
    y_pred = gnb.predict(x_in)
    y_pred = np.round(y_pred).reshape(xx.shape)
    
    plt.contourf(xx, yy, y_pred, cmap=plt.cm.RdYlBu, alpha=0.7 )
    plt.scatter(x[:,0], x[:, 1], c=y, s=40, cmap=plt.cm.RdYlBu)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.savefig('decision_boundary.png',dpi = 300)





















