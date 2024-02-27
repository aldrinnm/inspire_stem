names = input("Enter your full names : ")
age = input("Enter your age : ")
salary = int(input("Enter your salary : "))

if salary <= 100000 :
    salary = salary + (salary * 3.0)
    print("Your new salary is : ",salary)

elif salary >= 100000 and salary <= 150000 :
    salary = salary + (salary * 1.5)
    print("Your new salary is : ",salary)

elif salary >= 150000 :
    salary = salary + (salary * 0.5)
    print("Your new salary is : ",salary)