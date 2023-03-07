#Write a program to read  a file line by line and store it into  a list

#fp = open("demo.txt","r")
#print(fp.readlines())

with open("demo.txt") as f:
    content = f.readlines()

print(content)

#remove neww line character
content = [x.strip() for x in content]
print(content)