

# 13. Palindrome Checker     
# - Write a program to check if a given string or number is a palindrome.
# - Allow the user to input multiple values using a loop.

while(1):
    print("do you want to give an input \n  ")
    input1=input("enter yes if you want to or no \n")
    if input1=='yes':
        print("do you want an integer or string as an input  \n enter int for integer   and str for string")
        input_type=input()
        if(input_type=="int"):
            user_input=int(input("enter a integer \n"))
            tmp=user_input
            tmp2=abs(user_input)
            new_value=0
            while(tmp2!=0):
                last_digit=tmp2%10
                new_value=last_digit+new_value*10
                tmp2=tmp2//10
            
            
            if abs(tmp)==abs(new_value):
                print("given number is palindrome")
            else:
                print("not a palindrome")

        else:
            user_input=input("enter a string \n")
            reverse_input=user_input[::-1]
            if user_input==reverse_input:
                print("given string is palindrome")
            else:
                print("given string is not a palindrome")


    else:
        break