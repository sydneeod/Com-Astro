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
    
    k1 = h*f(temp,t)
    k2 = h*(f(temp+0.5*k1,t+0.5*h))
    temp = temp + k2
    
print(temp)

fig = plt.figure()
ax =  fig.add_subplot(111)
ax.plot(tpoints, t_solution)
ax.set_xlabel("time")
ax.set_ylabel("x(t)")
fig.savefig('rk1.png')
