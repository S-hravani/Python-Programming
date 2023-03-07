#Python function that takes a list and returns a new list with unique elements of the first list

def unique_list(l):
    list1 = []
    for x in l:
        if x not in list1:
            list1.append(x)
    return list1

l=[]
n = int(input("Enter the size of list = "))
for i in range(0,n):
    ele = int(input("Enter elements = "))
    l.append(ele)

print(unique_list(l))