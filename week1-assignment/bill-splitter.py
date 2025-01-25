

# 10. Bill Splitter
# - Create a program to split a bill among a group of people:
# - Input: Total bill amount, number of people, and any tip percentage.
# - Output: Amount each person has to pay.

bill_amount=int(input("enter total bill"))
no_of_people=int(input("enter no of people"))
tip=int(input("enter tip percentage "))

tip_amount=bill_amount*(tip)/100
total_amount= bill_amount+ tip_amount
split_amount=total_amount/no_of_people

print(f"amount each person need to pay is {split_amount}")