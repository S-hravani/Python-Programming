#Pattern Printing 1

rows = int(input("enter the no of rows = "))

for i in range(1,rows+1):
    for j in range(i):
        print(i,end=" ")
    print(" ")


#rows = int(input("Enter the no of rows = "))
#columns = int(input("Enter the no of columns = "))

#for i in range(1,rows+1):
#    for j in range(1,columns+1):
#        if i>=j:
#           print(i,end="")
#    else:
#           print(" ")
