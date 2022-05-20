'''
Create a list of all odd numbers between 1 and a max number.
Max number is something you need to take from a user using input() function
'''
maxNo = int(input("Enter Max No : "))
for x in range(1,maxNo,2):
    print(x)