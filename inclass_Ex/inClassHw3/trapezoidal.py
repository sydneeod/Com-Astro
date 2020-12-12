import numpy as np

## function being integrated
def f(x):
    return x**4 - 2.*x + 1

## setting up values 
N = 100
b = 15
a = 0
h = (b-a)/N

## initalizing intgral answer using trapezoidal rule
integral = 0.5*(f(a) + f(b))

## integral loop
for i in range (1,N):
    integral = integral + f(a + (i*h))

integral = integral*h

print(integral)
