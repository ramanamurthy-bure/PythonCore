# Regular Expression - Part1
# We already know we can search for substrings within a larger string with the in operator
# "dog" in "my dog is great" -> True
# This has severe limitations, we need to know the exact string,and need to perform additional operations
# _ to perform additional operations to account for capitalization and punctuation
# What if we only the pattern structure of the string we are looking for? Like an e-mail or phone number?

# Regular Expressions (regex) allow us to search for general patterns in text data!
# For example, a simple e-mail format can be
#    user@email.com
# We know in this case we are looking for a pattern "text"+"@"+"text"+".com"
# The re library allows us to create specialized pattern strings and then search for matches within text
# The primary skill set for regex is understanding the special syntax for these pattern strings
# Phone No : (555)-555-5555
# Regex Pattern -1 : r"(\d\d\d)-\d\d\d-\d\d\d\d"
# Regex Pattern -2 : r"(\d{3}-\d{3}-\d{4}"
# Here r indicates that it is not a normal string and it contains some identifiers within the string
# You will notice that there is a bunch of black slashes which correspond to the individual identifiers
# This series of lecture will first focus on how to use the re library to search for pattern within text
# Afterwards we will focus on understanding the regex syntax codes
print("################################## (1 - Without regular expression ) ##########################################")
text = "The agent's phone number is 408-555-1234. call soon!"
print('phone' in text) # True

print("################################## (2 - with re library) ##########################################")
import re
pattern = 'phone'
print(re.search(pattern,text)) # Match object address
match = re.search(pattern,text)
print(match.span())
print(match.start())
print(match.end())

print("################################## (3 - with re library) ##########################################")
import re
text = 'my phone once,my phone twice'
pattern = 'phone'
print(re.search(pattern,text)) # Match object address
match = re.search(pattern,text) # This will only give first match
print(match.span())
print(match.start())
print(match.end())
print(match.group())

matches = re.findall(pattern,text) # This will only give first match
print(matches)
print(len(matches))

for match in re.finditer(pattern,text):
    print(match)
    print(match.span())
    print(match.start())
    print(match.end())
    print(match.group())






