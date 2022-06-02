# Operator is a symbol which will perform operation between 2 or more variables
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
print("#########################(1)#######################################")
# 2. Relational Operators - Will help to compare values
# < , > , <= , >=, !=
a = 5
b = 10
print(a > b)  # False
print(a < b)  # True
print(a == b)  # False
print(a <= b)  # True
print(a >= b)  # False

# 3. Logical Operators  - and or not - These are the keywords

print("###############################(2) a=True , b=True ################################################")
a = True
b = True
print(a and b)  # True
print(a or b) # True

print("###############################(3) a=True , b=False ################################################")
a = True
b = False
print(a and b)  # False
print(a or b)  # True

print("###############################(4) a=False , b=True ################################################")
a = False
b = True
print(a and b)  # False
print(a or b) # True

print("###############################(5) a=False , b=False ################################################")
a = False
b = False
print(a and b) # False
print(a or b) # False

print("###############################(6) a=False ################################################")
a = False
print(not a) # True

print("###############################(7) a=True ################################################")
a = True
print(not a) # False

