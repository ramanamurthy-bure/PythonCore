# Probelem - 1:
# Create a generator that generates the squares of numbers up to some number N
from trio._util import generic_function

print("################################# (Problem -1 ) #######################################")
def gensquares(n):
    for x in range(n):
        yield x**2

for x in gensquares(3):
    print(x)

g = gensquares(3)
print(g) # This will give the generator object
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2

print("################################# (Problem -2) #######################################")
# Create a generator that yields 'n' random numbers between a low and high number(that are inputs)
# Note: Use the random library
import random
def gentoholdrandomnos(low,high,totalnos):
    for x in range(totalnos):
        yield random.randint(low,high)

for x in gentoholdrandomnos(2,50,10):
    print(x)

print("################################# (Problem -3) #######################################")
# Use the iter() function to convert the string below into an iterator
s = 'hai'

s = iter(s)
print(next(s)) # h
print(next(s)) # a
print(next(s)) # i
# print(next(s)) # Stop Iter error

print("################################# (Problem -4) #######################################")
#generator comprehensions
my_list = [1,3,4,5,7,0,2,8]
gencomp = (item for item in my_list if item>3) # HEre we are using the parantheisis bracket to make it as generator

for item in gencomp:
    print(item)






