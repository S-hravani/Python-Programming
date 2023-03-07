#Python function that acepts a string and calculate number of upper case and lower case letters

upcnt = 0
locnt = 0

def string_test(s):
    global upcnt
    global locnt

    for c in s:
        if c>='A' and c<='Z':
            upcnt = upcnt+1
        elif c>='a' and c<='z':
            locnt = locnt+1
        else:
            pass
    print("Original string is: ",s)
    print("count of uppercase letters = ",upcnt)
    print("Count of lowercase letters = ",locnt)


string_test(input("enter a string = "))
