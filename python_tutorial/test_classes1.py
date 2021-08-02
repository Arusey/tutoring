# creating class
# class <ClassName>:
#   code block
# define function for object initialisation
# def __init__(self, other_params) 

class Person:
    def __init__(self, n, h, a):
        self.age = a
        self.name = n
        self.height = h

    # defining methods
    # define it similar to any other function except the first parameter will be self
    def add_age(self):
        self.age +=1

    def change_name(self, new_name):
        self.name = new_name


    def calculate_birth_year(self, current_year):
        # current_year = 2021
        return current_year - self.age

    def calc_height_diff(self, other_person):
        return self.height - other_person.height

    #double underscore 
    def __str__(self):
        return self.name

shopping = ["sugar", "salt", "cereal"]

shopping[0]



place = ("name", 12, 2.3242)
class Map:
    def __init__(self, distance, coordinates):
        self.distance = distance
        self.coordinates = coordinates

    def guide_user(self):
        # get the distance and coordinates for between two points on a map
        coordinateA = (10.3, 17.3) 
        return distanc


        


# instanciate a class / make an instance of a class
# varaible_name = className()

kevin = Person('kevin', 5.4, 26 )
kevin.name
#param = arg
Jon  = Person('Jonathan', 6.4, 26 )
hD = kevin.calc_height_diff()
print(hD)
print(kevin.age)
# calling a method
# variable_name.method_name(arguments)  variable_name is where the object is stored
kevin.add_age()
print(kevin.age)
print(kevin.name)

kevin.change_name('kevin_changed')
print(kevin.name)
kevin_birth_year = kevin.calculate_birth_year(2022)
print(kevin_birth_year)

print(kevin)
# def function_name(param):
#  do something with param
# function_name(value) 



