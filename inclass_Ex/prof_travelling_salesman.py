import numpy as np
from numpy import random
from numpy import empty #allows us to an empty numpy array

import matplotlib.pyplot as plt


#how many cities are we going to travel?
N = 25 #number of cities
Tmax = 10 #degrees
Tmin = 1e-3 #degrees
tau = 1.e4

def mag(x):
    return np.sqrt(x[0]**2. + x[1]**2.)

def distance(N,r):
    s = 0. #distance traveled
    for i in range(N):
        s = s+mag(r[i+1] - r[i])
    return s



#lets assign the city locations, and calculate the initial distance that we travel

r = empty([N+1,2],float) #define empty 2D array with city # and x,y coordinate 
for i in range(N):
    r[i,0] = np.random.random()
    r[i,1] = np.random.random()
r[N] = r[0]

#calculate the initial distance.
D = distance(N,r)

D_saved = []

T = Tmax
t = 0 #time


while T >Tmin:

    #cool a little bit
    t = t+1
    T = Tmax * np.exp(-t/tau)

    #pick to cities to swap
    i = np.random.randint(N)
    j = np.random.randint(N)
    
    #in case i accidently picked the same city twice
    while i == j:
        i = np.random.randint(N)
        j = np.random.randint(N)

    #lets swap the cities and calculate the change in distance
    oldD = D
    r[i,0],r[j,0] = r[j,0],r[i,0]
    r[i,1],r[j,1] = r[j,1],r[i,1]
    D = distance(N,r)

    deltaD = D - oldD  #difference in distances (we want this to be a
                       #negative number if its a good swap)

    if deltaD > 0: #if its a bad swap, swap it back (unless i don't)
        
        #conditional that we can lay with to try different annealing
        if np.random.random() > np.exp(-deltaD/T):
            r[i,0],r[j,0] = r[j,0],r[i,0]
            r[i,1],r[j,1] = r[j,1],r[i,1]

        D = distance(N,r)
        D_saved.append(D)

        #print('bad swap swapping back')
    else:
        D = distance(N,r)
        D_saved.append(D)


fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(np.arange(len(D_saved)),D_saved)
ax.set_xscale('log')
fig.savefig('mcmc2.png',dpi=300)
plt.show()
