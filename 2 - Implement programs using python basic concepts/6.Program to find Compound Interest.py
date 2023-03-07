#program to find compound interest

principle = int(input("Enter the principal amount = "))
rate = float(input("enter the rate = "))
time = int(input("Enter the time period = " ))

amount = principle * (pow((1+rate/100),time))
compound_interest = amount - principle
print("Compound Interset = ",compound_interest)