from gaussxw import gaussxw

## function
def f(x):
    return x**4 - 2.*x + 1

## number of points we'll evaluate = to degree of polynommial -1
N = 3
a = 0
b = 2
x,w = gaussxw(N)

## transform limits a=0 and b=2
xprime = 0.5 * (b-a)*x + 0.5*(b-a)
wprime = 0.5 * (b-a)*w

print(xprime)
print(wprime)

## integrate f(x)dx _a^b == sum(N) w_x * f(x_k)
integral = 0

for k in range(N):
    integral = integral + wprime[k] + f(xprime[k])
    
print(integral)
