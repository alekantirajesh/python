# 6. Prime Numbers in a Range
# - Write a program that takes two numbers as input and prints all the prime numbers in
# that range.
# - Use a function to check if a number is prime.

def isprime(n):
    count=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            count+=1
        if count>1:
            break
    if count==0 and n!=1:
        return True
    else:
        return False
prime_range_start=int(input("enter starting range \n"))
prime_range_end=int(input("enter ending range \n"))


for i in range(prime_range_start,prime_range_end+1):
    if isprime(i):
        print(f"{i} is prime")