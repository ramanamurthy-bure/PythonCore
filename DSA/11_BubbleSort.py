# Bubble Sort
l1 = [5,6,3,1,4,8,8,8,10,34,55,24,11,9,18]
print (l1)

for i in range(len(l1)-1,0,-1):
    for j in range(i):
        if(l1[j] > l1[j+1]):
            l1[j],l1[j+1] = l1[j+1],l1[j]
print (l1)