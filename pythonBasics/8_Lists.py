# Python Lists
# Lists are ordered sequence that can hold a variety of object types.
# They use [] brackets and commas to separate objects in the list
# [1,2,3,4,5]
# Lists supports indexing and slicing. Lists can be nested and also can have variety of useful
# methods that can called off them
print("######################  (1) ############################################")
my_list1=[1,2,3,4,5,6,7,8,9] # Valid
my_list2=["String",100,23.2,5,7,8,10,34] # Valid
print(len(my_list1)) #9
print("######################  (2) ############################################")
my_list3=['one','two','three'] # Valid
my_newlist = my_list1 + my_list2 # TO join 2 lists
print(my_newlist)
print("######################  (3) ############################################")
my_newlist.append("four") # To add the new item to the last
print(my_newlist)
popeditem = my_newlist.pop() # To remove the last item and store in variable
print(popeditem)
print(my_newlist)
print(my_newlist)
my_newlist.pop(3) # Here 3 is index
print(my_newlist) # Removing the element based on index
print("######################  (4) ############################################")
my_newlist.insert(3,"Ramnaa") # To insert item at particular index
print(my_newlist)
my_newlist.remove("Ramnaa") # To remove the specific item.
my_newlist.remove("String") # To remove the specific item.
print("Before Sorting: ",my_newlist)
my_newlist.sort()  # To sort the list.
print("After Sorting: ",my_newlist)
my_newlist.reverse()  # To reverse the list.
print("Revered List: ",my_newlist)
slicedlist = my_newlist[1:7] # Slicing
print("Sliced List: ",slicedlist)
print("######################  (5) ############################################")
# iterating List
for x in my_newlist:
    print(x,end=" ")
print("")
# checking the particular item presence
print(100 in my_newlist)