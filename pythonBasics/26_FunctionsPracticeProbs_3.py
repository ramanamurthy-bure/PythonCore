# Problem-1:
# Given  a list of ints, return True if the array contains the 3 next to a 3 somewhere.
# has_33([1,3,3]) -> True
# has_33([1,3,1,3]) -> False
# has_33([3,1,3]) -> False
print("########################### (Problem-1-Approach-1)#######################################")


def has_33(mylist):
    for x in mylist:
        exp_index = mylist.index(3)
        if exp_index >= 0:
            if mylist[exp_index + 1] == 3:
                return True
            else:
                return False


print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False
print(has_33([3, 1, 3]))  # False

print("########################### (Problem-1-Approach-2)#######################################")


def has2_33(mylist):
    for i in range(0, len(mylist) - 1):
        if mylist[i] == 3 and mylist[i + 1] == 3:
            return True
    return False


print(has2_33([1, 3, 3]))  # True
print(has2_33([1, 3, 1, 3]))  # False
print(has2_33([3, 1, 3]))  # False

print("########################### (Problem-1-Approach-3)#######################################")


def has3_33(mylist):
    for i in range(0, len(mylist) - 1):
        if mylist[i:i + 2] == [3, 3]:
            return True
    return False


print(has3_33([1, 3, 3]))  # True
print(has3_33([1, 3, 1, 3]))  # False
print(has3_33([3, 1, 3]))  # False
print("########################### (Problem-2)#######################################")


# Problem-2:
# PAPER DOLL : Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello')->'HHHeeellllllooo'
# paper_doll('Mississippi')->'MMMiiissssssiiissssssiiippppppiii'

def paper_doll(mystring):
    result = ''
    for x in mystring:
        result = result + (x * 3)
    return result


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

print("########################### (Problem-3)#######################################")


# Problem-3:
# BLACKJACK : Given three integers between 1 and 11, if their sum is less than or equal to 21,return their sum.
# if their sum exceeds 21 and there's an eleven,reduce the total sum by 10. Finally,
# if the sum(even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) -> 18
# blackjack(9,9,9) -> 'BUST'
# blackjack(9,9,11) -> 19

def blackjack(a, b, c):
    sumval = a + b + c
    if sumval <= 21:
        return sumval
    elif 11 in (a, b, c) and sumval - 10 <= 21:
        sumval = sumval - 10
        return sumval
    else:
        return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))

print("########################### (Problem-4 - Approach-1)#######################################")


# Problem-4:
# SUMMER OF '69' : Return the sum of the numbers in the array, except ignore sections of numbers starting
# with a 6 and extending to the next 9(every 6 will be followed by at least one 9). Return 0 for no numbers
# summer_69([1,3,5]) --> 9
# summer_69([4,5,6,7,8,9]) --> 9
# summer_69([2,1,6,9,11]) --> 14
# summer_69([2,1,6,11,9]) --> 14

def summer_69(mylist):
    result = 0
    for x in mylist:
        if x not in range(6, 10):
            result = result + x
    return result


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
print(summer_69([2, 1, 6, 11, 9]))

print("########################### (Problem-4 - Approach-2)#######################################")


def summer1_69(mylist):
    total = 0
    add = True
    for num in mylist:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


print(summer1_69([1, 3, 5]))
print(summer1_69([4, 5, 6, 7, 8, 9]))
print(summer1_69([2, 1, 6, 9, 11]))
print(summer1_69([2, 1, 6, 11, 9]))
