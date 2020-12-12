 
import math
from math import pi

## altitude h = (GMT^2/(4pi^2))^(1/3) - R ##

# constants 
G = 6.67*10**-11 # Gravitational Constant - m^3kg^(-1)s^(-2) 
M = 5.97*10**24 # Mass of Earth - kg 
R = 6371000 # Radius of Earth - km 


# equation
h_45 = (((G*M*45**2) / (4*pi**2)**(1/3)) - R
h_90 = (((G*M*90**2) / (4*pi**2))**(1/3)) - R

# output 
print("The altitude of the sattellite at 45 minutes is", h_45, "meters"\n)
print("The altitude of the sattellite at 90 minutes is", h_90, "meters"\n)
print("The value for 90 minuites is incorrect because the orbit ratio is too large for this period")
