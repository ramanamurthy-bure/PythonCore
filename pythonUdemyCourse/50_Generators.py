# Generators
# Generator functions alow us to write a function that can send back a value and then later resume to pick up
# _where it left off
# This type of function is generator in Python, allowing us to generate a sequence of values over time
# The main difference in syntax will be the use of a 'yield' statement
# Generator functions will automatically suspend and resume their execution and
# _state around the last point of value generation
# The advantage is that instead of having to compute an entire series of values up front, the generator computes
# _one value waits until the next value is called for.

# For example, the range() function doesn't produce an list in memory for all the values from start to stop
# Instead it just keeps track of the last number and the step size, to provide a flow of numbers

# If a user did need the list, they have to transform the generator to a list with list(range(,10))

# If the output has the potential of taking up a large amount of memory and you only intend  to iterate through it,
# you would want to use a generator.

print("################################# (1) #######################################")


def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x ** 3)
    return result


print(create_cubes(10)) # Here the entire function will run at once and store all the results

for x in create_cubes(10):  # Here the entire function will run at once and store all the results
    print(x)
print("################################# (2 - Applying Generators to the above code) #######################################")

def create_cubes(n):
    for x in range(n):
        yield x ** 3

print(create_cubes(10)) # This will give generator object . We need to iterate over it to ge the numbers
print(list(create_cubes(10)))

for x in create_cubes(10):
    print(x)


print("################################# (3 - Fibanoci Series - Generator) #######################################")
# The below function is more memory efficient when we had to deal with more large numbers
#
def gen_fibon(n):
    a = 1
    b = 1

    for x in range(n):
        yield a
        a,b = b,a+b


for number in gen_fibon(10):
    print(number)

print(list(gen_fibon(10)))


print("################################# (4 - Fibanoci Series - Without Generator) #######################################")
# The below function is less memory efficient when we had to deal with more large numbers
# Here it will store all the numbers in the memory
def gen_fibon(n):
    a = 1
    b = 1
    output = []
    for x in range(n):
        output.append(a)
        a,b = b,a+b
    return output

print(gen_fibon(10))


print("################################# (5 - Simple Generator Function) #######################################")
def sipmple_gen():
    for x in range(3):
        yield x

for number in sipmple_gen():
    print(number)


g = sipmple_gen()
print(g) # Generator Object
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2
# print(next(g)) # Stop iterator error

# This is what generator object is doing internally when you call the yield keyword. It's remembering what's
# the previous one and returning the next value Instead of storing everything in the memory.

print("################################# (6 - iter function) #######################################")
# It allows us to automatically iterate through normal obejct
s = 'hello'
print("#################################")
# Iterating normally
for letter in s:
    print(letter)

#  print(next(s) # This wil give error. We need to convert this string to generator to use next method

print("################## Converting to string to generator using iter function ###############")
s_iter = iter(s)
print(next(s_iter)) # h
print(next(s_iter)) # e
print(next(s_iter)) # l
print(next(s_iter)) # l
print(next(s_iter)) # o
# print(next(s_iter)) # # Stop iterator error








