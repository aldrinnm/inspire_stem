# a program that gets the sum of the first 20 numbers
# date: 26/02/2024
# name: Aldrin

sum_nums = 0
max_value = int(input("Enter the maximum number : "))

for x in range (0 , max_value+1):

    sum_nums = sum_nums + x
    print(sum_nums)