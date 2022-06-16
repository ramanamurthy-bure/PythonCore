'''
Tic Tac Toe Project Helpful Hints
In this text lecture we will just have a useful guide for helping you complete the project! Sometimes this project can feel overwhelming, like being thrown into the deep end of the pool and told "Now learn to swim!". So to help out with this, here's a guide to help you begin in the right direction!
 (Note, there's lots of ways to accomplish this task, so your code may look completely different than the given solution).
If the hints below still aren't enough, check out the "Walkthrough Workbook" notebook for even more help!
First off, make sure you understand the project scope. What needs to happen?

We need to print a board.
Take in player input.
Place their input on the board.
Check if the game is won,tied, lost, or ongoing.
Repeat c and d until the game has been won or tied.
Ask if players want to play again.
Ok so we got a general idea of what we need to do. Let's break it down by steps. If you're having trouble with the project, come and check this lecture if you ever get stuck.

PROJECT HINTS:

Start by deciding how you will store the player's marker positions (Xs and Os). Let's choose a list,
 where each index corresponds with a number on a keypad, which in turn corresponds with a position
 on the 3 by 3 board.
Create a list called board which will keep track of the player markers.
The list should already be the same length as your intended board.
Create a function that will print a board. Not just the list, but an actual representation of a board!
This can be done with multiple print statements within the function. Think about how you would take
elements from the list and print them out into the board. (You can also clear output in jupyter
notebook with clear_output() . You need to import this, so at the top of a cell copy and paste:
from IPython.display import clear_output
Write a function which takes an input marker string 'X' or "O' and a given number and stores
it to a list at that appendix.
You might have to look up how to take input in python! input()
Play around with input() to make sure you understand it
Write a function that takes in the board and a player marker and checks it theres a win or a tie.
The checking for a win should be a series of a bunch checks, for example:
 (board[7] == board[8] == board[9] == marker) would check the first top row if they all match a player's marker.
Check for a tie (this means nobody won and the board list is full!)
Now begin writing functions that begin game play.
You'll need to write a function which starts combining and calling the
 different functions you've made within it.
For example, a function which asks for a player's move, then updates the board,then checks for a win,
then prints out the board.
How can you keep the game continually going?
Maybe try using a while loop.
Something like, while the board isn't full and nobody's won...
You might want to think about how to use boolean objects as markers of the game's status.
Alright you should have enough now to begin piecing things together!
If you're still stuck, try googling around for "Python Tic Tac Toe" for ideas of how to put all
your pieces and functions together!
Great job and remember, this is a milestone project, so its meant to be challenging!

'''


def display_borad(board):
    print('\n' * 3)
    print("*****************************************")
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("*****************************************")


def place_marker_on_borad(board, marker, position):
    board[position] = marker


def player_input():
    choice = "WRONG"

    while choice.isdigit() == False or int(choice) not in range(1, 10):
        choice = input("Choose a position(1-9): ")
        if choice.isdigit() == False:
            print("Invalid input, please enter valid choice : ")
        else:
            if int(choice) not in range(1, 10):
                print("Please enter valid choice between(0-9) : ")

    return int(choice)


def player_marker():
    marker = ""
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, choose X or O: ')

    marker = marker.upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # Board is Full
    return True


def choice_first():
    import random
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def replay():
    choice = "WRONG"

    while choice not in ['Y', 'N']:
        choice = input('Keep Playing? (Y or N) : ').upper()

        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand, please choose Y or N")

    if choice == 'Y':
        return True
    else:
        return False


print("Welcome to Tic TAC TOE")
while True:
    # Play The Game
    # SET EVERYTHING UP(BOARD, WHOS FIRST, CHOOSE MARKERS X,O
    myboard = [' '] * 10
    player1_marker, player2_marker = player_marker()
    turn = choice_first()
    print(turn + " will go first")

    play_game = input('Ready To Play(Y or N) :').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_borad(myboard)
            position = player_input()
            place_marker_on_borad(myboard, player1_marker, position)

            if win_check(myboard, player1_marker):
                display_borad(myboard)
                print("Player 1 has won!")
                game_on = False
            else:
                if full_board_check(myboard):
                    display_borad(myboard)
                    print("Tie game!")
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_borad(myboard)
            position = player_input()
            place_marker_on_borad(myboard, player2_marker, position)

            if win_check(myboard, player2_marker):
                display_borad(myboard)
                print("Player 2 has won!")
                game_on = False
            else:
                if full_board_check(myboard):
                    display_borad(myboard)
                    print("Tie game!")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
