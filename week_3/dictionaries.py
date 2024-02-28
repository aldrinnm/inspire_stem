my_laptop = {"make":"lenovo","colour":"grey","weight":"1","year":"2022"}

print(my_laptop["make"])
print(my_laptop["colour"])
print(my_laptop["year"])

#to change the values in a dictionary
my_laptop["colour"] = "red"
my_laptop["year"] = "2020"
print(my_laptop)

"""
for key,value in my_laptop.items():
    print(key)
    print("\n")
    print(value)
"""

#
my_laptop["size"] = "1200mm x 600mm"
print(my_laptop)

#delete an item from the list
del my_laptop["colour"]
print(my_laptop)

#copy your details
siz_laptop = my_laptop.copy()
print(siz_laptop)

"""
create a tuple of your hobbies
using dictionaries describe your fav Carr
print individual values and keys
copy the dictionary into another dictionary
"""