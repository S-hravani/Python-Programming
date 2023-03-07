#Write a program to read a file line by line store it into a variable

def file_read(fname):
    with open (fname,"r") as fp:
        data = fp.readlines()
        print(data)
file_read("demo.txt")