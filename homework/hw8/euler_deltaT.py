import numpy as np
import matplotlib.pyplot as plt

def f(T,t):
    return -k*(T - Toutside)

k = 0.001
Toutside = 40

a = 0 # inital point 
b = 600 # end point
N = 1000 # number of steps
h = (b-a)/N # step size

temp = 0 

tpoints = np.arange(a,b,h)

t_solution = [] # empty solution aray

for i in range(1,5): # looping through the four different delta T
    deltaT = 1 / (2**(i-1))
    h = ((b - a)/N) * delta
    
    for t in tpoints:
        t_solution.append(temp)

        temp = temp + h*f(temp,t)

    print("delta t",deltaT,"temp",temp)

## as delta T decreases, so does the step size that the function is using. The smaller the step size, the less the error
