# To check given strings are valid anagrams or not

str1 = input("Enter string1 : ")
str2 = input("Enter string2 : ")


# Solution-1-a : Using Sorted function
def anargamCheckUsingSort(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        return sorted(str1) == sorted(str2)


print(anargamCheckUsingSort(str1, str2))

# Solution-1-b : Using Sorted function
list1 = []
list2 = []
for x in str1:
    list1.append(x)

for x in str2:
    list2.append(x)

list1 = sorted(list1)
list2 = sorted(list2)
# print(list1)
# print(list2)

s1 = ""
s2 = ""
s1 = s1.join(list1)
s2 = s2.join(list2)
# print(s1)
# print(s2)

print(s1 == s2)

'''
if s1 == s2:
    print("Given strings are valid Anagrams")
else:
    print("Given strings are Not valid Anagrams")
'''


# Solution-2 : Without Using Sorted function

def anargamCheckUsingFreq(str1, str2):
    if len(str1) != len(str2):
        return False

    freq1 = {}
    freq2 = {}

    for ch in str1:
        if ch in freq1:
            freq1[ch] = freq1[ch] + 1
        else:
            freq1[ch] = 1

    for ch in str2:
        if ch in freq2:
            freq2[ch] = freq2[ch] + 1
        else:
            freq2[ch] = 1

    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True


print(anargamCheckUsingFreq(str1, str2))

# Solution-3 : Using Counter in Collections module

from collections import Counter


def anargamCheckUsingCollections(str1, str2):
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)


print(anargamCheckUsingCollections(str1, str2))
