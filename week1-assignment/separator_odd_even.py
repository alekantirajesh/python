# 16. Odd and Even Separator
# - Write a program that takes a list of numbers as input and separates them into odd and
# even lists.

list1=list(map(int,input("enter list  values \n").split()))
even=[]
odd=[]
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)