# Write your code here
import string

s = "0123456789yz"
alphalist = list(string.ascii_lowercase)
nolist = list(range(10))
print(nolist)
print(alphalist)

lenofno = len(nolist)

for x in range(lenofno):
    if str(x) in s:
        nolist.remove(x)
    else:
        pass

charlist =[]
for y in alphalist:
    if y in s:
        charlist.append(y)
    else:
        pass

for z in charlist:
    alphalist.remove(z)

print(nolist)
print(alphalist)
