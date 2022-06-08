# Regular Expression - Part 3 - Additional Regex Syntax
import re
print("################################## (1 - Or symbol(|) ) ##########################################")
results = re.search(r'cat|dog','The dog is here')
print(results)
print(results.span()) #(4, 7)
print(results.start()) #4
print(results.end()) #7
print(results.group()) #dog
print("################################## (2 - Or symbol(|) ) ##########################################")
results = re.search(r'cat|dog','The cat is here')
print(results)
print(results.span()) #(4, 7)
print(results.start()) #4
print(results.end()) #7
print(results.group()) #cat

print("################################## (3 - findall with wildcard chars) ##########################################")
results = re.findall(r'at','The cat in the hat sat there')
print(results) #['at', 'at', 'at']

results = re.findall(r'.at','The cat in the hat sat there')
print(results) # ['cat', 'hat', 'sat']

results = re.findall(r'...at','The cat in the hat went splat')
print(results) # ['e cat', 'e hat', 'splat']


print("################################## (4 - starts-with(^) and ends-with($) ) ##########################################")
results = re.findall(r'^\d','1 is a number') # It will find if the entire text is starts with number
# so returns 1 as the entire text is started with number 1
print(results) #['1']

results = re.findall(r'^\d','The 2 is a number') # It will find if the entire text is starts with number
# so returns empty results as the text is not started with number
print(results) #[]

results = re.findall(r'\d$','1 is a number') # It will find if the entire text is ends with number
# so returns empty results as the entire text is not started with number
print(results) #[]

results = re.findall(r'\d$','The number is: 2') # It will find if the entire text is starts with number
# so returns 2 as the entire text is ends with number 2
print(results) #['2']

print("################################## (5 - Include and Excludes ) ##########################################")
phrase = 'there are 3 numbers 34 inside 5 this sentence'
# Pattern to exclude any digits in the given text
pattern = r'[^\d]'
results = re.findall(pattern,phrase)
print(results) #['t', 'h', 'e', 'r', 'e', ' ', 'a', 'r', 'e', ' ', ' ', 'n', 'u', 'm', 'b', 'e', 'r', 's', ' ', ' ', 'i', 'n', 's', 'i', 'd', 'e', ' ', ' ', 't', 'h', 'i', 's', ' ', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e']

pattern = r'[^\d]+' # Here + helps to get the one or more chars
results = re.findall(pattern,phrase)
print(results) #['there are ', ' numbers ', ' inside ', ' this sentence']

print("################################## (6 - Excluding punctuation ) ##########################################")
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
test_pattern = r'[^!.?]+' # Here + helps to get the one or more chars
results = re.findall(test_pattern,test_phrase)
print(results) #['This is a string', ' But it has punctuation', ' How can we remove it']

print("################################## (7 - Excluding spaces ) ##########################################")
test_pattern = r'[^!.? ]+' # Here + helps to get the one or more chars
results = re.findall(test_pattern,test_phrase)
print(results) #['This', 'is', 'a', 'string', 'But', 'it', 'has', 'punctuation', 'How', 'can', 'we', 'remove', 'it']
print(' '.join(results)) # This is a string But it has punctuation How can we remove it

print("################################## (8 - Includes ) ##########################################")
test_phrase = 'Only find hypen-words in this sentence. But you do not know how long-ish they are'
test_pattern = r'[\w]+'
results = re.findall(test_pattern,test_phrase)
print(results) #['Only', 'find', 'hypen', 'words', 'in', 'this', 'sentence', 'But', 'you', 'do', 'not', 'know', 'how', 'long', 'ish', 'they', 'are']

print("################################## (9 - Includes ) ##########################################")
test_pattern = r'[\w]+-[\w]+'
results = re.findall(test_pattern,test_phrase)
print(results) #['hypen-words', 'long-ish']

print("################################## (10 ) ##########################################")
text_one  = 'Hello, would you like some catfish?'
text_two  = 'Hello, would you like to take catnap?'
text_three  = 'Hello, have you seen this caterpillar?'
print(re.search(r'cat(fish|nap|claw)',text_one)) #catfish
print(re.search(r'cat(fish|nap|claw)',text_two)) #catnap'>
print(re.search(r'cat(fish|nap|claw)',text_three)) #None
print(re.search(r'cat(fish|nap|erpillar)',text_three)) #caterpillar