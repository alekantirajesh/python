# ternery operator

# age=int(input("enter age \n"))

# ticket_price= 20 if age>=18 else 10


# print(f'ticket price ={ticket_price}')



# ##               pass statement is used to ignore definition    or   The pass statement is used as a placeholder for future code

# x=10
# if x==10:
#     print("yes")
# else:
#     pass

#function

# def emp(name='rajesh',role='sde',sal=10000000):#  parameters

#     print(f"the emp name is {name} \n and emp role is {role} \n and sal is {sal}")


# emp()
# emp('sai')
# emp('sai','web developer')
# emp('sai','full stack dev',500000000)# arguments 



# def emp(name,role='sde',sal=10000000):#  parameters followed by  default parameters

#     print(f"the emp name is {name} \n and emp role is {role} \n and sal is {sal}")



# emp('sai','web developer')
# emp('sai','full stack dev',500000000) 


#recursion

def countdown(n):
    if n==0:
        return
    else:
        print(n,)
        countdown(n-1)
countdown(10)
 

