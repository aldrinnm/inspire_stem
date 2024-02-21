# program to find the Nth term of a geometric equation
# date: 20/02/2023
# name: Aldrin

a = float(input("enter the first term : "))
n = float(input("enter the number of terms : "))
r = float(input("enter the common ratio"))

f = a * r**(n - 1)

print("the solution to find the Nth term of the geometric progression is : ",f)