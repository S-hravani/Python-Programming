# Program to find repeated items of a Tuple

tuplex = (1,2,3,5,9,9,7,6,6,5,4)

for i in tuplex:
    if tuplex.count(i)>1:
        print("repeated items = ",i)