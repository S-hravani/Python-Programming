#Write a program to  read an entire text file

fp = open("demo.txt","r")
content = fp.read()
print(content)
#print(fp.read(5))
#print(fp.readline())
#print(fp.readline(),end="")
#print(fp.readline())
#print(fp.readlines())
fp.close()