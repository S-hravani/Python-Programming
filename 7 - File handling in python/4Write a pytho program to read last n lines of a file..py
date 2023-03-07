#Write a python program to read last  n lines of a file

def lastNlines(fname, N):
    with open(fname) as fp:          #opening file using () method so that file get closed after completing work
        for line in (fp.readlines() [-N:]):    #loop to iterate last n lines and print it
            print(line, end="")

#if __name__ == '__main__' :
fname = input("Enter the file name = ")
N = int(input("Enter the no of lines = "))

try:
    lastNlines(fname, N)
except:
    print("File not found")