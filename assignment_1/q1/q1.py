import numpy as np

# Here, covariance of both the classes is same so it is the first case and thus the decision boundry is straight line:
# w.T(x-x0)=0 and w and x0 are calculated as below:

def calculate_case_1(mus,sigma,priors):
    dimension=len(mus[0])
    if (dimension,dimension) != sigma.shape:
        return NameError("Dimension mismatch")
    mu_dff=(mus[0]-mus[1])
    w= mu_diff
    x0= 1/2 * (mus[0]+mus[1]) - (sigma[0][0]**2)/(np.linalg.norm(mu_diff))*(math.ln(prior[0]/prior[1])**mu_diff)
    return w,x0

def create_data(mu,sigma):
    
