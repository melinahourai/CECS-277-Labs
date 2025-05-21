
# Purpose: Allow the user to build a character that will fight against three different monsters...
# ...using the Decorator pattern. There will be three trials for the user to face, user wins if passes two out of three.

import random
import check_input
import bard
import wizard
import warrior
import ring
import shield
import cloak

def main():
    print("Character Maker!")
    print("Choose a starting character:\n1. Bard\n2. Warrior\n3. Wizard")
    start_char = check_input.get_int_range(">", 1, 3) #Gets user selection for starting character

    #Checks which character the user chose, creates it, and prints it
    if start_char == 1:
        start_char = bard.Bard()
    elif start_char == 2:
        start_char = warrior.Warrior()
    else:
        start_char = wizard.Wizard()
    print(f"\n{start_char}")

    # creates a list of possible decorator items for the user to choose from
    possible_items = ["Sturdy Shield", "Magic Ring", "Protective Cloak"]

    # loops twice so that the user can choose two items
    for i in range(len(possible_items) - 1):
        if len(possible_items) == 3: # If there are 3 possible items
            print(f"Choose 2 items:\n1. {possible_items[0]}\n2. {possible_items[1]}\n3. {possible_items[2]}")
        else: # If there are 2 possible items
            print(f"Choose 1 item:\n1. {possible_items[0]}\n2. {possible_items[1]}")

        select_item = check_input.get_int_range(">", 1, len(possible_items)) # gets user selection for item

        # checks which item the user chose and modifies the character accordingly
        if possible_items[select_item - 1] == "Sturdy Shield":
            new_char = shield.Shield(start_char)
        elif possible_items[select_item - 1] == "Magic Ring":
            new_char = ring.Ring(start_char)
        else:
            new_char = cloak.Cloak(start_char)

        possible_items.remove(possible_items[select_item - 1]) # Removes chosen item from list

        # prints the modified character and sets the new character as starting character to add another item
        print(f"\n{new_char}")
        start_char = new_char

    # List of monsters is made with magic and strength
    monsters = [["Spiked Dragon", 0, 6], ["Orc Warlord", 1, 5], ["Shadow Knight", 2, 4], ["Lava Monster", 3, 3],
                ["Fiendish Ghoul", 4, 2], ["Goblin Mage", 5, 1], ["Dark Magician", 6, 0]]

    print("\nYou must pass two of the following three trials!")

    # sets total trials for loop, sets trials won to zero, and trials done to zero
    total_trials = 3
    trials_won = 0
    trials = 0

    # loops for each trial
    while trials < total_trials:
        # randomly selects 3 monsters for the user to defeat
        rand_mon = random.randint(0, len(monsters) - 1)
        monster_name = monsters[rand_mon][0] # finds monster name
        monster_resist = monsters[rand_mon][1] # finds monster magic resistance
        monster_str = monsters[rand_mon][2] # finds monster strength

        print(f"\nTrial {trials + 1} of {total_trials}: ")
        print(f"You encounter a {monster_name}")
        print(f"MR: {monster_resist}")
        print(f"STR: {monster_str}")
        print("Fight:\n1. Battle\n2. Dodge")
        move = check_input.get_int_range(">", 1, 2) # gets user selection for move

        if move == 1: # If battle is chosen
            # only if both user's magic resistance and strength is higher or equal to monster's
            if new_char.magic_resistance() >= monster_resist and new_char.strength() >= monster_str:
                print(f"You battle with the {monster_name} and easily defeat it.\nYou have passed this trial.")
                trials_won += 1 # increments the trials won by 1
            else: # Unsuccessful run
                print(f"You battle with the {monster_name} and you are defeated.\nYou have failed this trial.")
            trials += 1 # increments the trials by 1 due to loss
        else: # If dodge is chosen
            # 25% chance that dodging works and user wins
            win_chance = random.randint(1, 4)
            if win_chance == 1:
                print(f"You dodge the {monster_name} successfully.\nYou have passed this trial.")
                trials_won += 1 # increments the trials won by 1
            else: # Unsuccessful run
                print(f"You attempt to dodge the {monster_name}, but it manages to hit you.\nYou have failed this trial.")
            trials += 1 # increments the trials by 1 due to loss

        if trials == 2 and trials_won == 0 or trials == 3 and trials_won < 2:
            # at the end, if trials is more than the trials won then user has lost the game
            print("\nYou failed too many trials.\nYou have lost...")
            break

        # if user only wins 2 out of 3 trials
        elif trials == 3 and trials_won == 2:
            print("\nYou have passed the trials!\nYou win....barely.")
            break

        # if user wins all three trials
        elif trials == 3 and trials_won == 3:
            print("\nYou have passed all trials! Congratulations! You win!")
            break


main()
