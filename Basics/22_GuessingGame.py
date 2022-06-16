def shuffle_list(mylist):
    from random import shuffle
    shuffle(mylist)
    return mylist


def guess_the_ball():
    guessed_index = int(input("Guess the index no(0,1,2 or 3) : "))
    while guessed_index not in [0, 1, 2, 3]:
        guessed_index = int(input("Guess the index no(0,1,2 or 3) : "))
    return guessed_index


def check_guess(mylist, guess_no):
    if mylist[guess_no] == 'O':
        print("Your guess is correct!")
        print(mylist)
    else:
        print("Your guess is wrong!")
        print(mylist)


l1 = ['O', '', '', '']
mixed_list = shuffle_list(l1)
guessed_no = guess_the_ball()
check_guess(mixed_list, guessed_no)
