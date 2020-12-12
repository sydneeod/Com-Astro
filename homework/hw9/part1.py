import matplotlib.pyplot as plt
import numpy as np
 
data = np.loadtxt("ks_observables.dat",skiprows=1) # loading the data from the .dat file

data_x = np.log10(data[:,0]) # separating column one and putting the values into an array
data_y = np.log10(data[:,1]) # separating column two and puttint the values into an array


sumx = sum(data_x) # sum data for x
sumy = sum(data_y) # sum data for y
sumx2 = 0 # initalizing sums before their for loops
sumxy = 0
S = len(data_x) # s = the number of data points

for i in range(len(data_x)): # looping through and squaring each x value
    sumx2 += data_x[i]*data_x[i]
    
for j in range(len(data_x)): # looping through and multiplying each component 
    sumxy += data_x[j]*data_y[j]
    

a1 = (sumy*sumx2 - sumx*sumxy) / (S*sumx2 - ((sumx)**2))
a2 = (S*sumxy - sumy*sumx) / (S*sumx2 - ((sumx)**2)) 

# fitting curve using homework funcion
fit = (a1*(data_x) + a2)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(data_x,data_y)
ax.plot(data_x,fit)

ax.set_xlabel('Carbon Monoxide Intensity')
ax.set_ylabel('Star Formation Rate')
fig.savefig("kennsch.png")

## worked with Joe, Raymond, and Nik
