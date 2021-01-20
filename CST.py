## Description : This code creates a set of airfoil coordinates using CST parameterisation method
## Input : wl = CST weights of lower surface
##	   ws = CST weights of upper surface
##	   dz = half trailing edge thickness
##	   yte = y-coordinate of TE
## Output: x, y = set of coordinates of airfoil generated by CST

import numpy as np
import math as mt
import matplotlib.pyplot as plt

## Definition of the function that performs the CST parameterisation calculus
## The output is the y-coordinates of each airfoil surface
def classShape(w, x, N1, N2, dz, yte):
	n = len(w)-1
	C = np.zeros((len(x),1))
	S = np.zeros((len(x),1))
	K = np.zeros((len(w),1))
	y = np.zeros((len(x),1))
	
	for i in range(len(x)):
		C[i] = pow(x[i], N1)*pow((1-x[i]), N2)
	
	for i in range(n+1):
		K[i] = mt.factorial(n)/(mt.factorial(i)*(mt.factorial(n-i)))
	
	for i in range(len(x)):
		S[i] = 0
		for j in range(n+1): 
			S[i] = S[i] + w[j]*K[j]*pow(x[i], (j))*(pow((1-x[i]), (n-(j))))
	
	for i in range(len(x)):
		y[i] = C[i]*S[i] + x[i]*(dz+yte)
	
	return y

## Definition of the main function
def CST(wl, wu, dz, N, yte):
	xu = np.linspace(0,1,N//2)
	xl = np.linspace(1,0,N//2)
	y = np.zeros((N+1, 1))
	
	N1 = 0.5
	N2 = 1
	
	yl = classShape(wl, xl, N1, N2, -dz, yte)
	yu = classShape(wu, xu, N1, N2, dz, yte)
	
	x = np.concatenate((xl, xu), axis=None)
	y = np.concatenate((yl, yu), axis=None)
	
	return x, y
	


#wl = [-0.17, 0.37, 0.43, 1.3, 1.4]
#wu = [0.8, 1.7, 2, 3.3, 3]
#dz = 0.01
#N = 100
#yte = -1
#c = 1
#
#x, y = CST(wl, wu, dz, N, yte, c)
#
#plt.plot(x,y)
#plt.show()