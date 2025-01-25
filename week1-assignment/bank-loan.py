   



# 7. Bank Loan Eligibility
# - Develop a program to check loan eligibility:
# - Input: Salary, age, and credit score.
# - Output: Loan approval or rejection with reasons.

print("enter the details \n")

salary=int(input("enter salary \n"))
age=int(input("enter age \n"))
credit_score=int(input("enter credit score \n"))

if(age>18 ):

    if(credit_score>700):
        if salary>15000:
            print("the customer is eligible for loan")
        else:
            print("the customer salary is low so he may not be able to  pay the loan amount and interests ")

    else:

        print("he not eligible because his credit score is less which indicates that we cannot trust the person as the person is not paying his dues in regular intervals")

else:
    print("loan cannot be sanctioned due to below age")