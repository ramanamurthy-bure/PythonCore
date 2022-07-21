"""
List comprehensions are a unique way of quickly creating a list with python
If you find yourself using a for loop along with .append() to create a list, List comprehensions
are a good alternative
"""
print("########################  (1) Without List Comprehensions ##########################################")
mystring = 'Hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

print("########################  (2) Using List Comprehensions ##########################################")
mylist = [letter for letter in mystring]
print(mylist)

print("########################  (3) Using List Comprehensions ##########################################")
mylist = [letter for letter in mystring if letter in ['e', 'l']]
print(mylist)

print("########################### (4) #######################################")
mylist1 = [num for num in range(0, 11)]
print(mylist1)

print("############################ (5) ######################################")
mylist1 = [num ** 2 for num in range(0, 11)]
print(mylist1)

print("############################ (6) ######################################")
mylist2 = [num for num in range(1, 12) if num % 2 == 0]
print(mylist2)

print("########################### (7) #######################################")
mylist2 = [num if num % 2 == 0 else 'ODD' for num in range(1, 12)]
print(mylist2)

print("########################## (8) ########################################")
celcius = [0, 10, 20, 34.5]
fahrenheit = [((9 / 5) * temp + 32) for temp in celcius]
print(fahrenheit)

print("############################ (9) ######################################")
l1 = []
for x in [2, 4, 6]:
    for y in [100, 200, 300]:
        l1.append(x * y)
print(l1)

print("########################### (10) #######################################")
l2 = [x * y for x in [2, 4, 6] for y in [100, 200, 300]]
print(l2)
