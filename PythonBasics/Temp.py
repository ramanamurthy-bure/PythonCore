def squarePlus2(num):
    result = (num*num)+2
    return result

def checkEven(num):
    return num %2 ==0

l1 = [1,2,3,4,5]

for x in l1:
    print(squarePlus2(x))

print(list(map(squarePlus2,l1)))

print(list(filter(checkEven,l1)))

