#Program to count the number of lines in a text file
fname = input("Enter file name : ")
num_lines = 0
with open(fname,"r") as f:
    for line in f:
        num_lines = num_lines + 1
print("Number of lines = ",num_lines)
