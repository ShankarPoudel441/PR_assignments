# importing sys
import sys
sys.path.insert(0, "/home/spoudel/PR_assignments/assignment_1/")

from utilities import utilities


mus=[[10,10],[1,1]]
sigmas=[[5,5],[1,1]]
numbers=[10,5]
total_data=sum(numbers)
print(total_data)

pripor_prob=[(lambda x: x/total_data)(x) for x in numbers]   # Estimated using the experiments i.e. generating n numbers of data from any of the models created





data = utilities.generate_data_uncorrleated(numbers,mus,sigmas)


# print(data.shape)
# print(data)





def calculate_case_3_constants(self):
        dimension=len(self.mus[0])
        print(self.sigmas.shape)
        if (dimension,dimension) != self.sigmas[0].shape:
            return NameError("Dimension mismatch")
        mu1=self.mus[0]
        mu2=self.mus[1]
        sigma1=self.sigmas[0]
        sigma2=self.sigmas[1]
        sigma1_inv=np.linalg.inv(sigma1)
        sigma2_inv=np.linalg.inv(sigma2)
        prior1=self.priors[0]
        prior2=self.priors[1]
        self.W12=-1/2*sigma1_inv
        self.W22=-1/2*sigma2_inv
        self.w11=np.matmul(sigma1_inv,mu1)
        self.w21=np.matmul(sigma2_inv,mu2)
        self.w10=-1/2*np.matmul(np.matmul(mu1.T,sigma1_inv),mu1) - 1/2*np.log(np.linalg.det(sigma1)) + np.log(prior1)
        self.w20=-1/2*np.matmul(np.matmul(mu2.T,sigma1_inv),mu2) - 1/2*np.log(np.linalg.det(sigma2)) + np.log(prior2)
        return self.W12,self.W22,self.w11,self.w21,self.w10,self.w20