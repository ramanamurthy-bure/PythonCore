print("########################### (1) #######################################")
# *args and **kwargs
def myfunc1(a,b):
    # Returns 5% of the sum
    return sum((a,b))*0.05

print(myfunc1(40,60)) # This works fine for 2 arg.
# If we want to add more args to this same function we can add below
print("########################### (2) #######################################")
def myfunc2(a,b,c=0,d=0,e=0):
    # Returns 5% of the sum
    return sum((a,b,c,d,e))*0.05
print(myfunc2(40,60))
print(myfunc2(20,60,30))
print(myfunc2(30,60,20,10))
print(myfunc2(10,60,20,10,30))
# print(myfunc2(10,60,20,10,30,11)) # This will throw error : takes from 2 to 5 positional arguments but 6 were given
print("########################### (3) *args #######################################")
# So to avoid this we can use arbitary args
def myfunc3(*args):
    return sum(args)*0.05

print(myfunc3(10,90))
print(myfunc3(10,50,40))
print(myfunc3(10,20,20,30,20))

print("########################### (4) **kwargs #######################################")
def myfunc4(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


myfunc4(fruit='apple')
myfunc4(fruit='orange')
myfunc4()
