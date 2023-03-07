#Program for Sum of Squares of first n natural numbers

n = int(input("Enter the number = "))
sum = 0

for num in range(1,n+1):
    sum = sum + num**2

print("Sum of Squares of first ",n," natural numbers is ",sum)