s = "Ramana Murthy Bure is working as a software engineer in Bank Of America"
l1 = s.split()
print(l1)
l2=[ x for x in l1 if len(x)%2 == 0 ]
print(l2)

l1=[1,2,3]
l2=['a','b','c']
l3=[x*y for x in l1 for y in l2]
print(l3)


l4 = list(zip(l1,l2))
print(l4)

for x,y in l4:
    print(x)

l1=[1,2,3,4,5,6,7,8,9,9,10,11,12,13,14]
l5=[x if x%2 == 0 else 5 for x in l1]
print(l5)



