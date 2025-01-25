
# 9. String Analysis Tool
# - Write a program to analyze a string:
# - Count vowels, consonants, digits, and special characters.
# - Reverse the string and display the result.

user_string=input("enter string \n")
vowels=['a','i','e','o','u','A','E','I','O','U']
digit_count=0
v_count=0
c_count=0
specialcharacter_count=0
user_list=user_string.split()
for i in user_string:
    if i.isalpha():
        if i in vowels:
            v_count+=1
        else:
            c_count+=1

    elif i.isdigit():
        digit_count+=1
    else:
        specialcharacter_count+=1
reversed_string=user_string[::-1]
print( f"count of digits = {digit_count} \n count of vowels= {v_count} \n count of consonants= {c_count} \n count of special charcters = {specialcharacter_count} \n reverse string = {reversed_string}")
    
