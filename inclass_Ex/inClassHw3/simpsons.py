##simpsons rule##
import numpy as np 

def f(x):
    return x**4 - 2.*x + 1

## definitions 
a = 0
b = 15
N = 1000
h = (b-a)/N

## integral equation including endpoints
integral = 0
integral = integral + f(a) + f(b)

## integrals 

## odd
for i in range(1,N,2): 
    integral = integral + (f(a + (i*h))*4)

## even
for k in range(2,N,2): 
    integral = integral + f(a + (k*h))*2
    
integral = integral*(h/3)

print(integral)
