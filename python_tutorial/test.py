# variables
# functions
# conditionals
# loops


# classes
#

# variable initialization
# varaible_name = value

name = "kevin"
name = "Jon"

# function definition
# def function_name(parameters):
#    code block
#    return

# if condition:
#    code block to excute if condition is true

# conditon or condition Will evaluate to true if both conditions are true


# for i in iterable


def addition(a, b):
    print("Calling addittion")
    return a + b


def addition_2(a, b):
    print("Calling addittion2")

    print(a + b)


# print(name)
sum1 = addition(1, 2)
addition_2(3, 2)

print('Print variable values')

# Nand to tetrir

# recursion
# having a function that calls itself
# fibonachi  1,1,2,3,5,8
# name_array = ["Jon", "Kevin", "Other"]
age_dictionary = {"Kevin": 60, "Jon": 90}
print("Dictionary", age_dictionary["Kevin"])
print("Iterable", list(age_dictionary.items()))

# print(list(range(2,10, 3)))


def fibonachi(index):
    fibonachi_items = [1, 1]
    value = 1
    prev_value = 1
    if index == 0 or index == 1:
        return value
    print(list(range(index-1)))
    for i in range(index-1):
        print("Before", value)
        temp = value  # store current value in tmp
        value += prev_value  # update value making current value previous value
        print("After", value)
        prev_value = temp  # store previous in previous value
        fibonachi_items.append(value)

    print(fibonachi_items)
    return value


def fibonichi_rec(index):
    if index == 0 or index == 1:
        return 1
    return fibonichi_rec(index-1) + fibonichi_rec(index - 2)


print(fibonachi(10))
print(fibonichi_rec(10))

# fib 0 = 1
# fib 1 = 1
# fib 2 = 2
# fib 3 = 3
# fib 4 = 5
# fib 5= 8


# class AuthModel(models.Model):
#     name = models.CharField()


# cup1 = juice
# cup2 = wine
# cup3 <= cup1 # cup1 empty cup3 juice
# cup1 <= cup2 # cup1 wine and cup 2 is empty
# cup2 <= cup3 # cup3 empty and juice in cup2


test_string = "I am a test string"
print("test" in "I am a test string")
print(5 in [1, 2, 3, 4])
test_list = [1, 2, 3, 5]
turple = (1, 2, 3)
test_list[0] = 2

# arithmetic operators
# % modulus
modulus = 10 % 3
print("Modulus")
print(modulus)

# arithmetic operators
# / division
div = 10 / 3
print("division")
print(div)


# arithmetic operators
# // integer division
div = 10 // 2.1
print("Integer div")
print(div)

# power
# **
print(4**2)



#conditionals 
# if elif

# if condition:
#     code to execute if condition is true

if 2> 40:
    print("Two is greater than 3")
elif 1> 2:
    print("Three is greater than 2")
else:
    print("Both failed")

age = 20
is_adult =  True if age > 18 else False

if age > 18:
    is_adult = True
else:
    is_adult = False

# pass do nothing

if age > 20:
    pass
else:
    print("I am okay")

# for loop
# for i in itreable assign i the current value and keep assinging next value until there are no more value

sample_list = ['sample1', 'sample2', 'sample3']
sample = (1,2,3)

for sample in sample_list:
    print(sample)

for letter in "Banana":
    print(letter)

#continue go to next iteration

#break exit the loop
print("Continue test")
for i in range(10):
    if i == 5:
        # pass
        continue
    print(i)

#while 
# while condtion:
#     code to execute

i = 0
while  True:
    print("We are at" , i)
    i +=1
    if i >= 200:
        break

        
        