# 1. ATM Simulation
# - Create a program to simulate an ATM where users can:
# - Check balance
# - Deposit money
# - Withdraw money
# - Exit
# - Use functions for each operation and implement proper input validation (e.g., insufficient
# balance for withdrawal).


def deposit(available_balance):
    amount=int(input("enter amount to be deposited \n"))
    available_balance+=amount
    print(available_balance)
    return available_balance

def withdraw(available_balance):
    amount=int(input("enter amount to be withdrawn \n"))
    if (amount>available_balance):
        print("insufficient balance for withdrawal \n")
    else:
        available_balance-=amount
        print(available_balance)
    return available_balance


atm_pin=int(input("enter atm pin \n"))  

available_balance=1000 
if(atm_pin==1234):
    while(1):
        print("enter 1 for check balance \n enter 2 for deposit money \n enter 3 for withdraw money  4 for exit \n")

        choice1=int(input())
        if(choice1==1):
            print(available_balance)

           
        elif choice1==2:
            available_balance=deposit(available_balance)
            
            
        elif choice1==4:
            break
        else:
            available_balance=withdraw(available_balance)
            
else:
    print("try again with  correct pin")

