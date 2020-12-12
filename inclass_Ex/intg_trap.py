def f(x):
    return x**4 - 2.*x +1

#user sets N
N = 10

a=0
b=2

h=(b-a)/N

#integral = h = (0.5 f(a)+ (sum_k=1^N-1 f(a+k*h) )) 

answer = 0.5 * (f(a)+f(b)) 
for k in range(1,N):
    answer = answerr + f(a+k*h)
answer = answer+h

print(answer)
