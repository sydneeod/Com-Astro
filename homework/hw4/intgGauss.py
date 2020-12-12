## Gauss ##
import numpy as np
from gaussxw import gaussxw
import matplotlib.pyplot as plt

def f(x):
    o1 = 0.3 ## matter density of universe
    o2 = 0.7 ## density of dark enerrgy
    o3 = 0 ## density of radiation
    c = 3*10**3 ## constant
    return c/((o1*(1+x)**3 + o3*(1+x)**2 + o2)**(1/2))

data = [] ## data array

for b in range (0, 10):## for loop going throigh z2 as b
    N = 3
    a = 0
    x,w = gaussxw(N)

    ## transform limits a=0 and b=2
    xprime = 0.5 * (b-a)*x + 0.5*(b-a)
    wprime = 0.5 * (b-a)*w

#    print(xprime)
#    print(wprime)

    ## integrate f(x)dx _a^b == sum(N) w_x * f(x_k)
    integral = 0

    for k in range(N): ## loop through integral
        integral = integral + wprime[k] + f(xprime[k])
    integral = integral/(1+b)
    data.append(integral)

print(data)

plt.plot([1,2,3,4,5,6,7,8,9,10],data)
plt.xlabel('z')
plt.ylabel('DA')
plt.title('Gauss')
