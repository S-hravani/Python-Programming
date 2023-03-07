#program to clone or copy a list

old_list = []
size = int(input("Enter the size of list: "))

for i in range(0,size):
    num=int(input("Enter the number in list: "))
    old_list.append(num)

print("original list: ",old_list)

#cloning
list_copy = list(old_list)                   #list_copy = []
                                             #list_copy.extend(old_list)
print("After cloning: ",list_copy)