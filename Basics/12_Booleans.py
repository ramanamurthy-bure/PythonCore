# Python Booleans are operators that allow you to convey True or False statements
# These are very important later on when we deal with control flow and logic!
print(type(True))
print(type(False))
# print(type(true)) # Name error
print(1 > 2)  # False
print(1 < 2)  # True
print(1 < 1)  # False
print(1 == 1)  # True
print(3.0 == 3)  # True
print(3.0 == 2)  # False
print("bye" == "Bye")  # False
print('2' == 2)  # False
print(3 != 2)  # False
b = None
print(type(b))

l1 = [1, 2, [3, 4]]
l2 = [1, 2, {'k1': 4}]
print(l1[2][0] > l2[2]['k1'])  # False
