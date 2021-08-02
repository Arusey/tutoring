# Object oriented programming.


# bicycle = color
#         wheel_types
#         sadle_type

# class Name(): blue print for objects
#   class variable
class Wheel:
    def __init__(self, shape, size) :
        self.shape = shape
        self.size =size



wheel20 =  Wheel('circular', 20)
wheel21 =  Wheel('octagon', 21)
class Bicycle:
    color = 'red'
    wheel_type = 'spoked'
    sadle_type = 'leather'
    wheel = None

    def bike_method(self):
        print(self)

    def set_color(self, color):
        self.color = color

    def print_color(self):
        print(self.color)
    
    def set_wheel(self, wheel):
        self.wheel = wheel 


    # def __str__(self) :
    #     return   f"color : {self.color }  wheelType : {self.wheel_type}"

    # def fucntion(paremeters):
    #     code''

class Loan:
    def __init__(self, principal, interest, years=0):
        self.p = principal
        self.i = interest
        self.y = years

    def calculate_loan_payment(self):
        return self.p * (self.i / 100) * self.y
    
    def set_area(self, area):
        self.area = area

    # def __str__(self) -> str:
    #     return self.p
       



bike =  Bicycle()
bike2 =  Bicycle()
bike.set_color('yellow')
bike2.set_color('green')

bike.print_color()
bike2.print_color()
bike.set_wheel(wheel20)
print(bike.wheel)

bike.bike_method()
bike2.bike_method()


long_loan = Loan(1000, 10, years = 20 )
short_loan = Loan(1000, 10, years = 2)

long_loan_interest =  long_loan.calculate_loan_payment()
short_loan_interest =  short_loan.calculate_loan_payment()

print(long_loan_interest)
print(short_loan_interest)






class MyClass:
    x = 0
    y = ""

    def __init__(self, anyNumber, anystring):
        self.x = anyNumber
        self.y = anystring

    # def __str__(self) -> str:

    #     return f"Myclass {str(self.x)} + {str(self.y)}"

        # return 'MyClass(x=' + str(self.x) + ' ,y=' + self.y + ')'


# myObject = MyClass(10, "Hello")

# print(myObject.__str__())
# print(myObject)
# print(str(myObject))

#built in functions in python

random_string = "this+is+a+string"

print(random_string.find("is"))
print(len(random_string))
print(random_string.split("+"))

password = "myPassword"


print(type(password.strip()))
print(password.split())

our_string = "This is tutoring"
new_string = our_string.replace("This is", "django")
print(our_string)
print(new_string)


# print(int(our_string))


print(int("12") * 7)
print(int(20.7))
print(int(False))
print(int(True))

x = float(24.83) * float(7.233)
print(x)
print(round(x, 6))

#modulus 
print(34.4 % 2.5)
print(34.4 / 2.5)

# for i in range(1, 20):
#     if i % 2 == 0:
#         print(i, "this is even")
#     else:
#         print(i % 2)
#         print(i, "this is odd")


#floor division

print(12.4 // 2)
print(5.5 // 4.5)
print(4.453341233141331231 // 2.2342342342)

# print(f"$ {%2.f} {4.4533412331413312312}")

print("%.2f" % (3424.23233323122332))



{
    "email": 'jon@email.com',
    "password": 'pass123'
}


# empty_dict = {}

# phone_book = { 
#     "Batman": 32323,
#     "Superman": 234232,
#     "Aquaman": 2321
# }

# print(phone_book)

empty_dict = dict()


phone_book = dict(Batman=1213, Superman=3223, Aquaman=23423)
print(phone_book)

print(phone_book["Aquaman"])
print(phone_book.get("Aquaman"))
#add an entry
phone_book["Antman"] = 2138632819

print(phone_book)
#deleting/removing an entry
del(phone_book["Aquaman"])
print(phone_book)

phone_book.pop("Batman")
print(phone_book)
print(len(phone_book))
# random_list = [1, 2, "this", 4, 5]
# random_list.append(6)
# random_list.pop(6)
# print(random_list)

print("Batman" in phone_book)

phone_book2 = dict(wonderwoman=122321, Flash=3247927)
#copying
phone_book.update(phone_book2)
print(phone_book)

#Dictionary comprehension

players = {
    1: "Ronaldo", 
    2: "Messi",
    3: "Neymar",
    4: "Hazard"
}

new_players = {key**2: players + "!" for (key, players) in players.items()}

# print(new_players)

# for (key, player) in players.items():
#     new_players = {key**2: player + "!"}
#     print(new_players)


# print(players)
# print(new_players)



#tuple

#tuples are immutable #lists are mutable

products = ("Mustang", "Toyota", 3131)
cars = ("Nissan", "Vw", 123)

#merging
awesome_car = products + cars
print(awesome_car)

print("Mustang" in products)

#nesting
awesome_cars = (products, cars)
print(awesome_cars)

