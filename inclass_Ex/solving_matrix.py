from numpy import array, empty

A = array([[2,1,4,1], 
          [3,4,-1,-1],
          [1,-4,1,5],
          [2,-2,1,3]], float)
v = array([-4,3,9,7], float) 
#Ax = v (x is what we want to solve for)
N = len(v) #number of rows/equations

#goal is to get it into upper triangular form

#Gaussian elimination
for m in range(N):
    
    #dividing by diagonal element to get diagonal to be all 1s
    div = A[m,m]
    A[m,:] /= div
    v[m] /= div #anything done to RHS needs to be done to LHS
    
    #subtracting from lower rows to get them to be zeros 
    for i in range(m+1, N): #on row m so want to go from m+1 and all rows below it # collin means do everyhing to all the columns
        mult = A[i,m] #defining multiplictive factor so we can multiply by it and subtract
        A[i, :] -= mult*A[m, :] #subtracting off multaplictive factor 
        v[i] -= mult*v[m] ##= LHS -> RHS
        #now you have an upper triangular form
        
    #backsubstitution
    x = empty(N, float)
    for m in range(N-1,-1,-1):
        x[m] = v[m]
        for i in range(m+1,N):
            x[m] -= A[m,i]*x[i]

print(x)
