# Date: 2/6/2025
# Purpose: A program that allows user to play Rock-Paper-Scissors against the computer, keeping score.
import check_input
import random


def weapon_menu():
    ''' Prompts the user to select weapon of choice, validates user weapon selection, 
     displays the weapon menu, prints user weapon selection'''
    print("Choose your weapon:")
    print("R. Rock")
    print("P. Paper")
    print("S. Scissors")
    print("B. Back")

    user_weapon = input("Please enter your choice (R, P, S, B): ")
    while user_weapon.lower() != "r" and user_weapon.lower() != "p" and user_weapon.lower() != "s" and user_weapon.lower() != "b":
        # Validates user input if not upper or lower R, P, S, B then repeatly asks until valid input
        print("Invalid input. Please choose from the following choices.")
        user_weapon = input("Please enter your choice (R, P, S, B): ")
        
    # Assigns the user input to player weapon
    if user_weapon.upper() == "R":
        user_weapon = "Rock"
    elif user_weapon.upper() == "P":
        user_weapon = "Paper"
    elif user_weapon.upper() == "S":
        user_weapon = "Scissors"
    elif user_weapon.upper() == "B":
        return "b"
    print(f'You chose {user_weapon}')
    return user_weapon


def comp_weapon():
    ''' Randomly generates the computer weapon against the user, 
     assigns the weapon options to a randomly generated range of integers from 1 - 3, and returns computer weapon'''
    ai = random.randint(1,3)
    if ai == 1:
        ai = "R"
        ai_weapon = "Rock"
    elif ai == 2:
        ai == "P"
        ai_weapon = "Paper"
    elif ai == 3:
        ai == "S"
        ai_weapon = "Scissors"
    print("Computer chose", ai_weapon) # Displays computer choice
    return ai_weapon


def find_winner(player, comp):
    ''' Compares the weapon options of player and computer and determines winnner
     if player and computer weapon is same then tie'''
    if player == comp:
        print('Tie')
        return 0
    # Player wins if weapon choice overrules computer weapon choice
    elif (player == 'Rock' and comp == 'Scissors') or (player == 'Scissors' and comp == 'Paper') or (
            player == 'Paper' and comp == 'Rock'):
        print('You win!')
        return 1
    # Computer wins if weapon choice overrules player choice if not previous statements
    else:
        print('Computer wins')
        return 2


def display_scores(p, c):
    '''Prints user and computer scores'''
    print(f'Player = {p}')
    print(f'Computer = {c}')


def main():
    # Prints main menu & asks for user choice
    menu = 0
    user_score = 0
    comp_score = 0
    while menu != 3:
        print("RPS Menu:")
        print("1. Play game")
        print("2. Show score")
        print("3. Quit")
        menu = check_input.get_int_range("Please enter your choice (1-3): ", 1, 3) # Validates the user input
        if menu == 1: # As user selects game, prints the weapon options and game
            # Calls and displays functions
            while True:
                player = weapon_menu()
                if player == 'b':
                    break
                else:
                    comp = comp_weapon()
                    winner = find_winner(player, comp)
                    if winner == 1:
                        user_score += 1
                    elif winner == 2:
                        comp_score += 1
        elif menu == 2:
            display_scores(user_score, comp_score)
    print('Final Score: ')
    print(f'Player = {user_score}')
    print(f'Computer = {comp_score}')
    

main()
