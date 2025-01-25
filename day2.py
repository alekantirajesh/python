# a=10
# b=10

# c,d,e=1,2,"hi"

# f=g=h=i=True

# print(a,b,c,d,e,f,g,h+i)

# #Arithmetic operators


# a=10
# b=3

# print( a+b)

# print( a-b)
# print( a*b)
# print( a/b)
# print( a//b)
# print(a**b)
# print(a%b)
# print(type(a))

# #relational operators

# c=100
# d=20

# e=c<d
# print(f'c<d   {e}')

# e=c>d
# print(f'c>d   {e}')
# e=c<=d
# print(f'c<=d   {e}')
# e=c>=d
# print(f'c>=d   {e}')
# e=c==d
# print(f'c==d   {e}')
# e=c!=d
# print(f'c!=d   {e}')


# assignment


# logical

# a=10
# b=2
# c=0
# print(c>a and b<a )  

# print(a<b and b)

# print(b or a>b)



# #membership
# print("membership")

# x="hippo"
# print("hi" in x)
# print("bye" not in x)

# #identity
# print("identity")
# a=10
# b=10

# print( a is b)
# print(a is not b)



# order of precedence 
# parenthesis
# exponentiation
# multiplication,division,floor division,modulus
# add,sub
# bitwise left shift,bitwise right shift

# 3<<5  3*(2**5)=4

# 4>>1  4/(2**1)

# x=list(map(str,input().split()))

# print(x)

# print(~5)
# a=10
# b=5
# print(a-5 is b)


### type conversion
#implicit    explicit


# tc1=10
# tc2=5.5
# tc1=tc1+tc2
# print(tc1)


# tc3=10
# tc4=float(tc3)
# print(tc3)

# tc5=5
# tc6=str(tc5)
# print(tc6)
# print(type(tc6))

# tc7=65
# tc8='a'
# print(chr(tc7))
# print(ord(tc8))

# tc9=

# tc10=list(tc9)
# tc11=tuple(tc9)
# tc12=set(tc9)
# # tc13=dict(tc9)
# # print(tc13)
# print(tc12)
# print(tc11)

# print(tc10)


#print statement

# print("hello python")
# print()
# print('wel',end='')
# print('come',end='')
# print(' to python')

# print(10)
# name='raj' 
# age=21
# print("my name is",name,"and age is ",age)

# l=[1,2,3,4]
# print(l)

# print("hi",'hello',sep="**")


# print("hello {},my age is {}".format(name,age))

# print(f"hello {name}, how are u")

#input function
# print("enter name")
# input1=input()
# print(input1)

# print("enter age")
# inp2=int(input())
# print(inp2)
# inp3=input().split(',')

# print(inp3)

# x=list(map(str,input().split()))

# print(x,end="")


# assignment2
# find area of rectangle using type conversion and format string 

# x=int(input())
# y=int(input())

# area=float(x)*float(y)

# print(f"area of rectangle is {area}")

#while

# while True:
#     lang=input("what is this programming languauge \n")

#     if lang.capitalize() =='Python':
#         print(f"you are right it is {lang}")
#     else:
#         print("not good")




# assignment 2

x=input("enter inputname \n")
y=input("enter password \n")

t=0
if x=="testuser":
    while t<3:
        if y=='Password123':
            print("valid user")
            break
        else:
            t+=1
            print("try again \n")
            y=input("enter password")
    if t==2:
        print(" 3 chances completed   so  try again after some time ")
else:
    print("invalid credentials enter correct username")

#assign 3

# check given num is prime or not

# n=int(input("enter number \n"))
# c=0
# for i in range(2,int(n/2)+1):
#     if n%i==0:
#         c+=1
#     if c==1:
#         break
# if c==0:
#     print("is prime")
# else:
#     print("not a prime")

    

# net_salary=int(input("enter salary  \n"))
# allowance=int(input("enter allowance  \n"))

# gross_sal=net_salary+allowance
# print(f"total salary = {gross_sal}")

# if(gross_sal<5):
#     print("tax paid =",gross_sal*0.1)
# else:
#     print("tax paid =",gross_sal*0.2)

    # calculate tax based on salary
    # gross salary <5lpa   tax 10%
    #   else 20%
    # gross salary
    # net salry
  

    # calculate attendence tracker based on no of classes attended 
    # if attendence is above 75 you are eligible for exam
    #     or
    #     not eligible for exam 

# total_classes=int(input("total classess"))
# class_attended=int(input("classes attended"))
# attendence_percentage= (class_attended/total_classes)*100
# if(attendence_percentage>75):
#     print("eligible")
# else:
#     print("not eligible")


