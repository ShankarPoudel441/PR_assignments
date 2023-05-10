import numpy as np
import pandas as pd
import math

from numpy.linalg import inv

class twoD_gaussian:
    def __init__(self):
        self.mu=[np.random.uniform(0,1),np.random.uniform(0,1)]
        self.sigma=[[1,0],[0,1]]

    def fit_mu_sigma(self,mu,sigma):
        self.mu=np.array(mu)
        self.sigma=np.array(sigma)
    
    def calculate_gaussian_prob(self,x):
        dimension=len(x)
        if dimension == len(self.mu) and (dimension,dimension)== self.sigma.shape:
            deter=np.linalg.det(self.sigma)
            if deter==0:
                raise NameError("The covariance matrix can't be singular")
            inver=np.linalg.inv(self.sigma)
            const=1/((2*math.pi)**(float(dimension)/2)*deter**0.5)
            exponent=-1/2*np.matmul(np.matmul((x-self.mu).T,inver),(x-self.mu))
            return const*math.exp(exponent)
        else:
            raise NameError("The dimension of input doesnot match")

    def find_mean_and_covariance(self,data):
        data=np.array(data)
        mean = np.average(data , axis=0)
        sigma = 0
        for entry in data:
            sigma += np.dot((entry-mean).reshape(len(entry), 1), (entry-mean).reshape(1, len(entry)))
        if len(d)<30:
            sigma /= (len(d)-1)
        else:
            sigma /= len(d)
        return np.array(mean),np.array(sigma)


    def fit(self,data):
        mean,sigma = find_mean_and_covariance(data)
        fit_mu_sigma(mean,sigma)


x = np.array([0,0])
mu  = np.array([0,0])
cov = np.array([[1,0],[0,1]])
model=twoD_gaussian()
model.fit_mu_sigma()
model