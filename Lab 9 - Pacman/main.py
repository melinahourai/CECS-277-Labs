# Names: Melina Hourai, Leilani Grimaldo
# Group: 2
# Date: 04/10/25
# Description: A program that allows the user to explore a maze that is guarded by a ghost. The user
# wins if they can eat all the dots in the maze without being captured by the ghost

import maze
import player
import ghost

def main():
    m = maze.Maze() # constructs maze object
    p = player.Player() # constructs player object
    g = ghost.Ghost() # constructs ghost object

    # loops until player either wins or loses
    while True:
        print(m) # Prints maze
        move = input("Move (WASD): ") # Player move input
        while move.lower() not in ['w', 'a', 's', 'd']: # validates user input
            print("Pick a valid move (WASD)")
            move = input("Move (WASD): ")

        check_player = p.move(move) # Moves the player

        if check_player: # If player collided with the ghost
            print(m)
            print("You ran into the ghost. Game over...")
            break

        if m.count_dots() == 0: # If all dots are eaten
            print(m)
            print("All dots eaten. You win! ")
            break

        check_ghost = g.move() # Moves the ghost

        if check_ghost: # If ghost collided with the player
            print(m)
            print("The ghost caught you! Game over...")
            break

main()
        
