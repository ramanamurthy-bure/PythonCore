def display_game(game_list):
    print("Here is the game list: ", game_list)
    print(game_list)


def get_position():
    input_val = "WRONG"

    while input_val.isdigit() == False or int(input_val) not in range(0,11):
        input_val = input("Enter a value between(0-2) : ")
        input_val = input_val.strip()
        if input_val.isdigit() == False:
            print("Sorry, You entered invalid input, please retry again!")
        if input_val.isdigit():
            if int(input_val) not in range(0, 2):
                print("Valid inputs range(0-2). Please retry entering valid input ")

    return int(input_val)


def replacement_choice(game_list,position):
    user_placement = input("Type the new string to place at position: ")
    game_list[position] = user_placement
    return game_list


def gameon_choice():
    choice = "WRONG"

    while choice not in ['Y','N']:
        choice  = input('Keep Playing? (Y or N) : ').upper()
        if choice not in ['Y','N']:
            print("Sorry, I don't understand, please choose Y or N")

        if choice=='Y':
            return True
        else:
            return False


gameon = True
game_list = [0, 1, 2]

while gameon:
    display_game(game_list)
    position = get_position()
    replacement_choice(game_list,position)
    display_game(game_list)
    gameon = gameon_choice()
    print("Game over!")
