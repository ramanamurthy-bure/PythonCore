# Python Tuples
# Python Tuples are very similar to lists. However they have one key difference - immutability.
# Once an element is inside a tuple, it can not be reassigned
# Tuples use parenthesis:(1,2,3)
print("########################## (1) ########################################")
l=[1,2,3,5,3,5,6,2]
print(l)
print(type(l)) # List
t=(1,2,3,5,3,5,6,2)
print(t)
print(type(t)) # Tuple
# We can do slicing like in lists
print(t[1:4]) # (2, 3, 5)
# You cannot add new item to the tuple
print("No of occurreces of 5 in tuple: ",t.count(5))
print("Index of 5 in tuple : ",t.index(5)) # It returns the very first occurrence of the item
print("Before Modifying index 0 in List : ",l)
l[0]="Ramana" # Allowed
print("After Modifying index 0 in List : ",l)
print("Modifying the item in Tuple not allowed : ",t)
# t[0]="Ramana" # Not Allowed  - 'tuple' object does not support item assignment
print("########################### (2) #######################################")
t = (1,2,3)
for item in t:
    print(item)
print("########################### (3) #######################################")
mylist = [(1,2),(3,4),(5,6),(7,8),(9,10),(11,12)]
print("length",len(mylist))
for item in mylist:
    print(item)
print("######################  (4) Tuple Unpacking ############################################")
# Here we can access individual item by specifing the format(a,b)
mylist = [(1,2),(3,4),(5,6),(7,8),(9,10),(11,12)]
for (a,b) in mylist:
    print(a)
    print(b)

print("######################  (5) Tuple Unpacking ############################################")
# Here we can access individual item by specifing the format(a,b)
mylist = [(1,2),(3,4),(5,6),(7,8),(9,10),(11,12)]
for a,b in mylist: # This is similar to line no 34. Parenthesis are not mandatory
    print(a)
    print(b)

print("######################  (6) Tuple Unpacking ############################################")
# Here we can access individual item by specifing the format(a,b,c,d)
mylist1 = [(1,2,4,5),(5,6,7,4),(5,7,9,6),(7,12,13,8),(9,14,15,23),(11,54,34,12)]
for a,b,c,d in mylist1:
    print(a)
    print(b)
    print(c)
    print(d)


