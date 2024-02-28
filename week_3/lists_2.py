friends = ["sam","victoria","kate","wesley","stan","lorna"]

for friend in friends:
    print(friend)

enemies = friends[:] #to copy one list to another

print(enemies)

fruits =("guava","lemon","mango","lime","strawberry","pineapple")
#to slice the list to get part of the list

print(fruits[0:3])



print(fruits)

squares = []#initialises an empty list

for x in range (0,11):
    squares.append(x**2)
print(squares)