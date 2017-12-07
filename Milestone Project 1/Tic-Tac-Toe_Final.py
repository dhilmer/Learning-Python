#Needed to delay progam so text can be read
import time
#Needed for the clear Function
import os
#Function to clear the board in Windows, Linux and OS X
def clear():
    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X


#Function to display the board, clears each time it is run
def display_board(board):
    clear()
    print("   |   |   ")
    print(" " + str(board[1]) + " | " + str(board[2]) + " | " + str(board[3]) + " ")
    print("___|___|___")
    print("   |   |   ")
    print(" " + str(board[4]) + " | " + str(board[5]) + " | " + str(board[6]) + " ")
    print("___|___|___")
    print("   |   |   ")
    print(" " + str(board[7]) + " | " + str(board[8]) + " | " + str(board[9]) + " ")
    print("   |   |   ")


#Takes player 1 input and assigns their marker as either 'X' or 'O', returns tuple to
# also assign player 2's marker
def player_input():
    marker_choice = input('Player 1: Would you like to be the letter "X" or "O" ? ').upper()
    while marker_choice not in ('X', 'O'):
        marker_choice = input('\nCome on GOON that is not a valid choice.  Please choose the letter "X" or "O".  What is your choice? ').upper()
    if marker_choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


#Takes the board list object, a marker ('X' or 'O'), and a desired
# position (number 1-9) and assigns it to the board
def place_marker(board, marker, position):
    board[position] = marker
    return board



#Takes in a board and a mark ('X' or 'O') and then
# checks to see if that mark has won the game
def win_check(board,mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or #across top
    (board[1] == mark and board[5] == mark and board[9] == mark) or #diagonal
    (board[1] == mark and board[4] == mark and board[7] == mark) or #left side
    (board[2] == mark and board[5] == mark and board[8] == mark) or #middle down
    (board[3] == mark and board[5] == mark and board[7] == mark) or #diagonal
    (board[3] == mark and board[6] == mark and board[9] == mark) or #right side
    (board[4] == mark and board[5] == mark and board[6] == mark) or #across middle
    (board[7] == mark and board[8] == mark and board[9] == mark)) #across bottom


#Use Random module to randomly decide which player goes first
import random
def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'



#Take board and position and return boolean indicating whether the space on the board is availble
def space_check(board, position):
    #check if position is 1-9 else return False
    if board[position] in board[1:10]:
        #If position is not an 'X' or 'O' the space is available so return True
        #Else (if it is and 'X' or 'O' it's unavailable so return False)
        if board[position] not in ('X', 'O'):
            return True
        else:
            return False
    else:
        return False


#Checks if the board is full and returns boolean, True if full otherwise False .
def full_board_check(board):
    for x in board[1:]:
        if x not in ('X', 'O'):
            return False
    return True


# Asks for a player's next position (as a number 1-9) and then uses space_check to
# check if its a free position. If input is not a number 1-9,
# error exception (ValueError if it's a string and IndexError if it's outside of of the range) will
# generate and ask for position again. If it is available, then return the position for later use.
def player_choice(board):
    while True:
        try:
            position = int(input('Where would you like to place your marker? (1-9)'))
            position_check = space_check(board, position)
            if position_check == True:
                return position
            else:
                print("Sorry that's not a valid choice.")
                continue
        except (ValueError, IndexError):
            print("Sorry that's not a valid choice.")
            continue




#Asks the player if they want to play again and returns the boolean True
# if they do want to play again.
def replay():
    play_again = input('\nWould you like to play again? (Yes or No) : ').upper()
    while play_again not in ('YES', 'Y', 'NO', 'N'):
        play_again = input("\nLet's read and follow directions, shall we?\nWould you like to play again? (Yes or No) : ").upper()
    if play_again in ('YES', 'Y'):
        return True
    elif play_again in ('NO', 'N'):
        return False





#Function to play Tic Tac Toe
def play_game():
    print('\nWelcome to Tic Tac Toe!\n')

    while True:
        #Reset/Create the board
        board = ['filler for index 0 (not used)',1,2,3,4,5,6,7,8,9]
        #Define each players marker
        markers_tuple = player_input()
        player_1_marker = markers_tuple[0]
        player_2_marker = markers_tuple[1]
        #Determine who will go first
        turn = choose_first()
        print('\n' + turn + ' will go first!')
        #Pause program for 1 seconds so you can read who goes first
        time.sleep(1)
        #Variable for Game_on, while loop will collapse when False
        game_on = True

        while game_on:
            #Player 1 Turn
            if turn == 'Player 1':
                display_board(board)
                print('\nPlayer 1 you are:',player_1_marker + '\n')
                position = player_choice(board)
                place_marker(board, player_1_marker, position)

                if win_check(board, player_1_marker):
                    display_board(board)
                    print('\nCongratulations, Player 1 has won the game!!!\n')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('\nThe game is a draw!\n')
                        break
                    else:
                        turn = 'Player 2'
            # Player2's turn.
            else:
                display_board(board)
                print('\nPlayer 2 you are:',player_2_marker + '\n')
                position = player_choice(board)
                place_marker(board, player_2_marker, position)

                if win_check(board, player_2_marker):
                    display_board(board)
                    print('\nCongratulations, Player 2 has won the game!!!\n')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('\nThe game is a draw!\n')
                        break
                    else:
                        turn = 'Player 1'
        if not replay():
            print('All Done')
            break
play_game()
