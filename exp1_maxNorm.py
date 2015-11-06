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

print "[+] Matrix in use is: \n", a
print "===================================================="
diff_array = np.zeros(s)
sorted_diff_array = np.zeros(s)
max_norm_max = np.zeros(k)
max_norm_min = np.zeros(k)
r = np.zeros(k)

for i in range(k):
	for j in range(n):
		if i != j:
			diff_array[i][j] = max(abs(np.subtract(a[i],a[j])))
			#max_norm_max[i] = max(diff_array[i])
			#max_norm_min[i] = min(diff_array[i])

for i in range(k):
	sorted_diff_array[i] = sorted(diff_array[i])
	max_norm_max[i] = sorted_diff_array[i][-1]
	max_norm_min[i] = sorted_diff_array[i][1]
print "[+] Sorted Diff Array is: \n", sorted_diff_array
print "===================================================="

for i in range(k):
	r[i] = max_norm_min[i]/max_norm_max[i]

print "[+]Infinity Norm is: \n", diff_array
print "===================================================="
print "[+] Min distances are: \n", max_norm_min
print "===================================================="
print "[+] Max distances are: \n", max_norm_max
print "===================================================="
print "[+] Ratios are: \n", r

