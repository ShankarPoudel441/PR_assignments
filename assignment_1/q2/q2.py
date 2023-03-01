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