
def appendtext(fname):
    with open(fname,"a") as fp:
        fp.write("appending line 1")
        fp.write("appending line 2")
    fp.close()

#y = open("demo.txt")
#print(y.read())
appendtext("demo.txt")

x = open("demo.txt")
print(x.read())