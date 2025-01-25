# 15. Leap Year Checker   ?????
# - Write a program to check if a given year is a leap year.
# - Allow the user to check multiple years.


print("enter year \n")
year=list(map(int,input().split()))
for i in year:
    if (i%4==0 and (i%400==0 or i%100!=0)) :
        print(f"{i} is leap year")
    else:
        print(f"{i} is not leap year")