class Maze:
    """Singleton class that represents maze
    Attributes:
        _grid(char[][]) - grid of the game"""

    _instance = None
    _initialized = False

    def __new__(cls):
        """Creates a maze if it hasn't been constructed and stores it in an instance variable then returns it"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Creates and fills the 2D grid from file contents"""
        if not Maze._initialized:
            file = open('pacman.txt') # Opens maze file
            self.grid = [] # Initializes grid as empty list
            for line in file: #runs through each line in file
                line.strip() # strips new line
                self.grid.append(list(line)) # Converts line to list of characters and adds it to grid
            Maze._initialized = True

    def __getitem__(self, row):
        """Returns specified row from the maze"""
        return self.grid[row] # Returns row at given index

    def is_wall(self, r, c):
        """Returns true if there is a wall"""
        if self.grid[r][c] == '*': # Checks if character at (r, c) is a wall
            return True
        return False

    def place_char(self, r, c, char):
        """Places specified character at specified row and column"""
        self.grid[r][c] = char # Overwrites the character at (r, c) with the given character

    def __str__(self):
        """Returns a string representation of the maze"""
        grid_string = '' # creates empty grid string
        for line in self.grid:
            line_string = '' # Initializes empty string for the current row
            for char in line: # Iterates through each character in row
                line_string += char # adds each character to line string
            grid_string += line_string # adds each line to grid string
        return grid_string # Returns maze as a string

    def search_maze(self, char):
        """Returns coordinates of specified character on maze"""
        for r in range(len(self.grid)): # Iterates through each row
            for c in range(len(self.grid[r])): # Iterates through each column in the row
                if self.grid[r][c] == char:
                    return [r, c] # Returns row and column coordinates
        return [-1, -1] # Returned if character not found

    def count_dots(self):
        """Counts and returns the number of dots"""
        count = 0
        for r in range(len(self.grid)):  # Iterates through each row
            for c in range(len(self.grid[r])):  # Iterates through each column in the row
                if self.grid[r][c] == '.': # Checks if character is a dot
                    count += 1
        return count # Returns total number of dots
