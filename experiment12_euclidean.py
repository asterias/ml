import time
import numpy as np
from scipy.spatial import distance as dist
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import random
import sys

dimensions = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]

for n in dimensions:
	k = 500
	m = 500
	s = (k,n)
	t = (m,n)

	x = np.zeros(s)
	y = np.zeros(t)
	b = []

	random.seed(time.time())
	
	print "[+] For " , k, " points and ", n, " dimensions we have: "
	#print "==================================================================="

	for i in range(k):
		for j in range(n):
			x[i][j] = random.random()
			
	for i in range(m):
		for j in range(n):
			y[i][j] = random.random()

	#print "[+] X Matrix in use is: \n", x
	#print "==================================================================="
	#print "[+] Y Matrix in use is: \n", x
	#print "==================================================================="
	for i in range(k):
		b.append(random.randint(0,1))

	xClass = np.insert(x, n, b, axis=1)
	#print "[+] X Matrix Classes are: \n", xClass
	#print "==================================================================="

	temp_min = np.zeros(m)
	min_array = np.zeros(m)
	min_pert_array = np.zeros(m)
	temp_pert_min = np.zeros(m)

	for i in range(m):
		temp_min[i] = sys.maxint
		temp_pert_min[i] = sys.maxint
		
	for i in range(m):
		for j in range(k):
			if (dist.euclidean(y[i],x[j]) < temp_min[i]):
				min_array[i] = j
				temp_min[i] = dist.euclidean(y[i],x[j])


	#print "[+] Closest points indices: \n", min_array
	#print "==================================================================="


	yclasses = []
	for i in range(m):
		yclasses.append(xClass[min_array[i]][-1])

	#print "[+] Real Classes we assigned: \n", yclasses
	#print "==================================================================="

	yClass = np.insert(y, n, yclasses, axis=1)
	#print "[+] Y Matrix Classes are: \n", yClass
	#print "==================================================================="

	mean = 0.0
	sigma = 0.1

	ksi = np.random.normal(mean,sigma,t)

	yPert = y + ksi

	for i in range(m):
		for j in range(k):
			if (dist.euclidean(yPert[i],x[j]) < temp_pert_min[i]):
				min_pert_array[i] = j
				temp_pert_min[i] = dist.euclidean(yPert[i],x[j])
				
	yPertClasses = []
	for i in range(m):
		yPertClasses.append(xClass[min_pert_array[i]][-1])
	
	confMatrix = confusion_matrix(yclasses, yPertClasses)
	
	print "The confusion matrix is: \n", confMatrix
	
	accuracy_array = np.subtract(yclasses, yPertClasses)
	pct_accuracy = accuracy_score(yclasses,yPertClasses)*100
	#print "[+] Perturbed Classes we assigned: \n", yPertClasses
	#print "==================================================================="
	print "[!!] Accuracy: ", pct_accuracy
	print "*******************************************************************"
	print "*******************************************************************"
	yPertClass = np.insert(yPert, n, yPertClasses, axis=1)
	#print "[+] YPert Matrix Classes are: \n", yPertClass
	#print "==================================================================="