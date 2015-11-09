# Uncomment 'print' lines for debugging

import time
import numpy as np
from scipy.spatial import distance as dist
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import random
import sys

dimensions = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]

for n in dimensions:
	sample_size = 100
	y_sample_size = 100
	s = (sample_size,n)
	t = (y_sample_size,n)

	x_matrix = np.zeros(s)
	y_matrix = np.zeros(t)
	x_random_classes = []

	random.seed(time.time())
	
	print "[+] For " , sample_size, " points and ", n, " dimensions we have: "
	#print "==================================================================="

	for i in range(sample_size):
		for j in range(n):
			x_matrix[i][j] = random.random()
			
	for i in range(y_sample_size):
		for j in range(n):
			y_matrix[i][j] = random.random()

	#print "[+] X Matrix in use is: \n", x_matrix
	#print "==================================================================="
	#print "[+] Y Matrix in use is: \n", x_matrix
	#print "==================================================================="
	for i in range(sample_size):
		x_random_classes.append(random.randint(0,1))

	xClass = np.insert(x_matrix, n, x_random_classes, axis=1)
	#print "[+] X Matrix Classes are: \n", xClass
	#print "==================================================================="

	temp_min = np.zeros(y_sample_size)
	min_array = np.zeros(y_sample_size)
	min_pert_array = np.zeros(y_sample_size)
	temp_pert_min = np.zeros(y_sample_size)

	for i in range(y_sample_size):
		temp_min[i] = sys.maxint
		temp_pert_min[i] = sys.maxint
		
	for i in range(y_sample_size):
		for j in range(sample_size):
			if (dist.cityblock(y_matrix[i],x_matrix[j]) < temp_min[i]):
				min_array[i] = j
				temp_min[i] = dist.cityblock(y_matrix[i],x_matrix[j])


	#print "[+] Closest points indices: \n", min_array
	#print "==================================================================="


	y_true_classes = []
	for i in range(y_sample_size):
		y_true_classes.append(xClass[min_array[i]][-1])

	#print "[+] Real Classes we assigned: \n", y_true_classes
	#print "==================================================================="

	y_matrix_classes = np.insert(y_matrix, n, y_true_classes, axis=1)
	#print "[+] Y Matrix Classes are: \n", y_matrix_classes
	#print "==================================================================="

	mean = 0.0
	sigma = 0.05

	ksi = np.random.normal(mean,sigma,t)

	y_pert_matrix = y_matrix + ksi

	for i in range(y_sample_size):
		for j in range(sample_size):
			if (dist.cityblock(y_pert_matrix[i],x_matrix[j]) < temp_pert_min[i]):
				min_pert_array[i] = j
				temp_pert_min[i] = dist.cityblock(y_pert_matrix[i],x_matrix[j])
				
	y_pert_classes = []
	for i in range(y_sample_size):
		y_pert_classes.append(xClass[min_pert_array[i]][-1])
		
	conf_matrix = confusion_matrix(y_true_classes, y_pert_classes)
	
	print "The confusion matrix is: \n", conf_matrix
	
	accuracy_array = np.subtract(y_true_classes, y_pert_classes)
	pct_accuracy = accuracy_score(y_true_classes,y_pert_classes)*100
	#print "[+] Perturbed Classes we assigned: \n", y_pert_classes
	#print "==================================================================="
	print "[!!] Accuracy: ", pct_accuracy, "%"
	print "*******************************************************************"
	print "*******************************************************************"
	yPertClass = np.insert(y_pert_matrix, n, y_pert_classes, axis=1)
	#print "[+] YPert Matrix Classes are: \n", yPertClass
	#print "==================================================================="