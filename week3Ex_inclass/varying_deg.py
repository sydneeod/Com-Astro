# varying in degrees, incriments of five #
import math

v_i = 26.8 

for ang in range(0, 50, 5):
    if ang % 10 == 0:
        # quadratic broken up #
        a = 9.8 / 2
        b = v_i * math.sin(ang*math.pi/180)
        c = 2
        d = b**2 - 4*a*c
        if d > 0:
            opt_1 = (-b-c*math.sqrt(d)) / (2*a)
            opt_2 = (-b+c*math.sqrt(d)) / (2*a)
            t = max(opt_1, opt_2)
            x = 26.8
