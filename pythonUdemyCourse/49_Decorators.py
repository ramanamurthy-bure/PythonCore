# Decorators allow you to 'Decorate' a function
# Imagine we created a simple function
# def simple_function():
#    # Do simle stuff
#    return something

# You now have two options:
# 1. Add that extra code(functionality) to your old function
# 2. Create a brand new function that contains the old code, and then add new code to that
# But what if you then want to remove that extra 'functionality'
# You would need to delete it manually, or make sure to have the old function
# Is there a better way? Maybe an on/off switch to quickly add this functionality?

# Python has decorators that allow you to track extra functionality to an already existing functionality
# They use the @ operator and are then placed on top of the original function

# Now you can easily add on extra functionality with decorator:
#     @some_decorator
#     def simple_func():
#         Do simle stuff
#         return something

# This idea is pretty abstract in practice with Python syntax, so we will go through the steps of manually building
# out a decorator ourselves, to show what the @ operator is doing behind the scenes
# Functions are objects that can be passed into other functions
print("################################# (1) #######################################")


def hello_1(name='Ramana'):
    print('The hello() function has been executed!')

    def greet():  # This function scope is limited to function hello()
        return "This is greet() func inside hello!"

    def welcome():  # # This function scope is limited to function hello()
        return "This is welcome() func inside hello!"

    print(greet())
    print(welcome())

    print("This is the end of the hello function!")


hello_1()

print("################################# (2) #######################################")


def hello_2(name='Ramana'):
    print('The hello() function has been executed!')

    def greet():  # This function scope is limited to function hello()
        return "This is greet() func inside hello!"

    def welcome():  # # This function scope is limited to function hello()
        return "This is welcome() func inside hello!"

    print("I am going to return a function!")

    if name == 'Ramana':
        return greet  # Here we are returning the function object
    else:
        return welcome  # Here we are returning the function object


new_func1 = hello_2()  # Here we are string the function object to new variable
print(new_func1)  # This will return function object address
print(new_func1())  # This will call the function

print("################################# (3) #######################################")


def cool():
    def super_cool():
        return 'I am very cool!'

    return super_cool  # Returning the function object


some_func = cool()
print(some_func)  # This will give the function object address
print(some_func())  # This will execute the function

print("################################# (4) #######################################")


def hello():
    return "Hi Ramana!"


def other(some_def_func):  # Here passing the function object as an argument to other function
    print('Other code runs here!')
    print(some_def_func())  # Calling the function here


# Example:

def other(hello):
    print('Other code runs here!')
    print(hello())  # Calling the function here


other(hello)

# We will see decorator example using the above concepts we learnt like, how to assign function to new variable
# How to pass function object as an argument to other function etc..
print("################################# (5 - Decorator Example) #######################################")


def new_decorator(origional_func):
    def wrap_func():
        print('Some extra code, before the origional function')
        origional_func()
        print('Some extra code, after the origional function')

    return wrap_func


def func_needs_decorator():
    print('I want to be decorated')


func_needs_decorator()
decorated_func = new_decorator(func_needs_decorator)
decorated_func()

print("################################# (6 - Decorator Example) #######################################")


def new_decorator_func(origional_func):
    def wrap_func():
        print('Some extra code, before the origional function')
        origional_func()
        print('Some extra code, after the origional function')

    return wrap_func


#  Here specifying this @new_decorator_func we are passing this funct to new_decorator_func function as an argument
# No need to explicitly specify like in 124
# Also, we can comment this line #142 to turn off the decoration
@new_decorator_func
def func_needs_decorator():
    print('I want to be decorated')


func_needs_decorator()

'''
Framework : A framework is a type of software library that provides generic functionality which can be extended
by the programmer to build applications. Flask and Django are good eamples of frameworks intended for Web development

A framework is distinguished from a simple library or API. An API is a piece of software that a developer can use 
in his application. A framework is more enompassing: your entire application is structured around the framework.
(i.e it provides the framework around which you build your software)

 
'''
