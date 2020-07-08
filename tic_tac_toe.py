
from random import randint


#################################################################################
# Function name: display_board
# Parameters: board - list type with 10 objects. The variable contains a list of
# characters that should either be an X, O, or a blank based on user input.
# Return: None
# Calls: None
# Description: This function is used to display the tic tac toe board.
# Operation: This function contains consecutive print statements that display
# a tic tac toe board. F strings are used to update user input. Blank spaces are 
# used as place holders.
#################################################################################

def display_board(board):
    print("\t\t|\t\t|")
    print("\t{}\t|\t{}\t|\t{}".format(board[1],board[2],board[3]))
    print("\t\t|\t\t|")
    print("_"*50)
    print("\t\t|\t\t|")
    print("\t{}\t|\t{}\t|\t{}".format(board[4],board[5],board[6]))
    print("\t\t|\t\t|")
    print("_"*50)
    print("\t\t|\t\t|")
    print("\t{}\t|\t{}\t|\t{}".format(board[7],board[8],board[9]))
    print("\t\t|\t\t|")

#################################################################################
# Function name: player_input
# Parameters: wins - dictionary type with 2 objects which have values that are 
# integers.
# Return: player1.upper() - character type that is chosen by the user whether to
# be X or O.
# Calls: play_game, quit_game
# Description: This function is used to determine the markers for the players.
# Operation: This function asks the user whether they want to be X or O. 
# Whichever symbol player 1 chooses, player 2 is assigned the other symbol by
# default. Player 1 can choose to also enter R to reset the game or Q to quit the
# game. Any other entry will result in an error message and loop back. The 
# parameter is used to be passed to the functions play_game to reset the game and
# wins when R is input and to be passed to the function quit_game to determine 
# which player had th emost wins and is the ultimate winner before quitting. 
#################################################################################

def player_input(wins):
    correct = False
    while not correct:
        player1 = input("Player 1: Do you want to be X or O?  ")
        if player1.upper() in ['O','X']:
            correct = True
        elif player1.upper() == 'R':
            correct = True
            play_game(wins)
        elif player1.upper() == 'Q':
            correct = True
            quit_game(wins)
        else:
            print("Error. Invalid Entry.\n")

    return player1.upper()
 
#################################################################################
# Function name: game_over
# Parameters: board, players, wins - The board is a list type with 10 objects that
# are character types for the symbols of the game. The players variable is a list
# type that holds the symbols that represents each player. The wins variable is a 
# dictionary type with 2 objects and is used to count how many wins each player 
# gets.
# Returns: A boolean that insidactes whether or not the game is over based on the
# set conditions
# Calls: None
# Description: This function is used to determine whether or not the game is over
# Operation: This function checks the 8 ways there are to win Tic Tac Toe to 
# see if any of those spots all contain one symbol. If so, it checks to see which
# player has won, prints it and the current scoreboard of wins, and returns True 
# to end the game. If it does not detect that there is a winner but there are no 
# more spots available for another move, it prints that it's a tie, prints the 
# scoreboard, and returns True to end the game. Otherwise, it returns False.
#################################################################################              

def game_over(board, players, wins):
    #There are 8 ways to win Tic Tac Toe
    winning = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win in winning:
        check = set([board[win[0]], board[win[1]], board[win[2]]])
        if check == {'X'} or check == {'O'}:
            if players[0] == check:
                wins['p1']+=1
                print("\nPlayer 1 WINS!!!")
            else:
                wins['p2']+=1
                print("\nPlayer 2 WINS!!!")
            print("Scoreboard:\n\tPlayer 1: {}\n\tPlayer 2: {}\n".format(wins['p1'],wins['p2']))
            return True
    isFull = 0
    for index in range(1,10):
        if board[index] != ' ':
            isFull += 1
    if isFull == 9:
        print("\nIt's a Tie!")
        print("Scoreboard:\n\tPlayer 1: {}\n\tPlayer 2: {}\n".format(wins['p1'],wins['p2']))
        return True

    return False

#################################################################################
# Function Name: quit_game
# Parameters: wins - a dictionary type with 2 objects with integer values that is
# used to keep track of the wins of the players.
# Returns: None
# Calls: None
# Description: This function is used to end the tic tac toe game.
# Operation: When this function is called, the scoreboard is printed and 
# evaluated. The player with more wins is announced as the winner, otherwise it's
# announced that there is a draw. The function then dismisses and exits the 
# program.
#################################################################################

def quit_game(wins):
    print("\n\n\nScoreboard:\n\tPlayer 1: {}\n\tPlayer 2: {}".format(wins['p1'],wins['p2']))
    if wins['p1'] > wins['p2']:
        print("PLAYER 1 WINS THE GAME!")
    elif wins['p1'] < wins['p2']:
        print("PLAYER 2 WINS THE GAME!")
    else:
        print("IT'S A DRAW!")
    print("\nGOODBYE! Play again soon!")
    exit(0)


################################################################################# 
# Function Name: change_marker
# Parameters: marker - a character type used to be given to the board and display
# the moves of the players
# Returns: a character type
# Calls: None
# Description: This function toggles the markers on the tic tac toe board.
# Operation: This is a simple function that returns the opposite symbol every 
# time it is called. if the marker is an X, it changes it to an O. Otherwise, it
# returns an X. This is to indicate turns being taken by the players. It was made 
# into a function as to not be repetive code in the play_game function.
#################################################################################
    
def change_marker(marker):
    if marker == 'X':
        return 'O'
    else:
        return 'X'

#################################################################################
# Function name: play_game
# Parameters: wins - a dictionary type with 2 objects with integer values that is
# used to keep track of the wins of the players.
# Returns: None
# Calls: player_input, display_board, game_over, play_game, quit_game,
# change_marker
# Description: This function executes the Tic Tac Toe game.
# Operation: This function first prompts the user to choose a marker: X or O, and 
# assigns player 2 the marker that player 1 doesnt choose. After everything is 
# initiated, randomly select a player to go first. Initiate a save_position 
# variable for instances where a player wants to undo the last move made. Then
# start the game. While the game is not over (as decided by the game_over 
# function), keep looping between turns. Keep prompting the user to enter a
# position until a valid entry is given. Valid entries include R to reset the
# game, Q to quit the game, U to undo the last move, and an integer from 1 to 9
# to indicate which spot on the board you'd like to place your marker. Once a
# valid entry has been chosen by the player, check to make sure that the 
# chosen position isn't occupied. if so, inform the user and loop back to prompt
# the player to choose a position again. Otherwise, place the player's marker
# in that position and switch to the next player's turn. Once the game is over,
# prompt the user if they'd like to play again and loop until a valid answer is
# given. If yes, call this function again for a new game. If no, call quit_game.
#################################################################################

def play_game(wins):
    player1 = player_input(wins)
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    players = [set(player1), set(player2)]
    board = [' '] * 10
    display_board(board)
    marker = randint(0,10)
    if marker%2 == 0:
        marker = 'X'
    else:
        marker = 'O'
    if marker == player1:
        player = 'Player 1'
    else:
        player = 'Player 2'
    save_position = 0
    while not game_over(board, players, wins):
        valid_entry = False
        while not valid_entry:
            position = input("{} Choose your next position (1-9):  ".format(player))
            if position.upper() == 'R':
                valid_entry = True
                play_game(wins)
            elif position.upper() == 'Q':
                valid_entry = True
                quit_game(wins)
            elif position.upper() == 'U':
                valid_entry = True
                if player == "Player 1":
                    player = "Player 2"
                else:
                    player = "Player 1"
                print("\nGoing back to player {}...\n".format(player))
                board[save_position] = ' '
                display_board(board)
                marker = change_marker(marker)
            elif position not in ['1','2','3','4','5','6','7','8','9']:
                print("Error. Invalid Entry.")
            else:
                valid_entry = True
                position = int(position)          
                if board[position] != ' ':
                    print("That position is occupied.")
                else:
                    save_position = position
                    board[position] = marker
                    display_board(board)
                    marker = change_marker(marker)
                    if player == "Player 1":
                        player = "Player 2"
                    else:
                        player = "Player 1"

    play_again = False
    while not play_again:
        again = input("Would you like to play again?  ")
        if again.lower() == 'yes' or again.lower() == 'y':
            play_again = True
            play_game(wins)
        elif again.lower() == 'no' or again.lower() == 'n':
            play_again = True
            quit_game(wins)
        else:
            print("Error. Invalid Entry.")



#################################################################################
# Main Code
# Description: This code welcomes the user to the game and displays the rules. It
# then prompts the user if they are ready to play and if the user says yes, the 
# game initiates. Otherwise, the code dismisses the user and ends the program. 
# Before the game starts, the wins variable is initialized to 0 for each object
# indicating that neither player has any wins yet.
#################################################################################

print("\t\t\tWelcome to Tic Tac Toe!\n\t+ The player that goes first is chosen at random.")
print("\t+ At any moment during an entry, you can select R to restart or Q to quit.")
print("\t+ If you make a mistake, you can select U to undo the last move made.")
print("\t+ At the end of the game, wins will be calculated.")
print("\t+ The Player with the most wins WIN TIC TAC TOE!")
print("\t\t   HAVE FUN AND LET THE GAMES BEGIN!!!\n\n")
ready = input("Are you ready to play? Enter yes or no:  ")
wins = {'p1':0,'p2':0}
if ready.lower() == 'yes': 
    play_game(wins)
else:
        print("GOODBYE!")
        exit(0)

