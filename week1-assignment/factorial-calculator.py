# 14. Factorial Calculator

# - Create a program to calculate the factorial of a number using a loop.
# - Include error handling for negative numbers.


number=int(input("enter a number \n"))
factorial_num=1
if number<0:
    print("factorial is defined for positive numbers")
else:
    for i in range(1,number+1):
        factorial_num*=i

    print(f"the factorial of {number} is {factorial_num}")