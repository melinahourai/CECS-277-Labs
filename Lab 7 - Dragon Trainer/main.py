# Group: 2
# Date: 3/13/2025
# Purpose: A game where the user must defeat three dragons to pass the trials.

import dragon
import hero
import fire
import flying
import random
import check_input


def main():
    name = input("What is your name, challenger?\n")
    print(f"Welcome to dragon training, {name}\nYou must defeat 3 dragons.\n")

    h = hero.Hero(name,50)
    # List of dragons, initializing the names and hp.
    dragons = [dragon.Dragon('Deadly Nadder',10), fire.FireDragon('Gronckle',15), flying.FlyingDragon('Timberjack',20)]


    while h.hp >0: # While the hero has hp that is greater than 0, they will be able to continuously attack the dragons
        print(h)
        num = 1
        for i in dragons:
            print(f"{num}. Attack {i}")
            num += 1
        dragon_choice = check_input.get_int_range("Choose a dragon to attack: ", 1, len(dragons))
        dragon_choice = dragon_choice-1

        print("Attack with:\n1. Arrow\n2. Sword")
        weapon_choice = check_input.get_int_range("Enter weapon: ", 1, 2)
        # If weapon choice is 1, uses arrow attack
        if weapon_choice == 1:
            print(h.arrow_attack(dragons[dragon_choice]))
        # If weapon choice is 2, uses sword attack
        elif weapon_choice == 2:
            print(h.sword_attack(dragons[dragon_choice]))

        # If dragon dies after hero's attack, print dragon's defeat statement and removes it from dragon_choice
        if dragons[dragon_choice]._hp == 0:
            print(f"You defeated {dragons[dragon_choice]._name}!")
            dragons.pop(dragon_choice)

        if len(dragons) == 0: # If there are no remaining dragons for hero to defeat, breaks out of loop
            break
        
        #Randomly chooses a surviving dragon
        surviving_dragon = random.choice(dragons)
        #Chooses between a basic and special attack
        random_attack = random.randint(1, 2)
        if random_attack == 1:
            print(surviving_dragon.basic_attack(h))
        else:
            print(surviving_dragon.special_attack(h))

    if len(dragons) == 0: # If hero defeats all remaining dragons, prints victory message.
        print("Congratulations! You have defeated all 3 dragons, you have passed the trials.")
    else: # If hero manages to lose and dies to dragons, prints losing message.
        print("You have died. Game over.")

main()
