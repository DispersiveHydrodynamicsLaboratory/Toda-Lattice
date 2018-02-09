# Plot of the Riemann problem for the Toda Lattice
# In both original and Flaschka's variables

# Import Libraries
import numpy as np
import matplotlib.pyplot as plt

# Position vectors of 'balls'
n = np.linspace(-20,20,41)
print(n)

# Parameters in Flaschka's variables
al = 1
ar = 2
bl = -3
br = 0
a  = al*(n<=0) + ar*(n>0)
b  = bl*(n<=0) + br*(n>=0)

# Parameters in original variables
p = -2*b
cl = -2*np.log(2*al)
cr = -2*np.log(2*ar)
q = cl*np.mod(n,2)*(n<=0) + (cl+cr*(n-1))*(n>0)

print(q)