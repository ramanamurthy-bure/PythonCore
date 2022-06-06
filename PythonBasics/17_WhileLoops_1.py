'''
While loops will continue to execute a block of code while some conditions remains True.

For example, while my pool is not full,keep filling the pool with the water
Or while my dogs  are still hungry, keep feeding my dogs
# Syntax of a while loop
while some_boolean_condition:
    # do something
else:
    # do something different. This will execute once when the condition becomes False
'''

# break, continue, pass
# break -Breaks out of the current closest enclosing loop.
# continue -Goes to the top of the closest enclosing loop.
# pass -Does nothing at all.

print("######################  (1) ############################################")
x=0
while x<=5:
    print(f"The current value of the X : {x}")
    x+=1
else:
    print("X is not less than are equal to 5")

print("######################  (2) ############################################")
my_string = "Ramana Murthy Bure"
for letter in my_string:
    if letter == 'a':
        continue # This will skip the next line execution when the above condition is true
    print(letter,end=" ")
print("")

print("######################  (3) ############################################")
for letter in my_string:
    if letter == 'y':
        break # This will skip the loop when the above condition is true
    print(letter,end=" ")
print("")

print("######################  (4) ############################################")
x=0
while x<=15:
    print(f"The current value of the X : {x}")
    x+=1
    if x == 4:
        break
else:
    print("X is not less than are equal to 15")
















