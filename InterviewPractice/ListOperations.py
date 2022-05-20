l = [1, 9, 8, 4, 5, 1, 9, 6]
# To print all the items using for loop
for i in l:
    print(i)

# Applying the ranges
print(l[:2])  # this will print the values of index's 0,1 but not 2
print(l[2:])  # this will print the values of index's 2,3,4 etc...till last index
print(l[-1])
print(l[-1:])
print(l[-4:-1])
print(l[-4:])

# finding the occ of duplicate elements
lst = []
for i in l:
    if l.count(i) > 1:
        if lst.count(i) == 0:
            lst.append(i)
        print(str(i) + " displayed "+str(l.count(i))+" times")

print(lst)


list1 = ['Ramana', 'Gowri', 'Bure', 'Latha', 'Chinna', 'Swamy', 'Karthi', 'Yaswin']
print(len(list1))
print(list1[0])

# Sorting the list in descending order
list1.sort(reverse=True)
print(list1)

# Sorting the list in ascending order
list1.sort(reverse=False)
print(list1)

list1.pop()  # To remove the last item from the list
print(list1)

list1.pop(2)  # To remove the item from the list based on the index provided
print(list1)









