#Problem-1
# Write a function that computes the volume of a sphere given it's radis
print("########################### (Problem-1-Approach-1)#######################################")
import math
def volme_sphere(r):
    return (4/3)*(math.pi)*(r**3)

print(volme_sphere(2))

#Problem-2
print("########################### (Problem-2-Approach-1)#######################################")
# Write a function that checks whether a number is in given range(inclusive of high and low)
def ran_check(num,low,high):
    for i in range(low,high+1):
        if i == num :
            return True
    return False

print(ran_check(5,2,7))

print("########################### (Problem-2-Approach-2)#######################################")
def ran_check1(num,low,high):
    if num in range(low,high+1):
        return True
    else:
        return False
print(ran_check1(5,2,7))

print("########################### (Problem-3-Approach-1)#######################################")
#Problem-3
# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters
# Input: 'Hello Mr.Ramana, How are you?'
# o/p : No Of Upper : 4
# No Of Lower : 18

def check_countof_upperandlower(my_string):
    upper_count = 0
    lower_count = 0
    for x in my_string:
        if x.isupper():
            upper_count =upper_count+1
        elif x.islower():
            lower_count = lower_count + 1
        else:
            continue
    print(f"No of lower case letters: {lower_count}")
    print(f"No of upper case letters: {upper_count}")

s = 'Hello Mr.Ramana, How are you?'
check_countof_upperandlower(s)
print("#####################################################")
s = 'Hello Mr.Rogers, how are you this fine Tuesday?'
check_countof_upperandlower(s)

print("########################### (Problem-4)#######################################")
#Problem-4
# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Input : [1,1,1,1,2,2,3,3,3,3,4,5]
# O/P : [1,2,3,4,5]

def unique_list(my_list):
    return list(set(my_list))

l = [1,1,1,1,2,2,3,3,3,3,4,5]
print(unique_list(l))

print("########################### (Problem-5)#######################################")
#Problem-5
# Write a python function to multiply all the numbers in a list
# Input : [1,2,3,-4]
# Output : -24

def multiply_all(my_list):
    result = 1
    for x in my_list:
        result =result*x
    return result

l1 = [1,2,3,-4]
print(multiply_all(l1))

print("########################### (Problem-6)#######################################")
#Problem-6
# Write a python function to check a word is palindrom or not
# Input : madam,kayak,
# Output : True

def palindrome_check(my_string):
    reversed_string = my_string[::-1]
    if reversed_string == my_string :
        return True
    else:
        return False

print(palindrome_check('madam'))
print(palindrome_check('kayak'))



