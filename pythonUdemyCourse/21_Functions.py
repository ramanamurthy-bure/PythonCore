'''
1. Creating clean repeatable code is a key part of becoming an effective programmer
2. Functions allow us to create blocks of code that can be easily executed many times, without needing to
constantly rewrite the entire block of code
3. Functions will be a huge leap forward in your capabilities as a python programmer
4. This means that the problems you are able to solve can also be a lot harder!
5. It is very important to get practice combining everything you have learned so far( Control Flow, Loops, etc..)
with functions to become an effective programmer

# 1. def keyword
# Creating a function requires a very specific syntax, including the def keyword, correct indentation,
# and proper structure
#########################################################
#syntax:
def name_of_function():
    # Function explanation in doc string
#########################################################
def -> This keyword will tell python that this is a function
name_of_function -> You decide on function name. Notice 'snake casing'
snake casing -> All lowercase with underscores between words
() -> Parenthesis at the end. Later on we can pass in arguments/parameters into the function
: -> Colon indicates an upcoming indented block. Everything indented is then 'inside' the function
#########################################################
-> Typicallly we use return keyword to send back the result of the function, instead of just printing it out.
-> return allows us to assign the output of the function to a new variable
'''


def functWithoutAnyArg():
    print("My name is functWithoutAnyArg")


def functWithoutDeafaultArg(name):  # Here if we are not passing argument , we will get error
    print(f"My name is : {name}")


def functWithDeafaultArg(name="Default"):  # Here if we are not passing argument , we will NOT get error
    print(f"My name is : {name}")


def add_num(num1, num2):
    return num1 + num2


def even_check(number):
    result = number % 2 == 0
    return result  # We can directly write ' retun number%2 == 0 '


def check_evenlist1(mylist):
    for x in mylist:
        if x % 2 == 0:
            return True
        else:
            return False


def check_evenlist2(mylist):
    for x in mylist:
        if x % 2 == 0:
            return True
        else:
            pass
    return False


def check_evenlist_with_comprehension(mylist):
    new_list = [x for x in mylist if x % 2 == 0]
    if len(new_list) > 0:
        return True
    else:
        return False


def get_all_even_num_from_list(mylist):
    new_list = [x for x in mylist if x % 2 == 0]
    return new_list


def getModifiedString(mystring):
    result_string = ''
    for i in range(len(mystring)):
        letter = mystring[i]
        if (i % 2 == 0):
            result_string = result_string + letter.upper()
        else:
            result_string = result_string + letter.lower()
    return result_string


if __name__ == "__main__":
    functWithoutAnyArg()
    functWithoutDeafaultArg("Ramana")
    # functWithoutDeafaultArg() # Will throw error
    functWithDeafaultArg("Murthy")
    functWithDeafaultArg()  # Will NOT throw error. It will use the Default
    sum_result = add_num(3, 4)
    print(f"Sum results: {sum_result}")  # 7

    sum_result = add_num('10', '20')
    print(f"Sum results: {sum_result}")  # 1020 . This will return 1020 as python is dynamivcally typed
    # which means we no need to specify the type of the data unlike other programming languages

    print(even_check(20))  # True
    print(even_check(13))  # False

    l1 = [1, 2, 3, 4]
    print(check_evenlist_with_comprehension(l1))  # True

    l1 = [1, 3]
    print(check_evenlist_with_comprehension(l1))  # False

    l1 = [1, 2, 3, 4]
    print(check_evenlist_with_comprehension(l1))  # True

    l1 = [1, 2, 3]
    print(check_evenlist1(l1))  # False # This will return False as it will execute for only for the 1st element
    print(check_evenlist2(l1))  # True # This will return True as it will execute for all the elements

    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(get_all_even_num_from_list(l1))

    print(getModifiedString("Ramana"))
