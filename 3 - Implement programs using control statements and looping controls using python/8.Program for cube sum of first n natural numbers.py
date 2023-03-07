#Program for Sum of Cubes of first n natural numbers

n = int(input("Enter the number = "))
sum = 0

for num in range(1,n+1):
    sum = sum + num**3

print("Sum of cubes of first ",n," natural numbers is ",sum)