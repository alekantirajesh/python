

# 4. Student Grading System
# - Write a program to calculate and display student grades.
# - Input: Student&#39;s name and marks for 5 subjects.
# - Output: Total marks, percentage, grade (A/B/C/Fail based on percentage).

studentName=input("enter the name of the student \n")
a,b,c,d,e=list(map(int,input("enter five subject marks \n").split()))

total_marks=a+b+c+d+e
percentage=(total_marks/500)*100
if(percentage>90):
    grade='A'
elif percentage<90 and percentage>80:
    grade='B'
elif percentage<80 and percentage>70:
    grade='C'
elif percentage<70 and percentage>60:
    grade='D'
else:
    grade='Fail'
print(f"total marks obtained = {total_marks} \n percentage obtained = {percentage} \n grade = {grade}")