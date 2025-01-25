


import random

# 3. Number Guessing Game
# - Develop a program where the computer generates a random number between 1 and 100,
# and the user guesses the number.
# - Provide hints like Too High or Too Low.
# - Use a loop to allow multiple attempts.

randomNumber=random.randint(1,100)
chances=int(input("enter number of chances you need \n"))
while(chances):
    guess=int(input("guess the value  and value should not be 0 \n"))
    if guess==0:
        continue
    diff=randomNumber/guess
    if diff>1:
        print("high")
    elif diff==1:
        print("found the number")
    else:
        print("low")
    chances-=1
     