import time
import numpy as np
from scipy.spatial import distance as dist
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import random
import sys

dimensions = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]
pct_accuracy_array = []
for n in dimensions:
	k = 1000
	m = 2000
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

	for i in range(k):
		b.append(random.randint(0,1))

	xClass = np.insert(x, n, b, axis=1)
	#print "[+] X Matrix Classes are: \n", xClass
	#print "==================================================================="

	diff_array = np.zeros((m,k))
	ind = np.zeros(m)	
	for i in range(m):
		for j in range(k):
			diff_array[i][j] = max(abs(np.subtract(y[i],x[j])))
		ind[i] = np.argmin(diff_array[i])
		
	yclasses = []
	for i in range(m):
		yclasses.append(xClass[ind[i]][-1])

	#print "[+] Real Classes we assigned: \n", yclasses
	#print "==================================================================="

	yClass = np.insert(y, n, yclasses, axis=1)
	#print "[+] Y Matrix Classes are: \n", yClass
	#print "==================================================================="

	mean = 0.0
	sigma = 0.1

	ksi = np.random.normal(mean,sigma,t)

	yPert = y + ksi
	
	diff_pert_array = np.zeros((m,k))
	ind_pert = np.zeros(m)
	for i in range(m):
		for j in range(k):
			diff_pert_array[i][j] = max(abs(np.subtract(yPert[i],x[j])))
		ind_pert[i] = np.argmin(diff_pert_array[i])

	yPertClasses = []
	for i in range(m):
		yPertClasses.append(xClass[ind_pert[i]][-1])
	
	confMatrix = confusion_matrix(yclasses, yPertClasses)
	
	print "The confusion matrix is: \n", confMatrix
	
	accuracy_array = np.subtract(yclasses, yPertClasses)
	pct_accuracy = accuracy_score(yclasses,yPertClasses)*100
	pct_accuracy_array.append(pct_accuracy)
	#print "[+] Perturbed Classes we assigned: \n", yPertClasses
	#print "==================================================================="
	print "[!!] Accuracy: ", pct_accuracy
	print "*******************************************************************"
	print "*******************************************************************"
	yPertClass = np.insert(yPert, n, yPertClasses, axis=1)
	#print "[+] YPert Matrix Classes are: \n", yPertClass
	#print "==================================================================="
plt.plot(dimensions,pct_accuracy_array, 'ro')
plt.axis([0, 100, 0, 100])
plt.ylabel('Accuracy')
plt.xlabel('Dimensions')
plt.title('Accuracy for K=%d and M=%d'%(k,m))
plt.show()