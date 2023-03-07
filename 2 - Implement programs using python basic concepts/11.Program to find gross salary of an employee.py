#Program to find gross salary of an employee
#Take basic from user
#DA is 80% and TA is 20%

basic = int(input("Enter the Basic Salary = "))
DA = 0.8 * basic
TA = 0.2 * basic

gross_salary = basic + DA + TA
print("Gross salary of an employee = ",gross_salary)