# Problem-1:
# Lesser of two evens: Write a function that returns the lesser of two given numbers if both numbers are
# even, but returns the greater if one or both numbers are odd
print("########################### (Problem-1-Approach-1)#######################################")


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            print(a)
        else:
            print(b)
    else:
        if a > b:
            print(a)
        else:
            print(b)


lesser_of_two_evens(2, 4)
lesser_of_two_evens(2, 5)

print("########################### (Problem-1-Approach-2)#######################################")


def lesser_of_two_evens1(a, b):
    if a % 2 == 0 and b % 2 == 0:
        print(min(a, b))
    else:
        print(max(a, b))


lesser_of_two_evens1(2, 4)
lesser_of_two_evens1(2, 5)

print("########################### (Problem-2)#######################################")


# Problem-2:
# ANIMAL CRACKERS : Write a function takes two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') -> True
# animal_crackers('Crazy Kangaroo') -> False

def animal_crackers(mystring):
    l = mystring.split()
    if l[0][0] == l[1][0]:
        return True
    else:
        return False


print(animal_crackers('Levelheaded Llama'))  # True
print(animal_crackers('Crazy Kangaroo'))  # False

print("########################### (Problem-3-Approach -1)#######################################")


# Problem-3:
# MAKES TWENTY : Given two integers, return True if the sum of the integers is 20 or
# if one of the integers is 20. If not, return False
# makes_twenty(20,10) -> True
# makes_twenty(12,8) -> True
# makes_twenty(2,3) -> False

def makes_twenty(a, b):
    if 20 in (a, b) or a + b == 20:
        return True
    else:
        return False


print(makes_twenty(20, 10))  # True
print(makes_twenty(12, 8))  # True
print(makes_twenty(2, 3))  # False

print("########################### (Problem-3-Approach -2)#######################################")


def makes_twenty1(a, b):
    return (a + b) == 20 or a == 20 or b == 20


print(makes_twenty1(20, 10))  # True
print(makes_twenty1(12, 8))  # True
print(makes_twenty1(2, 3))  # False
