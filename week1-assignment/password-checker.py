




# 11. Password Strength Checker
# - Develop a program to check the strength of a password:
# - Criteria: At least 8 characters, includes uppercase, lowercase, digits, and special
# characters.

u=l=d=s=0
input_string=input("enter a password")
for i in input_string:
    if i.isupper():
        u=1
    if i.islower():
        l=1
    if i.isdigit():
        d=1
    else:
        s=1
if u==s==d==l==1 and len(input_string)>=8:
    print("password is strong")
else:
    print("password is weak")