import random
import maze

class Ghost:
    """Guardian of maze and chases the player
    Attributes:
        _previous(char) """

    def __init__(self):
        """initializes the previous attribute with a '.'"""
        self.previous = '.'

    def move(self):
        """detects player's location and moves one space towards them but if blocked by a wall then it randomly moves"""
        m = maze.Maze() # accesses maze
        g_pos = m.search_maze('G') # stores ghost location
        p_pos = m.search_maze('P') # stores player location
        gr = g_pos[0] # stores ghost row location
        gc = g_pos[1] # stores ghost column location
        pr = p_pos[0] # stores player row location
        pc = p_pos[1] # stores player column location

        new_gr = gr # creates new variable of ghost row to modify
        new_gc = gc # creates new variable of ghost column to modify

        m.place_char(gr, gc, self.previous) # restores previous character before moving

        # checks to move towards the player if there is no wall
        if gr < pr and not m.is_wall(gr + 1, gc): # moves up
            new_gr = gr + 1
        elif gr > pr and not m.is_wall(gr - 1, gc): # moves down
            new_gr = gr - 1
        elif gc < pc and not m.is_wall(gr, gc + 1): # moves right
            new_gc = gc + 1
        elif gc > pc and not m.is_wall(gr, gc - 1): # moves left
            new_gc = gc - 1

        # randomly chooses a direction to move in and checks for a wall
        else:
            while True:
                choice = random.randint(1, 4)
                if choice == 1 and not m.is_wall(gr + 1, gc): # moves up
                    new_gr = gr + 1
                    break
                elif choice == 2 and not m.is_wall(gr - 1, gc): # moves down
                    new_gr = gr - 1
                    break
                elif choice == 3 and not m.is_wall(gr, gc + 1): # moves right
                    new_gc = gc + 1
                    break
                elif choice == 4 and not m.is_wall(gr, gc - 1): # moves left
                    new_gc = gc - 1
                    break

        # stores ghost previous location
        self.previous = m[new_gr][new_gc]

        # returns True if ghost captures player and false if not
        if m.search_maze('P') == [new_gr, new_gc]:
            m.place_char(new_gr, new_gc, 'G')
            return True
        else:
            m.place_char(new_gr, new_gc, 'G')
            return False

