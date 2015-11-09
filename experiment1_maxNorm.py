# Uncomment 'print' lines for debugging

import time
import numpy as np
from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
import random
import sys

dimensions = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]
avg_ratios_list = []
std_ratios_list = []
for n in dimensions:
	sample_size = 5000
	s = (sample_size,n)

	x_matrix = np.zeros(s)

	random.seed(time.time())

	for i in range(sample_size):
		for j in range(n):
			x_matrix[i][j] = random.random()

	#print "[+] Matrix in use is: \n", x_matrix
	#print "==================================================================="
	diff_array = np.zeros((sample_size,sample_size))
	sorted_diff_array = np.zeros((sample_size,sample_size))
	max_norm_max = np.zeros(sample_size)
	max_norm_min = np.zeros(sample_size)
	ratios = np.zeros(sample_size)

	for i in range(sample_size):
		for j in range(sample_size):
			if i != j:
				diff_array[i][j] = max(abs(np.subtract(x_matrix[i],x_matrix[j])))

	#print "[+]Infinity Norm is: \n", diff_array
	#print "==================================================================="

	for i in range(sample_size):
		sorted_diff_array[i] = sorted(diff_array[i])
		max_norm_max[i] = sorted_diff_array[i][-1]
		max_norm_min[i] = sorted_diff_array[i][1]
	#print "[+] Sorted Inifinity Norm Array is: \n", sorted_diff_array
	#print "==================================================================="

	for i in range(sample_size):
		ratios[i] = max_norm_min[i]/max_norm_max[i]

	#print "[+] Min distances are: \n", max_norm_min
	#print "==================================================================="
	#print "[+] Max distances are: \n", max_norm_max
	#print "==================================================================="
	#print "[+] Ratios are: \n", ratios
	print "*******************************************************************"
	print "[+] For " , sample_size, " points and ", n, " dimensions we have: "
	print "==================================================================="
	print "[+] Average ratio is: ", np.mean(ratios)
	print "==================================================================="
	print "[+] Standard deviation of ratios is: ", np.std(ratios)
	print "*******************************************************************"
	avg_ratios_list.append(np.mean(ratios))
	std_ratios_list.append(np.std(ratios))
#print "###################################################################"
#print "The list of all average ratios is: \n", avg_ratios_list
#print "The list of all standard deviations of ratios is: \n", std_ratios_list
#print "###################################################################"
 
plt.plot(dimensions,avg_ratios_list, 'ro')
plt.axis([0, 100, 0, 1])
plt.errorbar(dimensions,avg_ratios_list, yerr = std_ratios_list, linestyle='none')
plt.ylabel('Average of ratios')
plt.xlabel('Dimensions')
plt.title('Average ratios for K=%d'%(sample_size))
plt.show()