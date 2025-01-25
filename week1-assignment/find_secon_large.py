# 19. Find Second Largest Number
# - Write a program to find the second largest number in a list provided by the user.

list2=list(map(int,input("enter list elements \n").split()))

max1=-100000000
max2=-100000000

for i in range(0,len(list2)):
    if max1<list2[i]:
        max2=max1  
        max1=list2[i]           
    elif max2<list2[i] and max1>list2[i]:
        max2= list2[i]
print(max2)