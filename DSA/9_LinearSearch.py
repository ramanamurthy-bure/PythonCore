# Using while loop
pos = -1
def searhWithWhile(l,n):
    i=0
    while i<len(l):
        if l[i] == n:
            globals()['pos']= i
            return True
        i = i+1
    return False

list1 = [4,5,62,3,6,5,2,1,8,14]
target = 14

if searhWithWhile(list1,target):
    print("Found at :",pos)
else:
    print("Not Found")

# Using for loop
pos = -1
def searhWithFor(l,n):
    i=0
    for x in l:
        if x==n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False

list1 = [4,5,62,3,6,5,2,1,8,14]
target = 62

if searhWithFor(list1,target):
    print("Found at :",pos)
else:
    print("Not Found")
