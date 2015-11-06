import time
import numpy as np
from scipy.spatial import distance as dist
import random
import sys

k = 10
n = 10
s = (n,k)

a = np.zeros(s)

random.seed(time.time())

for i in range(k):
	for j in range(n):
		a[i][j] = random.random()

print a
temp_max = np.zeros(k)
temp_min = np.zeros(k)
min_array = np.zeros(k)
max_array = np.zeros(k)
r = np.zeros(k)
for i in range(k):
	temp_min[i] = sys.maxint
	temp_max[i] = -1
for i in range(k):
	for j in range(n):
		if i != j:
			if (dist.cityblock(a[i],a[j]) < temp_min[i]):
				min_array[i] = dist.cityblock(a[i],a[j])
				temp_min[i] = min_array[i]
			if (dist.cityblock(a[i],a[j]) > temp_max[i]):
				max_array[i] = dist.cityblock(a[i],a[j])
				temp_max[i] = max_array[i]

for i in range(k):
	r[i] = min_array[i]/max_array[i]


print "[+] Min distances are: ", min_array
print "===================================================="
print "[+] Max distances are:", max_array
print "===================================================="
print "[+] Ratios are: ", r
print "===================================================="
print "[+] Average ratio is: ", np.mean(r)
