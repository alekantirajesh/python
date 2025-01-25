


# 2. Temperature Conversion Tool
# - Write a program that converts temperatures between Celsius, Fahrenheit, and Kelvin
# based on user input.
# - Use functions for each conversion.




choice=input("enter your choice C or F or K in which you want to give input \n")

if(choice.upper()=="C"):
    c=float(input("enter celsius temperature \n"))
    Fahrenheit=(9/5)*c+32
    Kelvin=c+273.15
    print(f"{c} cel to  {Fahrenheit} f")
    print(f"{c} cel to {Kelvin} k")

if(choice.upper()=="K"):
    k=float(input("enter kelvin temperature \n"))
    celsius=k-273.15
    fahrenheit=(k-273.15)*(9/5)+32
    print(f"{k} kelvin to  {fahrenheit} f")
    print(f"{k} kelvin to {celsius} c")



if(choice.upper()=="F"):  

    f=float(input("enter fahrenheit temperature \n"))

    celsius=(f - 32) * (5/9)    

    kelvin= (f - 32 )* (5/9) + 273.15
    print(f"{f} f to  {celsius} c")
    print(f"{f} f to {kelvin} k")

