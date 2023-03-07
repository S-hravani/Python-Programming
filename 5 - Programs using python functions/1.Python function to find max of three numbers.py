#Python function to find max of three numbers

def maximum(a,b,c):
    if (a>b) and (a>c):
         largest = a

    elif (b>a) and (b>c):
         largest = b

    else:
         largest = c

    return largest

a = int(input("Enter first number = "))
b = int(input("Enter second number = "))
c = int(input("Enter third number = "))

print("Maximum no is = ",maximum(a,b,c))

