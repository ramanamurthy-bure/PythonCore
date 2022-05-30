#Problem-1
# Write a python function to check whether a string is pangram or not
# Panagrams are words or sentences containing every letter of the alphabet at least once
# Ex : "The quick brown fox jumps over the lazy dog"
import string


def is_panagram(str1,alphabet=string.ascii_lowercase):
    alphabetset = set(alphabet)

    str1 = str1.replace(' ','')
    str1 = str1.lower()
    str1 = set(str1)

    return str1 == alphabetset

s1 = "The quick brown fox jumps over the lazy dog"
print(is_panagram(s1))