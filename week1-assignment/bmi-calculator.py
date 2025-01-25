




# 18. BMI Calculator
# - Develop a program to calculate BMI:
# - Input: Weight (kg) and height (m).
# - Output: BMI value and corresponding category (Underweight, Normal, Overweight,
# Obese).

weight=float(input("enter weight"))

height=float(input("enter height"))


bmi= float(weight)/float(height*height)

if(bmi<18.5):
    print(f"bmi value is {bmi } and category is underweight")
elif bmi>=18.5 and bmi<=24.9:
     print(f"bmi value is {bmi } and category is normal")
elif bmi>=25.0 and bmi<=29.9:
      print(f"bmi value is {bmi } and category is overweight")
else:
      print(f"bmi value is {bmi } and category is obese")
