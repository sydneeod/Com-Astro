# rectangular ##
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    o1 = 0.3 ## matter density of universe
    o2 = 0.7 ## density of dark enerrgy
    o3 = 0 ## density of radiation
    c = 3*10**3 ## constant
    return c/((o1*(1+x)**3 + o3*(1+x)**2 + o2)**(1/2))

data = [] ## data array

for b in range (0, 10):## for loop going through z2 as b
    
    ## definitions 
    a = 0
    N = 100
    h = (b-a)/N
    integral = 0
    
    for i in range (1,N): ## for loop for rectangular integration
        integral += (h*f(a + (i*h)))
    integral = (integral/(1+b))
    data.append(integral) ## appending each itteration into data array
    
print(data)

plt.plot([1,2,3,4,5,6,7,8,9,10],data)
plt.xlabel('z')
plt.ylabel('DA')
plt.title('Rectangular')
