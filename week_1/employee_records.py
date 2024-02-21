# A program that shows the records of an employee
# Date: 21/02/2024
# Name: Aldrin

n_1 = input("Enter your first name : ")
n_2 = input("Enter your second name : ")
n_3 = input("Enter your last name : ")
a = input("Enter your age : ") 
s = float(input("Enter your salary : "))
b = float(input("Enter your bonus : "))

f_1 = s + (s * (35/100))
f_2 = b - 5000

print("Your current salary is : ",f_1)
print("Your current bonus is : ",f_2)