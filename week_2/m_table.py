# A program to generate a mathematical table
# date: 22/02/2024
# name: Aldrin

num = int(input("the multiplication table of"))
for n in range ( 1 , 11) :
    print(num, 'x', n, '=',num * n)

#full set
#multiplication table consisting 1 - 9
    
for column in range (1 - 10) :
    for rows in range (1 - 10) :
        print(rows * column , end = '\t')
        