#Python fnction to multiply all the numbers in a list

def multiplication(numbers):
    mul = 1
    for x in numbers:
        mul = mul*x

    return mul

print("multiplication = ",multiplication((8,2,3,-1,7)))