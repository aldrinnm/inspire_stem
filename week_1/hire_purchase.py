# A program to find the hire purchase of an item
# Date: 21/02/2024
# Name: Aldrin

p = float(input("enter the principal :"))
r = float(input("enter the rate : "))
t = float(input("enter the time(months) : "))
d = float(input("enter the initial deposit :")) 
m = float(input("enter the total monthly installments : "))

i = ((p*r*t)/100)

h = d + (m * i)

print("the hire purchase for the item is : ",h)