import numpy as np

def f(x):
    return x**4 - 2.*x +1

## defineing values 
N = 1000
b = 15
a = 0
h = (b-a) / N

## initalizing integral
integral = 0

## looping through the rectangular integral
for i in range(1,N):
    integral = integral + (h*f(a + (i*h)))

print(integral)
