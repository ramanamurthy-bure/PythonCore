x = 100
# Here x is variable and 100 is value
# Variable are used to store the date. As soon as we store the value to variable some memory will be allocated
# In python, No need to specify the data type while creating variable. So we call it as dynamically typed language
# x = 100

# Here x will be considered as integer variable dynamically. No need to specify the type of data like in Java
# Like other programming languages python also have various data types.
# But it is not mandatory to specify the data type in front of the variable

"""
Text Type : str
Numeric Types : int, float
Sequence Types :list, tuple
Mapping Types : dict
Set Types : set
Boolean Type : bool 
"""
# In Python default type is 'NonType'

x = 100  # Here int is type of variable x. To know the type of variable we need to use the type function in python
print(type(x))  # <class 'int'> . This is belonged to int class type

y = 10.5  # Here float is type of variable y.
print(type(y))  # <class 'float'> . This is belonged to int class type

s1 = "Welcome-1"  # We can declare the string in python using double quotes
s2 = 'Welcome-2'  # We can declare the string in python using single quotes
c1 = 'A'  # We can declare the char in python using double quotes - This is also considered as String
c2 = "C"  # We can declare the char in python using single quotes - This is also considered as String

print(type(s1))  # <class 'str'>
print(type(s2))  # <class 'str'>
print(type(c1))  # <class 'str'>
print(type(c2))  # <class 'str'>

b1 = True  # Boolean declaration in Python
b2 = False  # Boolean declaration in Python

print(type(b1))  # <class 'bool'>
print(type(b2))  # <class 'bool'>

# We can also change the type of variable after it was already declared. Here b1 is declared as bool type already
# After the below statement it is now converted to int type
b1 = 10
print(type(b1))  # <class 'int'>

del b1  # To delete the variable
print(b1)  # This will give Name error as b1 is deleted using above statement

#Numbers:Store numerical information and come in two forms
# Integer - Whole numbers
# Floating Point - Numbers with decimals

# Strings: Ordered sequence of characters


