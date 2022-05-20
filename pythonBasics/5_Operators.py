# Operator is a symbol which will perform operation between  2 or more variables
# 1. Arithmetic Operators
a = 5
b = 2
print(a + b)   # This represents addition
print(a - b)   # This represents subtraction
print(a * b)   # This represents multiplication
print(a / b)   # This represents division
print(a // b)   # This represents quotient
print(a % b)   # This represents reminder
print(a ** b)   # 5**2 = 25
print("################################################################")
# 2. Relational Operators - Will hel to compare values
# < , > , <= , >=, !=
a = 5
b = 10
print(a > b)  # False
print(a < b)  # True
print(a == b)  # False
print(a <= b)  # True
print(a >= b)  # False

# 3. Logical Operators  - and or not - These are the keywords

print("############################### a=True , b=True ################################################")
a = True
b = True
print(a and b)
print(a or b)

print("############################### a=True , b=False ################################################")
a = True
b = False
print(a and b)
print(a or b)

print("############################### a=False , b=True ################################################")
a = False
b = True
print(a and b)
print(a or b)

print("############################### a=False , b=False ################################################")
a = False
b = False
print(a and b)
print(a or b)

print("############################### a=False ################################################")
a = False
print(not a)

print("############################### a=True ################################################")
a = True
print(not a)

