# Selection Sort
l1 = [5,6,3,1,4,8,8,8,10,34,55,24,11,9,18]
print (l1)

for i in range(len(l1)-1):
    minpos = i
    for j in range(i,len(l1)):
        if(l1[j] < l1[minpos]):
            minpos = j
    l1[i],l1[minpos] =l1[minpos] ,l1[i]
    print(l1)

print (l1)