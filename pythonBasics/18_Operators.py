'''
'''

print("############################### (1) ###################################")
my_list = [1,2,3]
for num in range(3,10,2):
    print(num)

print("############################### (2) ###################################")
print(range(3,10,2))
print(list(range(3,10,2)))

print("############################### (3) ##################################")
index_count = 0
for letter in 'abcdefg':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

print("############################### (4) ###################################")
index_count = 0
word = 'abcdefg'
for letter in word:
    print(word[index_count])
    index_count += 1

print("########################## (5)  enumerate ########################################")
word = 'abcdefg'
for item in enumerate(word):
    print(item) # This will return every item in the tuple format

print("########################  (6) Tuple Unpacking ##########################################")
word = 'abcdefg'
for index,letter in enumerate(word):
    print(index,letter,end=" ")
print("")

print("############################  (7) ######################################")
my_list1 = [1,2,3]
my_list2 = ['a','b','c']
for item in zip(my_list1,my_list2):
    print(item)

print("############################# (8)  Tuple Unpacking #####################################")
my_list1 = [1, 2, 3]
my_list2 = ['a', 'b', 'c']
for var_a,var_b in zip(my_list1, my_list2):
    print(var_a, var_b, end=" ")
print("")

print("#############################  (9) Tuple Unpacking #####################################")
# While zipping python will take the shortest list and zip it
my_list1 = [1, 2, 3, 4, 5, 6, 7]
my_list2 = ['a', 'b', 'c']
my_list3 = [100,200,300]
for var_a,var_b,var_c in zip(my_list1, my_list2,my_list3):
    print(var_a, var_b, var_c,end=" ")
print("")

print("########################### (10) #######################################")
print(list(zip(my_list1, my_list2,my_list3)))

print("############################# (11) #####################################")
print(3 in [1,2,3]) # True
print('x' in [1,2,3]) # False
print('x' in ['x','y','z']) # True
print('k' in ['x','y','z']) # False

print("############################### (12) ###################################")
print('a' in 'Ramana') # True
print('b' in 'Ramana') # False

print("################################# (13) #################################")
print('myKey1' in {'myKey1':345,'myKey2':432,'myKey3':633}) # True
print('myKey4' in {'myKey1':345,'myKey2':432,'myKey3':633}) # False

print("################################# (14) #################################")
d = {'myKey1':345,'myKey2':432,'myKey3':633}
print(633 in d.values()) # True
print(200 in d.values()) # False

print("################################# (15) #################################")
l1 = [1,2,3,4,5,6]
print(min(l1)) #1
print(max(l1)) #6

print("############################# (16)  shuffle #####################################")
# Random library
from random import shuffle
my_list4 = [1,2,3,5,6,2,1,3,4,6,8,9]
shuffle(my_list4) # this will shuffle the items in the list
print(my_list4)

print("##############################  (17) randint ####################################")
from random import randint
random_no = randint(0,100)
print(random_no)

print("##############################  (18) accepting input from user ####################################")
user_name = input("Enter your name: ")
print("You enterd your name as: ",user_name)




