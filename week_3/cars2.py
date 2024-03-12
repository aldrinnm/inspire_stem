# this is a class that decsribes cars

class car:
    def __init__(self,model,make,year_of_prooduction,fuel_capacity,colour,horse_power):
        self.model = model
        self.make = make
        self.year_of_production = year_of_prooduction
        self.fuel_capacity = fuel_capacity
        self.colour = colour
        self.horse_power = horse_power

    def print_make(self,make):
        print("The car is of {0} make".format(self.make))
    def set_make(self,make):
        self.make = make
    def get_make(self):
        return self.make
    def set_colour(self,colour):
        self.colour = colour
    def get_colour(self):
        return self.colour
        

my_car = car("Impala","Chevrolet","1969","2500 cc","Lilac","390 HP")
friends_car = car("Note","Nissan","2014","1400 cc","Black","150 HP")

my_car.print_make("Nissan")

my_car.set_make("Ford")
friends_car.set_make("Ferrari")

print(my_car.get_make())
print(friends_car.get_make())

my_car.set_colour("Metallic blue")
friends_car.set_colour("Beige")

print(my_car.get_colour())
print(friends_car.get_colour())

"""
ONE FORM FOR REGISTTERING STUDENTS
Name
AGE
CoURSE
"""


