l = [1,2,3]
l.append(4)
print(l)

print(l.count(12)) #0
print(l.count(2)) #1

x = [1,2,3]
x.append([4,5])
print(x) #[1, 2, 3, [4, 5]]

x = [1,2,3]
x.extend([4,5])
print(x) #[1, 2, 3, 4, 5]

x = [1,2,3]
x.insert(2,'Inserted')
print(x)

x.remove('Inserted')
print(x)
x.reverse()
print(x)











