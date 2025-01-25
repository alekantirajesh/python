
# 12. Pattern Generator
# - Create a program that generates the following pattern based on user input `n`:
# *
# **
# ***
# ****
# - Add an option to print the pattern in reverse.


def pattern(pLength):
    for i in range(1,pLength+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
    

def reverse_pattern(pLength):
    for i in range(1,pLength+1):
        for j in range(i,pLength+1):
            print("*",end="")
        print()
    


pattern_length=int(input("enter pattern length \n"))

print("enter p for regular pattern and r for reverse pattern")

pattern_type=input()
if(pattern_type.lower()=="p"):
    pattern(pattern_length)
else:
    reverse_pattern(pattern_length)
