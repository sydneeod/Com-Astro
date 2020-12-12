import numpy as np
from numpy import random
from numpy import empty

import matplotlib.pyplot as plt

N = 25 # number of people

def mag(x):
    return np.sqrt(x[0]**2. + x[1]**2.)

def distance(N,r):
    s = 0. #distance travled 
    for i in range(N):
        s = s+mag(r[i+1] - r[i])
    return s

# assigning city locations, calculating inital distance travled
r = empty([N+1,2],float)
for i in range(N):
    r[i,0] = np.random.random()
    r[i,1] = np.random.random()
r[N] = r[0]

# calculate inital distance
D = distance(N,r)

D_saved = []

for dummy_counter in range(10000):
    
    # pick 2 cities to swap    
    i = np.random.randint(N)
    j = np.random.randint(N)
    
    # in case accidentally pick same city, keep randomizing until not same
    while i == j:
        i = np.random.randint(N)
        j = np.random.randint(N)
        
    # swap cities to calculate change in distance    
    oldD = D
    r[i,0],r[j,0] = r[j,0],r[i,0] # new r of j = old r of j, does both swaps automatically once, swapping x positions for i and j 
    r[i,1],r[j,1] = r[j,1],r[i,1]
    D = distance(N,r)
    
    deltaD = D - oldD #is distance bigger or smaller? difference in distances, want it to be a - number if it is a good swap
    
    if deltaD > 0: # if bad swap, swap it back
        r[i,0],r[j,0] = r[j,0],r[i,0]
        r[i,1],r[j,1] = r[j,1],r[i,1]
        D = distance(N,r)
        D_saved.append(D)
    else:
        D = distance(N,r)
        D_saved.append(D)
        
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(np.arange(len(D_saved)),D_saved)
ax.set_xscale('log')
fig.savefig('mcmc.png',dpi=300)
