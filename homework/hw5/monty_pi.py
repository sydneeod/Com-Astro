import random as rand

## initialization
trials = 1000
circle = 0
square = 0

for i in range(trials**2):
    ## random x and y values
    x = rand.uniform(-1,1)
    y = rand.uniform(-1,1)
    
    r = x**2 + y**2 ##distance from circle 
    
    if r <= 1: ## if it is inside circle, add to count
        circle += 1
        
    square += 1 ## else add to square
    
    pi = (4*circle)/square ## estimation of pi
    
print(pi)
