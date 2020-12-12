## np.trapz ##
## listed below are several different ways I attempted to get my code
## to loop through the function and output an array of y values. I
## coundn't quite get this part to work.    

## np.trapz ##
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    o1 = 0.3 ## matter density of universe
    o2 = 0.7 ## density of dark enerrgy
    o3 = 0 ## density of radiation
    c = 3*10**3 ## constant
    return c/((o1*(1+x)**3 + o3*(1+x)**2 + o2)**(1/2))

#x = np.arange(0,10,0.1)
# x = [1,2,3,4,5,6,7,8,9,10]
# y=0
# data = []

# for i in range(len(x)):
#     y = f(i)/()
#     data.append(y)

# area = np.trapz(x,data)

#print(area)

data = [] ## data array

for b in range (0, 10):## for loop going through z2 as b
    
    ## definitions 
    a = 0
    N = 100
    h = (b-a)/N
    integral = 0
    
    for i in range (1,N): ## for loop for rectangular integration
        integral += f(i)
    integral = (integral/(1+b))
    data.append(integral)

print(data)
x = [1,2,3,4,5,6,7,8,9,10]
trapz = np.trapz(data,x)    
    
# for b in range(0,10):
#     a = 0
#     N = 100
#     h = (b-a)/N
#     integral = 0
    
#     for i in range(1,N):
#         integral = ((3*10**3)/((0.3*(1+i)**3 + 0.7)**(1/2)))/(1+b)
#         #integral = f(i)/(1+i)
#         data.append(integral)
    
#print(integral)
    
    

plt.plot([1,2,3,4,5,6,7,8,9,10],data)
plt.xlabel('z')
plt.ylabel('DA')
