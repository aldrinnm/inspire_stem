# a block of code running together as a unit
# sum 10,20 add numbers (10,20)are called parametus

# 1.initialize afunction:use a key word "def"
# 2.call the function

#types
#1.user define
#2.built in

# defining aa function
def print_name():
    print("My name is Aldrin")

# calling the function
print_name()
print_name()
print_name()
print_name()

def print_details(name , age , id , gender):
    print("I am {0},I am {1} years old , my id number is {2} and my gender is {3}".format(name , age , id , gender))


print_details("Aldrin" , "18" , "21968859" , "male")
print_details("Grace" , "40" , "20408040" , "female")

def sum_nums(x,y):
    return x + y

z = sum_nums(10,20)
print(z)


def prod_nums(x,y):
    return x * y
print(prod_nums(5,16))

def print_odds(first_number,last_number):
    for i in range(first_number,last_number):
        print(i +1)


print_odds(0,15)

"""
print all odds
wrtie a funvtion to print all squares and cubes between 1 and 10
write a function to print all prime numbers between 1 and 99
write a function to calculate surface area of cylinder,cone,cube,sphere and the volume of the four
"""

#odds
def printodds(first_number,last_number):
    for i in range(first_number,last_number):
     if i%2 == 1:
        print(i) 
printodds(0,10)


#squares
for x in range(0,11):
    print(x**2)

    

#cubes
for x in range(0,11):
    print(str(x**3) + "\t",end= " ")

#prime numbers
lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)

#surface area
#cylinder
def print_sa(r,h):
   r = float(input("the radius of the cylinder is : "))
   h = float(input("the height of the cylinder is : "))
pi = 3.142
f = (2* pi * r**2) + (2 * (22/7) * r * h)

print(f)
#cone
    
#cube

#sphere
    

#volume
#cylinder
    
#cone
    
#cube
    
#sphere