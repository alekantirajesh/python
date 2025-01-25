
# 5. Shopping Cart
# - Create a program to simulate a shopping cart:
# - Add items (item name and price).
# - View cart items.
# - Calculate the total price.
# - Exit.
# - Use functions and a loop to allow multiple actions.

def add(a,b):
    d[a]=b   #adding into cart
    

def totalprice():
    total=0
    for i in d:
        total+=d[i]
    print(total)


d={}
total=0
while(1):
    print("press 1 to add an item into cart \n press2 to view the cart \n press 3 to calculate total price \n  press 4 to exit \n")
    choice=int(input())
    if(choice==1):
        
        a=input("enter item name \n")
        b=int(input("enter item price \n "))
        add(a,b)
          
        
    if choice==2:
        print(d)
    if choice==3:
        totalprice()
    if choice==4:
        break

   
   