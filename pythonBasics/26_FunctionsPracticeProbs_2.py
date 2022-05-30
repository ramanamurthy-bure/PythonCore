# Problem-1:
# OLD MACDONALD : Write a function that capitalizes the first and forth letters of a name
# old_macdonold('macdonald') -> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald
print("########################### (Problem-1-Approach-1)#######################################")


def old_macdonold(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
    return first_letter.upper() + inbetween.lower() + fourth_letter.upper() + rest.lower()


print(old_macdonold("macdonald"))
print("########################### (Problem-1-Approach-2)#######################################")


def old_macdonold1(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()


print(old_macdonold1("macdonald"))
print("########################### (Problem-2-Approach-1)#######################################")


# Problem-2:
# MASTER YODA : Given a sentence, return a sentence with the words reserved
# master_yoda('I am home') -> 'home am I'
# master_yoda('We are ready') -> 'ready are We'
def master_yoda(text):
    l = text.split()
    l.reverse()
    result = ''
    for x in l:
        result = result + x + " "
    return result


print(master_yoda('I am home'))
print(master_yoda('We are ready'))
print("########################### (Problem-2-Approach-2)#######################################")


def master_yoda1(text):
    l = text.split()
    result = l[::-1]
    return ' '.join(result)


print(master_yoda1('I am home'))
print(master_yoda1('We are ready'))
print("########################### (Problem-3-Approach-1)#######################################")


# Problem-3:
# ALMOST THERE : Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) -> True
# almost_there(104) -> True
# almost_there(150) -> False
# almost_there(209) -> True
# Note: abs(num) -> Returns the absolute value of number
def almost_there(num):
    if num in range(90, 100) or num in range(100, 110):
        return True
    elif num in range(190, 200) or num in range(200, 210):
        return True
    else:
        return False


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
print("########################### (Problem-3-Approach-2)#######################################")


def almost_there1(num):
    return (abs(100 - num) <= 10) or (abs(200 - num) <= 10)


print(almost_there1(90))
print(almost_there1(104))
print(almost_there1(150))
print(almost_there1(209))
