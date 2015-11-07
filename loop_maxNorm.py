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
	k = 100
	s = (k,n)

	a = np.zeros(s)

	random.seed(time.time())

	for i in range(k):
		for j in range(n):
			a[i][j] = random.random()

	#print "[+] Matrix in use is: \n", a
	#print "==================================================================="
	diff_array = np.zeros((k,k))
	sorted_diff_array = np.zeros((k,k))
	max_norm_max = np.zeros(k)
	max_norm_min = np.zeros(k)
	r = np.zeros(k)

	for i in range(k):
		for j in range(k):
			if i != j:
				diff_array[i][j] = max(abs(np.subtract(a[i],a[j])))

	#print "[+]Infinity Norm is: \n", diff_array
	#print "==================================================================="

	for i in range(k):
		sorted_diff_array[i] = sorted(diff_array[i])
		max_norm_max[i] = sorted_diff_array[i][-1]
		max_norm_min[i] = sorted_diff_array[i][1]
	#print "[+] Sorted Inifinity Norm Array is: \n", sorted_diff_array
	#print "==================================================================="

	for i in range(k):
		r[i] = max_norm_min[i]/max_norm_max[i]

	#print "[+] Min distances are: \n", max_norm_min
	#print "==================================================================="
	#print "[+] Max distances are: \n", max_norm_max
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
print "###################################################################"
print "The list of all average ratios is: \n", avg_ratios_list
print "###################################################################"

#list_to_plot = zip(dimensions,avg_ratios_list)
#print "%% \n", list_to_plot, "\n %%"  
plt.plot(dimensions,avg_ratios_list, 'ro')
plt.axis([0, 100, 0, 1])
plt.errorbar(dimensions,avg_ratios_list, yerr = std_ratios_list, linestyle='none')
plt.ylabel('Average of ratios')
plt.xlabel('Dimensions')
plt.title('Average ratios for K=100')
plt.show()