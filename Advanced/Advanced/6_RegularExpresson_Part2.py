# Regular Expression - Part2
# CHARACTERS
# Character         Description         Example Pattern Code            Example Match
# \d                A Digit             file_\d\d                       file_25
# \w                Alphanumeric        \w-\w\w\w                       A-b_1
# \s                White Space         a\sb\s\c                        a b c
# \D                A non digit         \D\D\D                          ABC
# \W                Non-Alphanumeric    \W\W\W\W\W                    *-+=)
# \S                Non-WhiteSpace      \S\S\S\S                        Yoyo

# Note : Alphanumeric also includes underscore(_)
import re

print("################################## (1 - without pattern applied ) ##########################################")
text = "My phone number is 408-555-1234. call soon!"
match = re.search("408-555-1234",text)
print(match) # re.match object
print(match.span()) #(19, 31)
print(match.start()) #19
print(match.end()) #31
print(match.group()) #408-555-1234

print("################################## (2 - with pattern applied without quantifiers) ##########################################")
text = "Call phone # 765-222-4542"
match = re.search("\d\d\d-\d\d\d-\d\d\d\d",text)
print(match) # re.match object
print(match.span()) #(13, 25)
print(match.start()) #13
print(match.end()) #25
print(match.group()) #765-222-4542

print("################################## (3 - with pattern applied using quantifiers) ##########################################")
# QUANTIFIERS
# Character    Description                                  Example Pattern Code        Example Match
# +            Occurs one or more time                      Version \w-\w+              Version A-b1_1
# {3}          Occurs exactly 3 times                       \D{3}                       abc
# {2,4}        Occurs 2 to 4 times                          \d{2,4}                     123
# {3,}         Occurs 3 or more                             \w{3,}                      anycharacters
# *            Occurs zero or more times                     A*B*C*                     AAACC
# ?            Once or none                                  plurals?                   plural or pularals

text = "Pohone no is 332-645-3442"
match = re.search(r"\d{3}-\d{3}-\d{4}",text)
print(match) # re.match object
print(match.span()) #(13, 25)
print(match.start()) #13
print(match.end()) #25
print(match.group()) #332-645-3442
print("################################## (4 - with pattern applied using quantifiers and grouping with brackets) ##########################################")
text = "Call soon, My phone : 123-321-4432"
phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
results = re.search(phone_pattern,text)
print(results) # re.match object
print(results.span()) #(22, 34)
print(results.start()) #22
print(results.end()) #34
print(results.group(1)) #123
print(results.group(2)) #321
print(results.group(3)) #4432
print(results.group()) #123-321-4432
