from collections import Counter, defaultdict

print("######################################## (1) ############################################")
my_list = [1, 1, 1, 2, 3, 2, 3, 4, 5, 5, 6, 4, 5, 2, 3, 4, 5]
c = Counter(my_list)
print(c)
print(c.most_common())  # It will rerun as a list of tuples with most common
print(c.most_common(2))

print(type(c))
for x, y in c.items():
    print(x, y)

l = c.most_common()
print(l)
for a, b in l:
    print(a, b)

print("######################################## (2) ############################################")
my_list = ['a', 'b', 'c', 2, 3, 2, 3, 4, 'a', 'b', 'c', 5, 5, 6, 4, 5, 2, 'a', 'b', 'c', 3, 4, 5]
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
print("######################################## (4 - default dictionary ) ############################################")
d = {'a': 1, 'b': 2, 'c': 3}
print(d)
print(d['a'])
d.popitem()
print(d)
# print(d['wrongkey']) # This will give Key Error

# We can avoid the above error using the default dictionary
d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['correct'])  # 100
print(d['wrongkey'])  # 0 . This will return 0 not the key error

print("######################################## (5 - Named Tuple ) ############################################")
mytuple = (10, 20, 30)
print(mytuple[0])

from collections import namedtuple
Dog = namedtuple('Dog', {'age', 'breed', 'name'})
Sammy = Dog(age=5, breed='Husky', name='Sam')

print(Sammy.age)
print(Sammy.breed)
print(Sammy.name)
