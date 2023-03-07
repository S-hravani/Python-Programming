#Python program to reverse a list

def reverse(str):
    str1 = ""
    for i in str:
        str1 = i + str1

    return str1

str = input("Enter a string = ")
print("Original string is = ",str)
print("Reversed sring is = ",reverse(str))