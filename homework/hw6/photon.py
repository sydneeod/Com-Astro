import numpy as np
import random as rand

## initialization
c = 3*10**8 ## speed of light m/s
l = 4*10**(-3) ## free path of photon
Rsun = 7  ## radius of sun m, ficticious radius for time reasons 
count = 0 ## incrimenter/counter
dist = 0 ## distance travled 
x = 0
y = 0
mag = 0
theta = 0
path = 0 ## distance particle goes
totald = 0 ## total distance
t = 0 ## time in s it takes particle
years = 0 ## time in years

def magnitude(x,y): ## function 
    dist = np.sqrt(x**2+y**2)  ## pythagorean theorem 
    return dist

def polar(theta): ## converting 
    a = x + l*np.cos(theta) 
    b = y + l*np.sin(theta)
    return a,b

while dist < Rsun:
    path += 1
    theta = rand.uniform(0,2*np.pi) ## random theta b/t 0 and 2pi
    x,y = polar(theta)
    dist = magnitude(x,y)

totald = path*l
t = totald/c
years = (t)/(60*60*24*365)
print(years)
    
