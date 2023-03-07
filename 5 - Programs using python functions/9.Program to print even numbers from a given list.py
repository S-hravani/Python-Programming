#Program to print even numbers from a given list

def even_list(list1):
    e_list = []
    for x in list1:
        if x % 2 == 0:
            e_list.append(x)
    return e_list

list1 = []
n = int(input("Enter the no of elements in list = "))
for i in range(0,n):
    ele = int(input("Enter element = "))
    list1.append(ele)

print(even_list(list1))