# Date: 3/20/2025
# Group: 2
# Purpose: Create a game where the user must defeat three pokemon to win the game.
import random
import check_input
import fire
import water
import grass


def main():
    pokemon_options = [fire.Fire(), water.Water(), grass.Grass()] # Creates the list of three randomly chosen...
                                                                  # pokemon objects.

    print("PROF OAK: Hello Trainer! Today\nyou're off to fight your first\nbattle of 1 vs. 3 pokemon.")
    i = 1
    for i in range(len(pokemon_options)):
        print(f"{i + 1}. {pokemon_options[i]}")

    print(f"Select the pokemon that you will battle with.")
    print("1. I choose you, Charmander.\n2. Squirtle! GO!\n3. We can do it together, Bulbasaur!")
    choice = check_input.get_int_range("Please choose a pokemon: ", 1, 3) # Validates user input for menu choices
    user_pokemon = [fire.Fire("Charmander"), water.Water("Squirtle"), grass.Grass("Bulbasaur")][choice - 1]
    print("\n-- TRAINER BATTLE -- ")
    op = random.choice(pokemon_options)

    while user_pokemon.hp > 0: # While the user's pokemon still has hp, then initializes battle until otherwise.
        print(f"TRAINER: I choose you:")
        print(f"{op}\n")

        # Displays the pokemon that the user has chosen to battle with from the menu.
        if choice == 1:
            print(user_pokemon)
        elif choice == 2:
            print(user_pokemon)
        elif choice == 3:
            print(user_pokemon)

        attack_type = check_input.get_int_range(f"Choose an Attack Type:\n1. Normal\n2. Special\nEnter Attack Type: ",
                                                    1, 2) # Validates user input for menu choices
        if attack_type == 1: # If user chooses normal attack, program displays normal attack types of specific...
                             # pokemon and validates user input.
            normal_move = check_input.get_int_range(f"{user_pokemon.get_normal_menu()}\nEnter move: ", 1, 2)
            print(f"\n{user_pokemon.attack(op,1,normal_move)}")
        else: # If user chooses special attack, program displays special attack types of specific...
              # pokemon and validates user input.
            special_move = check_input.get_int_range(f"{user_pokemon.get_special_menu()}\nEnter move: ", 1, 2)
            print(f"\n{user_pokemon.attack(op,2,special_move)}")

        if op.hp == 0: # If the Trainer's pokemon reaches 0 hp, then the defeated pokemon is removed from the list...
                       # and another opponent pokemon is chosen for battle.
            pokemon_options.remove(op)
            print("TRAINER: NOOOOO! You defeated my pokemon!")
            op = random.choice(pokemon_options)
        else: # Displays the damage the opponent pokemon has dealt to the user's pokemon, with the type of attack and move.
            print(op.attack(opponent=user_pokemon, type=random.randint(1, 2), move=random.randint(1, 2)))



        if user_pokemon.hp <= 0: # If the user's pokemon is less than or equal to 0, then the program ends...
                                 # breaks out of the while loop.
            print("Oh no! Your pokemon fainted!")
            print("TRAINER: HA! I defeated you, come back when you get a better pokemon...")
            break

        if len(pokemon_options) == 0: # If all the Trainer's pokemon have been defeated and removed, then the program...
                                      # ends and breaks out of the while loop.
            print("Congrats! You defeated all the pokemon!")
            break

main()
