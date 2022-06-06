from collections import Counter
print("######################################## (1) ############################################")
my_list =  [1,1,1,2,3,2,3,4,5,5,6,4,5,2,3,4,5]
c = Counter(my_list)
print(c)
print(c.most_common())
print(c.most_common(2))

print("######################################## (2) ############################################")
my_list =  ['a','b','c',2,3,2,3,4,'a','b','c',5,5,6,4,5,2,'a','b','c',3,4,5]
c = Counter(my_list)
print(c)
print(c.most_common())
print(c.most_common(3))

print("######################################## (3) ############################################")
print(Counter('assasasasbsfjadjdebbasas'))
s = "How many times does each word show up in this sentence with a word"
c = Counter(s.split())
print(c)
print(c.most_common())
print(c.most_common(1))
