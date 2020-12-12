## I worked on this homework together with Joe Grimm and Raymond Banton
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

tolerance = 1e-20 
y = .1 # inital random guess
n = 0.005 # steps
counter = 0
nmax = 100 

def deriv(a): # function to find the derivative using the definition of the derivative f(x+h) - f(x) / h
    
    y = .1
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
import numpy as np

A = np.array([[0,1,4,1],
             [3,4,-1,-1],
             [1,-4,1,5],
             [2,-2,1,3]], float)
v = np.array([-4,3,9,7], float)
N = len(v)

for i in range(1,N):
    if A[i,i] == 0: # if an element on the diagonal = 0, piviot 
        Acopy = np.copy(A) # copy the original arrays
        vcopy = np.copy(v)
        
        if i == 0: # if the diagonal is 0, piviot 
            A[0] = Acopy[N-1] 
            v[0] = vcopy[N-1]
            
            A[N-1] = Acopy[i]
            v[N-1] = vcopy[i]
        
        else: 
            A[i] = Acopy[i-1]
            v[i] = vcopy[i-1]
            
            A[i-1] = Acopy[i]
            v[i-1] = vcopy[i]

print(A, "A")
print(v, "v")

for m in range(N):
    div = A[m,m]
    A[m,:] /= div
    v[m] /= div
    
    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]
        
x = np.empty(N,float)
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m,i]*x[i]
        
print(A)
print(x, "solutions")
    
