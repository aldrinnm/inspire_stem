# program to find the surface area of a cylinder
# date: 20/02/2024
# name: Aldrin

r = float(input("the radius of the cylinder is : "))
h = float(input("the height of the cylinder is : "))

f = (2* (22/7) * r**2) + (2 * (22/7) * r * h)

print("the solution to the surface area of the cylinder is : ",f)