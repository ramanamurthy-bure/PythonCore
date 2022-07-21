# We can use logical operators to combine comparisons:
'''
1. and
2. or
3. not
'''
# Let's explore how to use these!

print(1 < 2)  # True
print(2 < 3)  # True
print(1 < 2 < 3)  # True
print(1 < 2 > 3)  # False
print(1 < 2 and 2 < 3)  # True
print(1 < 2 and 2 > 3)  # False
print(1 < 2 or 2 > 3)  # True
print(1 == 1)  # True
print(not (1 == 1))  # False
print(not 2 > 1)  # False
