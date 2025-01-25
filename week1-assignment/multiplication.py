# 8. Multiplication Table Generator
# - Create a program to generate a multiplication table for any number provided by the user.
# - Allow the user to specify the range of the table.

print("enter the number \n")
number=int(input())
n=int(input("enter range \n"))

for i in range(1,n+1):
    print(f"|{number} * {i} = {number*i}  |")