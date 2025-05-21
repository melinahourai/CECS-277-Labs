
# Purpose: Create a puppy simulator program that allows the user to feed or play with the puppy.

import puppy
import check_input

def main():
    p = puppy.Puppy() # creates a puppy object
    print("Congratulations on your new puppy!") # introduces user to the program

    while True: # loops until user chooses to quit
        # gets user's input for what to do with the puppy and checks input
        choice = check_input.get_int_range("What would you like to do?\n1. Feed the puppy\n2. Play with the puppy\n3. Quit\nEnter choice: ", 1, 3)
        if choice == 1: # if user wants to feed puppy
            print(f"\n{p.give_food()}\n")
        elif choice == 2: # if user wants to play with puppy
            print(f"\n{p.throw_ball()}\n")
        else: # if user wants to quit
            break

main()
