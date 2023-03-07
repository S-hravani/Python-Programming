#Python fnction to check whether a number is in a given range

def test_range(a,n,z):
    if n in range(a,z):
        print(n," is in range ",a," to ",z)
    else:
        print(n," is  not in range of ",a," to ",z)

n = int(input("Enter the number = "))
a = int(input("Enter the starting Number = "))
z = int(input("Enter the ending Number = "))

test_range(a,n,z)