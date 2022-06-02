'''
Built-in objects in Python have a variety of methods you can use.
Let's explore in a bit more detail how to find methods and how to get information about them
'''
print("########################### (1) #######################################")
mylist = [1,2,3,4]
mylist.append(5)
print(mylist)
mylist.pop()
print(mylist)
mylist.clear()
print(mylist)
# To know the documentation for the built in function
help(mylist.pop)


