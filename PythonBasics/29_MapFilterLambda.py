print(map)

print("########################### (Map)#######################################")


# map function will execute the given function for the no of iterables .
# We no need to add parenthesis while calling function in map.
# We just need to specify the name of the function
# syntax :
# map(function name without parenthesis, iterable)

def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]

print(map(square, my_nums))  # This will return the address
print(list(map(square, my_nums))) # This will return list

for item in map(square, my_nums):
    print(item)


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "EVEN"
    else:
        return mystring[0]


my_names = ['Ramana', 'Bure', 'Uma', 'Swamy', 'Gowri', 'Jegan', 'Chinna']
print(list(map(splicer, my_names)))

print("########################### (Filter)#######################################")


# syntax :
# filter(function name without parenthesis, iterable)

def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 4, 5, 6, 7, 8, 3, 223, 32]
print(filter(check_even, my_nums))  # This will return the address
print(list(filter(check_even, my_nums)))

for l in filter(check_even, my_nums):
    print(l)

print("########################### (Lamda)#######################################")


# Normal Function - This will have the function name
def square(num):
    result = num ** 2
    return result


# lambda Function - This will not have the function name so it is called anonymous function
# Syntax : lambda varname : expression with the variable
# Example : lambda num:num**2

# so instead of writing seperate functions and using them in map or filter, we can write them using lambda function

my_names = ['Ramana', 'Bure', 'Uma', 'Swamy', 'Gowri', 'Jegan', 'Chinna']
print(list(filter(lambda mystring: len(mystring) % 2 == 0, my_names)))

my_nums = [1, 2, 4, 5, 6, 7, 8, 3, 223, 32]
print(list(map(lambda num: num ** 2, my_nums)))

my_nums = [1, 2, 4, 5, 6, 7, 8, 3, 223, 32]
print(list(filter(lambda num: num % 2 == 0, my_nums)))
