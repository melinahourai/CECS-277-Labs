
# Purpose: Create a game program where the user must defeat three monsters to pass the trials.

import random
import check_input
import hero
import beg_factory
import exp_factory


def main():
    # prints the starting menu
    print("Monster Trials")
    user_name = input("What is your name? ") # asks for user input of name
    print(f"\nYou will face a series of 3 monsters, {user_name}.\nDefeat them all to win.\n")

    h = hero.Hero(user_name) # constructs hero class
    exp = exp_factory.ExpFactory() # constructs the expert factory class
    beg = beg_factory.BegFactory() # constructs the beginner factory class

    # the list of three monsters is generated using beginner and expert factories
    monster_type = [(beg.create_random_enemy()), (beg.create_random_enemy()), (exp.create_random_enemy())]

    while True:
        print("Choose an enemy to attack: ")
        i = 1
        for i in range(len(monster_type)):
            print(f"{i + 1}. {monster_type[i]}")
        enemy_choice = check_input.get_int_range("Enter choice: ", 1, len(monster_type)) # validates user input...
                                                                        # ...between the length of remaining monsters
        if enemy_choice == 1:
            enemy = monster_type[0]
        elif enemy_choice == 2:
            enemy = monster_type[1]
        else:
            enemy = monster_type[2]

        print(f"\n{h}")
        print("1. Sword Attack \n2. Arrow Attack")
        attack_choice = check_input.get_int_range("Enter choice: ", 1, 2) # validates user input between range of 1 - 2

        if attack_choice == 1:
            print(f"\n{h.melee_attack(enemy)}") # Sword attack
        else:
            print(f"\n{h.ranged_attack(enemy)}") # Arrow attack

        if enemy.hp == 0: # If enemy hp reaches 0
            monster_type.remove(enemy) # Removes defeated enemy from list
            print(f"You have slain the {enemy.name}\n")
        else:
            print(f"{enemy.melee_attack(h)}\n")

        if h.hp <= 0: # If hero's hp reaches 0 or lower
            print("Oh no! You fainted!")
            print("You failed the trials!")
            print("Game Over!")
            break

        if len(monster_type) == 0: # If no monsters are left
            print("Congratulations! You defeated all three monsters!")
            print("Game Over")
            break



main()
