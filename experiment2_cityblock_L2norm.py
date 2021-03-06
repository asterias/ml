import time
import numpy as np
from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
import random
import sys

dimensions = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]
avg_ratios_list = []
std_ratios_list = []
for n in dimensions:
	k = 1000
	s = (k,n)

	a = np.zeros(s)

	random.seed(time.time())
	
	mean = 0.0
	sigma = 1.0

	for i in range(k):
		for j in range(n):
			a[i][j] = np.random.normal(mean,sigma)

	#print "[+] Matrix in use is: \n", a
	#print "==================================================================="
	normA = normalize(a, norm='l2')
	
	temp_max = np.zeros(k)
	temp_min = np.zeros(k)
	min_array = np.zeros(k)
	max_array = np.zeros(k)
	r = np.zeros(k)
	for i in range(k):
		temp_min[i] = sys.maxint
		temp_max[i] = -1
	for i in range(k):
		for j in range(k):
			if i != j:
				if (dist.cityblock(normA[i],normA[j]) < temp_min[i]):
					min_array[i] = dist.cityblock(normA[i],normA[j])
					temp_min[i] = min_array[i]
				if (dist.cityblock(normA[i],normA[j]) > temp_max[i]):
					max_array[i] = dist.cityblock(normA[i],normA[j])
					temp_max[i] = max_array[i]

	for i in range(k):
		r[i] = min_array[i]/max_array[i]

	#print "[+] Min distances are: \n", min_array
	#print "==================================================================="
	#print "[+] Max distances are: \n", max_array
	#print "==================================================================="
	#print "[+] Ratios are: \n", r
	print "*******************************************************************"
	print "[+] For " , k, " points and ", n, " dimensions we have: "
	print "==================================================================="
	print "[+] Average ratio is: ", np.mean(r)
	print "==================================================================="
	print "[+] Standard deviation of ratios is: ", np.std(r)
	print "*******************************************************************"
	avg_ratios_list.append(np.mean(r))
	std_ratios_list.append(np.std(r))
#print "###################################################################"
#print "The list of all average ratios is: \n", avg_ratios_list
#print "The list of all standard deviations of ratios is: \n", std_ratios_list
#print "###################################################################"
  
plt.plot(dimensions,avg_ratios_list, 'ro')
plt.axis([0, 100, 0, 1])
plt.errorbar(dimensions,avg_ratios_list, yerr = std_ratios_list, linestyle='none')
plt.ylabel('Average of ratios')
plt.xlabel('Dimensions')
plt.title('Average ratios for K=%d'%(k))
plt.show()