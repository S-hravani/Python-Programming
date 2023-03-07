#program to remove duplicates from a list

duplicate = [2,4,2,6,7,6,8,8]
final = []
for num in duplicate:
    if num not in final:
        final.append(num)

#print(list(final))
print(final)