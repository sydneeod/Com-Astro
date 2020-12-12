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

for t in tpoints:
    t_solution.append(temp)
    
    temp = temp + h*f(temp,t)

print(temp)

fig = plt.figure()
ax =  fig.add_subplot(111)
ax.plot(tpoints, t_solution)
ax.set_xlabel("time")
ax.set_ylabel("T(t)")
fig.savefig('euiler.png')
