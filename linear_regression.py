# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Data
X = np.array([0.02, 0.12, 0.19, 0.27, 0.42, 0.51, 0.64, 0.84, 0.88, 0.99])
t = np.array([0.05, 0.87, 0.94, 0.92, 0.54, -0.11, -0.78, -0.89, -0.79, -0.04])

# Define basis function as 4 dimensional
def phi(x) :
	return[1, x, x**2, x**3]

PHI = np.array([phi(x) for x in X])
print "PHI = "
print PHI

w = np.linalg.solve(np.dot(PHI.T, PHI), np.dot(PHI.T, t))
print "w = "
print w
"""
# w = np.dot(np.linalg.inv(np.dot(PHI.T, PHI)), np.dot(PHI.T, t)) 
"""

def f(w, x) :
	return np.dot(w, phi(x))

xlist = np.arange(0, 1, 0.01)
ylist = [f(w, x) for x in xlist]
plt.plot(xlist, ylist) # => plot the function f(w, x)

plt.plot(X, t, 'o') # => plot the data

plt.show()
