import numpy as np 

def Bv(T):
    
    h = 6.6260755 * (10**(-27)) # planck's constant (cm^2 g s^-1) 
    c = 2.99792458 * (10**10) # speed of light (cm s^-1)
    k = 1.380658 * (10**(-16)) # boltzman's constant (cm^2 g s^-2 K^-1)
    w = 870 * (10**(-4)) # wavelength (cm)
    v = c/w # frequency (hertz, s^-1)
    BvT = 1.25 * (10**(-12)) # observed intensity (cgs units)
    x = (((2*h*(v**3))/(c**2)) / (np.exp((h*v)/(k*T))-1)) - BvT # root 
    return x

tolerance = 1e-30 
y = 1 # inital random guess
n = 0.005 # steps
counter = 0
nmax = 1000

def deriv(a): # function to find the derivative using the definition of the derivative f(x+h) - f(x) / h
    
    y = 1
    n = 0.005 
    h = y + n
    BvPrime = ((Bv(y+h) - Bv(y - h)) / (2*h))
    return BvPrime


while abs(Bv(y)) > tolerance:
# while counter < nmax: # while loop to find the convergance of the root 
    
    y1 = y - (Bv(y)/ deriv(y))
    y = y1
    counter += 1
    print(counter, y1) # printing the progress to show the limit converging
    
print(y1, "is the answer to the great question... of life, the universe and everything.")

# I worked together with Joe Grim, Raymond Banton, and Nikolay Hardy on this part of the homework
