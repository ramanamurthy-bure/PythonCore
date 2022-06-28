s1 = 'Hello world'
s2 = 'hello World'

print(s1.capitalize()) # Hello world # Capitalizes the first char in the every word
print(s2.capitalize()) # Hello world # Capitalizes the first char in the every word

print(s1.upper()) # HELLO WORLD
print(s1.lower()) # hello world

print(s1.count('o')) #2
print(s1.find('o')) #4

print(s1.center(20)) #    hello World
print(s1.center(20,'z')) #zzzzhello Worldzzzzz

print('hello\thi') #hello	hi

print(s2.isalnum()) # False
print(s2.isalpha()) # False
s1 = 'hello'
print(s1.isspace()) # False


s = 'hiihhihihihhhi'
# split -> Returns list with the all the occurrences
print(s.split('i')) # ['h', '', 'hh', 'h', 'h', 'hhh', '']

# partition -> Returns tuple with the first occurrence
print(s.partition('i')) # ('h', 'i', 'ihhihihihhhi')