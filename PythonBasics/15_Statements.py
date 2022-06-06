'''
Let's begin to learn about control flow
We often only want certain code to execute when a particular condition has been met
For example, if my dog is hungry(some condition), then i will feed the dog(some action)
To control this flow we use some keywords
1. if
2. elif
3. else

Control flow syntax makes use of colons and indentation(whitespace)
This indentation system is crucial to python and is what sets it apart from other programming languages.
Syntax of an if/else statement:
if some_condition:
    # execute some code
elif:
    # do something different
else:
    # do something else
'''
print("######################  (1) ############################################")
if True:
    print("It's True")

a=10
if a>20:
    print("It's True")
else:
    print("It's False")

print("######################  (2) ############################################")
hungry = True
if hungry:
    print("I am hungry, Feed Me")
else:
    print("No food required")

print("######################  (3) ############################################")
hungry = False
if hungry:
    print("Feed Me")
else:
    print("No food required")

print("######################  (4) ############################################")
# To check multiple conditions
loc = 'Bank'
if loc =='Auto Shop':
    print("Cars are cool!")
elif loc =='Bank':
    print("Money is cool!")
elif loc =='Store':
    print("Welcome to the store!")
else:
    print("I do not know much")









