import time
import numpy as np
from scipy.spatial import distance as dist
import random
import sys

for k in (1,100):
	mean_ratio = []
	for n in [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]: 	
		
		s = (k,n)

		a = np.zeros(s)

		random.seed(time.time())

		for i in range(k):
			for j in range(n):
				a[i][j] = random.random()

		print a
		temp_max = np.zeros(n)
		temp_min = np.zeros(n)
		min_array = np.zeros(n)
		max_array = np.zeros(n)
		r = np.zeros(k)
		for i in range(n):
			temp_min[i] = sys.maxint
			temp_max[i] = -1
		for i in range(n):
			for j in range(k):
				if i != j:
					if (dist.cityblock(a[i],a[j]) < temp_min[i]):
						min_array[i] = dist.cityblock(a[i],a[j])
						temp_min[i] = min_array[i]
					if (dist.cityblock(a[i],a[j]) > temp_max[i]):
						max_array[i] = dist.cityblock(a[i],a[j])
						temp_max[i] = max_array[i]

		for i in range(n):
			r[i] = min_array[i]/max_array[i]
		

		print "[+] Min distances are: ", min_array
		print "===================================================="
		print "[+] Max distances are:", max_array
		print "===================================================="
		print "[+] Ratios are: ", r
		print "===================================================="
		print "[+] Average ratio is: ", np.mean(r)
	mean_ratio.append(np.mean(r))
	print mean_ratio
