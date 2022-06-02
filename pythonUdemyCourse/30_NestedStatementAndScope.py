# LEGB Rule
# 1. L: Local
# Names assigned in any way within a function (def or lambda), and not declared global in that function
# 2. E: Enclosing Function Locals
# Names in the local scope of any and all enclosing functions(def or lambda), from inner to outer
# 3. G: Global(module)
# Names assigned at the top-level of a module file or declared global in a def within the file
# 4. B: Built-in(Python)
# Names preassigned in the built-in names module: open, range, Syntax Error

print("########################### (Local)#######################################")
lambda num: num ** 2  # here num is the local variable to the lambda expression
print('lambda num: num ** 2 # here num is the local variable to the lambda expression')

print("########################### (Enclosing Function Locals)#######################################")
name = 'THIS IS A GLOBAL STRING'


# Here line no 19 to 25 we say it as Enclosing Function Locals
def greet():
    # here name is Enclosing Function Locals
    name = 'Sammy'

    def hello():
        # here name is LOCAL
        print('Hello ' + name)

    hello()


greet()
# When we call great as per LEGB rule, it will check the local variable first which is 'within in the function'
# in line no 25. Then it will check the same exists in 'Enclosing Function Locals' (from line 19 to 27). So it will
# print Hello Sammy
# incase if we comment line # 21,then it will print 'THIS IS A GLOBAL STRING'


print("########################### (1. Local and Global )#######################################")
x = 50


def func(x):
    print(f'X is {x}')  # This will print x = 50

    # LOCAL REASSIGNMENT
    x = 200
    print(f'I JUST LOCALLY CHANGED X to {x}')


func(x)  # This will print x = 200 as it was reassigned inside the function
# and its scope is limited to that function alone
print(x)  # This will print x = 50

print(
    "########################### (2. Changing the Global Variable locally- Approach1 )#######################################")
y = 30


def func1():
    global y
    print(f'Y is {y}')  # This will print y = 30

    # LOCAL REASSIGNMENT ON A GLOBAL VARIABLE
    y = 150
    print(f'I JUST LOCALLY CHANGED GLOBAL Y to {y}')


func1()  # This will print y = 150 as it was reassigned inside the function
# and its scope is limited to that function alone
print(y)  # This will print y = 150

print(
    "########################### (3. Changing the Global Variable locally - Approach2 )#######################################")
y = 30


def func1(y):
    print(f'Y is {y}')  # This will print y = 30

    # LOCAL REASSIGNMENT ON A GLOBAL VARIABLE
    y = 150
    print(f'I JUST LOCALLY CHANGED GLOBAL Y to {y}')
    return y


y = func1(y)  # This will print y = 150 as it was reassigned inside the function
# and its scope is limited to that function alone
print(y)  # This will print y = 150




