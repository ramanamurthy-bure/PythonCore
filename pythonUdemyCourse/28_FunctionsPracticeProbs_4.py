print("########################### (Problem-1 - Approach-1)#######################################")


# Problem-1:
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# spy_game[1,2,4,0,0,7,5] - True
# spy_game[1,0,2,4,0,5,7] - True
# spy_game[1,7,2,0,4,5,0] - False

def spy_game(myarry):
    zeroindex1 = myarry.index(0)
    zeroindex2 = myarry.index(0, zeroindex1)
    sevenindex = myarry.index(7)
    if sevenindex > zeroindex1 and sevenindex > zeroindex2:
        return True
    else:
        return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False

print("########################### (Problem-1 - Approach-2)#######################################")


def spy_game1(myarry):
    code = [0, 0, 7, 'x']
    # [0,7,x]
    # [7,x]
    # [x]
    for num in myarry:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1


print(spy_game1([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game1([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game1([1, 7, 2, 0, 4, 5, 0]))  # False

print("########################### (Problem-2 - Approach-1)#######################################")


# Problem-2:
# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(num):
    if num<2:
        return 0
    primes=[2]
    # Counter going up to the given number
    x = 3
    while x <= num:
        for y in primes: # use the primes list
            if x%y==0:
                x = x+2
                break
        else:
            primes.append(x)
            x = x + 2
    print(primes)
    return len(primes)




count_primes(10)


