# Python Sets

# Sets are unordered collections of unique elements.
# Meaning there can only be one representative of the same objects
# Let's see some examples

myset = set()
print(myset)
myset.add(1)
myset.add(2)
myset.add(2)
print(myset)
mylist = [1,2,33,2,2,2,1,1,1,3,4,5,6,2,1,3,4,5,22]
myset = set(mylist) # Converting list to Set
print(myset)
print("Before Poping the item",myset)
myset.pop() # To remove the last item from the set
print("After Poping the item",myset)
myset.remove(33) # To remove the specific item

# iterating the set
for x in myset:
    print(x,end=" ")
print("")

# iterating the set
while(len(myset)>0):
    popitem = myset.pop()
    print(popitem,end=" ")
print("")






