
#q3-create a python function that can calculate the age of a
# student, if the student age is greater than or equal to 18 it should return True else False.



current_year = 2023
average_age = 18
def myfun():
  student_name = input("Enter your name: ")
  student_age = int(input("Enter your date of birth: "))
  if student_age <=2005:
    final_age = current_year - student_age
    print("True" ,student_name, "Your Eligible You are" , final_age, "years old")
  else:
    final_age = current_year - student_age
    print("False" ,student_name, "Your Not Eligible you are" , final_age ,"years old")
myfun()
