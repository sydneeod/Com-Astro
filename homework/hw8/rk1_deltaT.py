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

        k1 = h*f(temp,t)
        k2 = h*(f(temp + 0.5*k1, t + 0.5*h))
        temp = temp + k2

    print("delta t",deltaT,"temp",temp)

## as the time step delta t goes down, the step size goes down. The error goes down as the time step becomes smaller
