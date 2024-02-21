# program to solve the quadratic equation
# date: 20/02/2024
# name: Aldrin


import math

a = float(input("Enter the coefficient of first term : "))
b = float(input("Enter the coefficient of second term : "))
c = float(input("Enter the constant : "))

d = (b**2) - (4*a*c)

x_1 = (-b-math.sqrt(d))/(2*a)
x_2 = (+b+math.sqrt(d))/(2*a)

print("The solution of the quadratic equation is : ",x_1)
print("The solution of the quadratic equation is : ",x_2)