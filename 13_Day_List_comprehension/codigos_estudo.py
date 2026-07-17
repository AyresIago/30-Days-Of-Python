#sintax
'''
[expression for in iterable if condition]
'''

#example 1

#For instance if you want to change a string to a list of characters. You can use a couple of methods. Let's see some of them
#one way
language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

#second way

lst = [i for i in language]
print(type(lst))
print(lst)

# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

'''
Lambda function is a small anonymous function without a name. 
It can take any number of arguments, but can only have one expression. 
Lambda function is similar to anonymous functions in JavaScript. 
We need it when we want to write an anonymous function inside another function.
'''
'''
----syntax------
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
'''

# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22



