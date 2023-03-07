#Python program to detect the no of local variables declared in a function

def function1():
    pass

def function2():
    a = 10
    b =25.9
    string = "Python"

print("Count of Local variables = ",function1.__code__.co_nlocals)
print("Count of Local variables = ",function2.__code__.co_nlocals)
