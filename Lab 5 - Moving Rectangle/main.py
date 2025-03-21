# Paige Moua, Melina Hourai, Leilani Grimaldo
# 2/27/2025
# Group: 1
# Purpose: Create a program that allows the user to move a rectangle around the grid
#          user should input the dimensions of the rectangle in restriction of width/height (1-5)

from rectangle import Rectangle
import check_input

def display_grid(grid):
    '''Passes in the grid and displays the contents of the grid.'''
    for row in grid:
        for item in row:
            print(item, end=' ')
        print()
    print()

def reset_grid(grid):
    '''Passes in the grid and overwrites the contents with all '.'s.'''
    for i in range(20):
        for j in range(20):
            grid[i][j] = '.'

def place_rect(grid, rect):
    '''Passes in the grid and the rectangle at the location of the rectangle (x,y) on the grid
       and overwrites the '.'s with '*'s using the width and height input of the rectangle.'''

    coords = rect.get_coords()
    dimensions = rect.get_dimensions()

    x = coords[0]
    y = coords[1]

    width = dimensions[0]
    height = dimensions[1]

    grid[x][y] = '*'

    for i in range(height):
        for j in range(width):
            grid[x + i][y + j] = '*'


def main():
    # Prompts user for width and height of rectangle
    width = check_input.get_int_range("Enter rectangle width (1-5): ", 1, 5)
    height = check_input.get_int_range("Enter rectangle height (1-5): ", 1,5)
    rect = Rectangle(width, height) # Creates rectangle

    # Creates grid
    grid = []
    for i in range(20):
        row = ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
        grid.append(row)

    # Places user's rectangle on grid
    place_rect(grid, rect)
    display_grid(grid)

    while True:
        # Displays the menu for the user to select from
        print("Enter Direction: ")
        print("1. Up")
        print("2. Down")
        print("3. Left")
        print("4. Right")
        print("5. Quit")

        # Prompts user for selection 1-5, checking input and repeatedly asking until valid
        direction = check_input.get_int_range("", 1, 5)
        # Gets coordinates of rectangle to check bounds
        coords = rect.get_coords()
        dimensions = rect.get_dimensions()
        if direction == 1 and coords[0] > 0: # User chooses "up"
            rect.move_up()
            reset_grid(grid)
            place_rect(grid, rect)
            display_grid(grid)
        elif direction == 2 and coords[0]+dimensions[1] < 20: # User chooses "down"
            rect.move_down()
            reset_grid(grid)
            place_rect(grid, rect)
            display_grid(grid)
        elif direction == 3 and coords[1] > 0: # User chooses "left"
            rect.move_left()
            reset_grid(grid)
            place_rect(grid, rect)
            display_grid(grid)
        elif direction == 4 and coords[1]+dimensions[0] < 20: # User chooses "right"
            rect.move_right()
            reset_grid(grid)
            place_rect(grid, rect)
            display_grid(grid)
        elif direction == 5: # Quits
            break
        else: # When rectangle is out of bounds
            print('You cannot move that way. Choose again.')


main()
