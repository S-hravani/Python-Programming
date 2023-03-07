#Write a program to count the frequency of words in a file

fname = input("Enter file name : ")
count = 0

with open(fname,"r") as f:
    for line in f:
        word = line.split()

        for i in word:
            count = count + 1
print("Frequency of words = ",count)