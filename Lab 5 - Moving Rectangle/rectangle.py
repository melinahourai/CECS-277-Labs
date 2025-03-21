class Rectangle:
    '''Rectangle class has attributes of x,y, width, and height, with methods of __init__, get_coords,
       get_dimensions, and four moves. The methods move based on user input from main, updating x and y coordinates.'''
    def __init__(self, w, h):
        '''Passes in w and h, assigning them to width and height and sets the x and y attributes to 0.'''
        self.width = w
        self.height = h
        self.x = 0
        self.y = 0

    def get_coords(self):
        '''Returns the x and y values as a list pair.'''
        coords = [self.x, self.y]
        return coords

    def get_dimensions(self):
        '''Returns the rectangle's width and height as a pair.'''
        dimensions = [self.width, self.height]
        return dimensions

    def move_up(self):
        '''Moves the rectangle up one row.'''
        self.x -= 1

    def move_down(self):
        '''Moves the rectangle down one row.'''
        self.x += 1

    def move_left(self):
        '''Moves the rectangle left one row.'''
        self.y -= 1

    def move_right(self):
        '''Moves the rectangle right one row.'''
        self.y += 1
