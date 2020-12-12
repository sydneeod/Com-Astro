import math
from math import pi

## altitude h = (GMT^2/(4pi^2))^(1/3) - R ##

# constants 
G = 6.67*10**-11 # Gravitational Constant - m^3kg^(-1)s^(-2) 
M = 5.97*10**24 # Mass of Earth - kg 
R = 6371000 # Radius of Earth - km 

# user input
t = float(input("Please enter a time interval in minuites: "))
T = t*60 #putting t in seconds

# equation
h = (((G*M*T**2) / (4*pi**2))**(1/3)) - R

# output 
print("The altitude of the sattellite is", h, "meters")
