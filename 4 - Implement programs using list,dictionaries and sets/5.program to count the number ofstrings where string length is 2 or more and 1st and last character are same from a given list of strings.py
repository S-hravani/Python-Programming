#program to count the number ofstrings where string length is 2 or more and 1st and last character are same from a given list of strings
#sample list:['abc','xyz','aba','1221']
#expected result:2

list =['abc','xyz','aba','1221']
cnt = 0

for str in list:
    if len(str)>=2and str[0]==str[-1]:
        print(str)
        cnt = cnt+1

print(cnt)