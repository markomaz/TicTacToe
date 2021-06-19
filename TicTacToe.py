from sys import exit
import os

COURSOR_UP = "\x1b[1A"
DELETE_LINE = "\x1b[2K"

field = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]]

occupied = []

character_mapping = {1 : "X", 2 : "O"}

def show_field():
    os.system("cls")

    print " {} | {} | {} ".format(field[0][0], field[0][1], field[0][2])
    print "---|---|---"
    print " {} | {} | {} ".format(field[1][0], field[1][1], field[1][2])
    print "---|---|---"
    print " {} | {} | {} ".format(field[2][0], field[2][1], field[2][2])

def show_prompt(player):
    if player == 1:
        print "Player 1 (\"X\"), choose a field: ",
    elif player == 2:
        print "Player 2 (\"O\"), choose a field: ",
    else:
        print "Invalid player number for <show_prompt> function!"
        exit(1)

def valid_input(args):
    if len(args) != 2:
        return False

    return args[0].isdigit() and args[1].isdigit()

def valid_range(args):
    return args[0] >= 0 and args[0] < 3 and \
           args[1] >= 0 and args[1] < 3

def give_message(message):
    print (COURSOR_UP + DELETE_LINE) * 2 + COURSOR_UP
    print "--{}".format(message)
    
def get_choice(player):
    show_field()
    print "\n\n"
    
    while True:
        show_prompt(player)
        choice = raw_input().split()

        if not valid_input(choice):
            give_message("Enter two indices (numbers)!")
            continue
        
        choice[0] = int(choice[0])
        choice[1] = int(choice[1])

        if not valid_range(choice):
            give_message("Indices are 0,1 or 2")
            continue

        if (choice[0], choice[1]) in occupied:
            give_message("Choose an empty field")
            continue

        break

    return choice    

def check_rows(character):
    for row in field:
        if character*3 == "".join(row):
            return True
    return False

def check_win(character):
    streak = character * 3

    if field[0][0] + field[0][1] + field[0][2] == streak: return True
    if field[1][0] + field[1][1] + field[1][2] == streak: return True
    if field[2][0] + field[2][1] + field[2][2] == streak: return True

    if field[0][0] + field[1][0] + field[2][0] == streak: return True
    if field[0][1] + field[1][1] + field[2][1] == streak: return True
    if field[0][2] + field[1][2] + field[2][2] == streak: return True

    if field[0][0] + field[1][1] + field[2][2] == streak: return True
    if field[0][2] + field[1][1] + field[2][0] == streak: return True

    return False

def give_result(message):
    show_field()
    print "\n\n"

    print ">> {}".format(message)

def play():
    player = 1
    for turns in xrange(1, 10):
        row, column = get_choice(player)
        occupied.append((row, column))

        character = character_mapping[player]
        field[row][column] = character

        if turns > 4:      # It's impossible to win in less then 5 turns!
            win = check_win(character)

            if win:
                give_result("Player {} (\"{}\") wins!!".format(player, character))
                exit(0)

        player = 2 if player == 1 else 1

    give_result("The game is a tie!!")

play()