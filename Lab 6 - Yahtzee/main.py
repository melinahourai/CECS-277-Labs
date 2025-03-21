# Group: 2
# Date: 3/6/2025
# Purpose: Create a dice game that awards the user points for a pair, three-of-a-kind, or a series.

import player
import check_input

def take_turn(user):
    """Rolls player's dice, displays the dice, checks for and displays any win types, and displays the updated score."""
    user.roll_dice()
    print(user)
    if user.has_three_of_a_kind(): # Numbers are all the same
        print("You got 3 of a kind!")
    elif user.has_series(): # Numbers are in a sequence
        print("You got a series of 3!")
    elif user.has_pair(): # 2 of the numbers are the same
        print("You got a pair!")
    else: 
        print("Aww. Too Bad.")
    print(f'Score = {user.points}') # Displays updated player score

def main():
    print("-Yahtzee-")
    user = player.Player()
    while True:
        take_turn(user) # Gets user's turn
        prompt = check_input.get_yes_no("Play again? (Y/N): ") # Checks for valid input from user if they want to...
                                                               # ...play again.
        print()
        if not prompt:
            break # Stops the game
    print(f"Game over.\nFinal Score = {user.points}") # Prints final score

    
main()
