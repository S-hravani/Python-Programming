#Program for how to check if given number is fibonacci number
#number is fibonacci number if 5*n*n-4 or 5*n*n+4 is perfect square


import math

def isperfect_square(x):
    s = int(math.sqrt(x))
    return s*s == x

def isfibonacci(n):
    return isperfect_square(5*n*n+4) or isperfect_square(5*n*n-4)

for i in range(1,11):
    if isfibonacci(i):
        print(i," is fibonacci number")
    else:
        print(i," is not fibonacci number")