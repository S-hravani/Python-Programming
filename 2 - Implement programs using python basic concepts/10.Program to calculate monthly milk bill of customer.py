#Program to calculate monthly milk bill of customer

litre = int(input("Enter the no of litres milk taken by customer per day = "))
rate = int(input("Enter the rate for 1 litre = "))
days = 30

monthly_bill = litre * rate *days
print("monthly milk bill of customer = ",monthly_bill)