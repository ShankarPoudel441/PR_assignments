import numpy as np

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
