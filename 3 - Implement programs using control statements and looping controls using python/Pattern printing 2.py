#Pattern printing 2

rows = 5
for i in range(1,rows+1):
    for j in range(i):
        if j == 0 or j == i-1:
            print("*",end="")
        else:
            if i!=rows:
                print(" ",end="")
            else:
                print("*",end="")
    print()