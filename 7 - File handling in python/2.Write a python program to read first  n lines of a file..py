#Write a python program to read first  n lines of a file

from itertools import islice

def file_read_from_top(fname, nlines):
    with open(fname) as fp:
        for line in islice(fp, nlines):
            print(line)

lines = int(input("enter the no of lines = "))

file_read_from_top("demo.txt",lines)