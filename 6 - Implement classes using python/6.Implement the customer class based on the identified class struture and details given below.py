#Implement the customer class based on the identified class struture and details given below

total_bill = 0
class Customer:
    def bill(self,bill_amount):
        bill_amount = total_bill

    def purchase(self,bill_amount):
        discount_bill = (10/100)*bill_amount
        print("discounted bill = ",discount_bill)

    def pays_bill(self,bill_amount,discount_bill,name):
        discount_bill = (10/100) * bill_amount
        bill = bill_amount - discount_bill
        print("Total bill amount to pay: ",bill)

bill_amount = int(input("Enter total amount spent = "))
discount_bill = 0
name = input("Enter the name: ")
p1 = Customer()
p1.bill(bill_amount)
p1.purchase(bill_amount)
p1.pays_bill(bill_amount,discount_bill,name)
