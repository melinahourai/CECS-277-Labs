# Paige Moua, Melina Hourai, Leilani Grimaldo
# 2/13/2025
# Group 2
# Purpose: Create a program that allows the user to play a game of battleship
#          using input coordinates to locate and destroy enemy ships

import random
import check_input


def display_board(board):
    '''Intializes the board by using operations from the reset board function, passing in the 5 x 5...
        game board and displaying the contents with row and column headings.'''
    print('  1 2 3 4 5')
    row_labels = ['A', 'B', 'C', 'D', 'E'] # Establishes the row heading as letters A-E by assigning to variable
    row_index = 0
    for row in board: # Formats the row labels in the location of row locations/indexes
        print(row_labels[row_index], end=' ')
        for item in row:
            print(item, end=' ')
        print()
        row_index += 1 # Formats by incrementings the location of row

def reset_game():
    '''Resets the game board and randomizes the position of the ship, returning the game board...
        and the solution.'''
    board = []
    for i in range(5):
        row = ['~', '~', '~', '~', '~']
        board.append(row)

    # Randomizes the position of the ships in row and column using randint function
    ship_row = random.randint(0, 3)
    ship_column = random.randint(0, 3)

    solution = []
    for i in range(5):
        row = ['~', '~', '~', '~', '~']
        solution.append(row)

    solution[ship_row][ship_column] = '*'
    solution[ship_row + 1][ship_column] = '*'
    solution[ship_row][ship_column + 1] = '*'
    solution[ship_row + 1][ship_column + 1] = '*'

    return board, solution

def get_row():
    '''Prompts the user to enter a valid input of the rows A-E, validating user input...
        and repeatedly prompting until valid. Returns valid input, the integer location 0-4.'''
    row = input("Enter a Row Letter (A-E): ")
    while row.lower() not in ("a", "b", "c", "d", "e"): # Validates the user input in a while loop...
                                                        # if not upper or lower A-E
        print("Invalid input. Please enter a Row Letter (A-E).")
        row = input("Enter a Row Letter (A-E): ") # Prompts the user for input again if invalid

    # Assigns the letters A-E to the locations of row indexes
    if row.upper() == 'A':
        row = 0
    elif row.upper() == 'B':
        row = 1
    elif row.upper() == 'C':
        row = 2
    elif row.upper() == 'D':
        row = 3
    elif row.upper() == 'E':
        row = 4

    return row

def fire_shot(board, solution, row, col):
    '''Passes in board, solution, row, and col from previous functions. With user input and solution, creates...
        marks on the board if location was a hit or miss. Returns True if hit and False if miss.'''
    if solution[row][col] == '*': # If the user input of board location is a hit, marks board with '*'
        board[row][col] = '*'
        return True
    else: # If user input of board location is a miss, marks the board with an 'x'
        board[row][col] = 'x'
        return False

def main():
    board, solution = reset_game() # Initializes the game board by calling reset_game function, generating a solution
    display_board(board) # Displays the board by calling the display_board function
    user_choice = 0
    hits = 0
    previous_choices = []

    while user_choice != 3:
        # Displays the main menu from the user to choose from
        print("Menu:")
        print("1. Fire Shot")
        print("2. Show Solution")
        print("3. Quit")

        user_choice = check_input.get_int_range("Enter your selection (1-3): ", 1,3) # Validates the user input


        if user_choice == 1: # If user choses to play then prompts user to enter locations of row and columns
            row = get_row()
            col = check_input.get_int_range("Enter a Column Number (1-5): ", 1, 5)
            col = col - 1

            choice = [row, col]

            if choice in previous_choices: # If the user choses a previous location, it initializes board again...
                                           # and loops user back to main menu
                print('You have already chosen that location.')
                display_board(board)

            else:
                previous_choices.append(choice)

                winner = fire_shot(board, solution, row, col)
                display_board(board)
                # Displays if user input was a hit or miss
                if winner == True:
                    print("Hit!")
                else:
                    print("Miss!")
                if winner == True:
                    hits += 1
                    if hits == 4: # If user has 4 hits on ship locations on board then the user has won
                        print('You Won!')
                        board, solution = reset_game()
                        display_board(board)
                        hits = 0
                        previous_choices = []

        elif user_choice == 2: # Displays the solutions and ship locations by calling display_board and reset_game...
                               # function
            display_board(solution)
            board, solution = reset_game()
            display_board(board)
            hits = 0
            previous_choices = []

main()






