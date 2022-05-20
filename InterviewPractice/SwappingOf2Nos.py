print("Swapping without 3rd variable")
x = 5
y = 10
print("->Before Swapping X: {} and Y: {}".format(x, y))
x, y = y, x
print("->After Swapping X: {} and Y: {}".format(x, y))


print("Swapping with 3rd variable")
x = 2
y = 4
print("->Before Swapping X: {} and Y: {}".format(x, y))
temp = x
x = y
y = temp
print("->After Swapping X: {} and Y: {}".format(x, y))


