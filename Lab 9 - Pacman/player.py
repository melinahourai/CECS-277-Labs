import maze

class Player:
    def move(self, direction):
        """Moves the player and checks for a wall. Returns True if player bumps into ghost."""
        m = maze.Maze() # accesses maze
        pos = m.search_maze('P') #find player's position
        r = pos[0] # player row
        c = pos[1] # player column

        m.place_char(r, c, ' ') # places space in current location to signify player eating dot

        new_r = r # Initializes new row
        new_c = c # Initializes new column

        if direction.lower() == 'w': # Up
            new_r = r - 1
        elif direction.lower() == 's': # Down
            new_r = r + 1
        elif direction.lower() == 'a': # Left
            new_c = c - 1
        elif direction.lower() == 'd': # Right
            new_c = c + 1

        # Check if new position is not a wall
        if not m.is_wall(new_r, new_c):
            # Check if new position is ghost position
            if m.search_maze('G') == [new_r, new_c]:
                m.place_char(new_r, new_c, 'P') # Move player to new position
                return True # Player bumped into ghost
            else:
                m.place_char(new_r, new_c, 'P') # Move player to new position
                return False # Player didn't bump into ghost

        # if new position is a wall
        else:
            m.place_char(r, c, 'P') # player stays at original location and does not move
            return False # Player didn't bump into ghost
