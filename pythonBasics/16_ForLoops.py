'''
Many objects in the Python are "iterable", meaning we can iterate over every element in the object. Such as every
element in a list  or every character in a string.
We can use for loops to execute a block of code for every iteration.
The term iterable means you can 'iterate' over the object
For example, you can iterate over every character in a string, iterate over every item in a list, iterate over every
key in a dictionary
# Syntacx of a for loop
my_iterable = [1,2,3]
for item_name in my_iterable:
    print(item_name)
'''
print("######################  (1) ############################################")

x = [1,2,3]
for i in x:
    pass # After indentation python expects some code. Here we can avoid that error by using pass
print("End of my script")
print("######################  (2) ############################################")
list1 = [3,4,2,2,4,2,3,31,2,10,3,43,24,46,66,42,212,333]
for x in list1:
    if x%2 == 0:
        print(f"Even no : {x}")
    else:
        print(f"Odd no : {x}")
print("######################  (3) ############################################")
list_sum = 0
for x in list1:
    list_sum = list_sum+x
    print(list_sum)
print("Total sum of all the items in the list: ",list_sum)
print("######################  (4) ############################################")
s = "Ramana Murthy Bure"
for x in s:
    print(x)
print("######################  (5) ############################################")
# If we don't want to use any variable we can use _ like below
s = "Ramana Murthy Bure"
for _ in s:
    print(_)
print("######################  (6) ############################################")
t = (1,2,3)
for item in t:
    print(item)
print("######################  (7) ############################################")
mylist = [(1,2),(3,4),(5,6),(7,8),(9,10),(11,12)]
print("length",len(mylist))
for item in mylist:
    print(item)
print("###################### (8) Tuple Unpacking ############################################")
# Here we can access individual item by specifing the format(a,b)
mylist = [(1,2),(3,4),(5,6),(7,8),(9,10),(11,12)]
for (a,b) in mylist:
    print(a)
    print(b)

print("###################### (9) Tuple Unpacking ############################################")
# Here we can access individual item by specifing the format(a,b)
mylist = [(1,2),(3,4),(5,6),(7,8),(9,10),(11,12)]
for a,b in mylist: # This is similar to line no 33. Parenthesis are not mandatory
    print(a)
    print(b)

print("###################### (10) Tuple Unpacking ############################################")
# Here we can access individual item by specifing the format(a,b)
mylist1 = [(1,2,4,5),(5,6,7,4),(5,7,9,6),(7,12,13,8),(9,14,15,23),(11,54,34,12)]
for a,b,c,d in mylist1:
    print(a)
    print(b)
    print(c)
    print(d)






