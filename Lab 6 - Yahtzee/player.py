import die

class Player:
    """Represents a player rolling dice to play the game.
    Attributes:
        _dice (list): list of 3 Die objects.
        _points (int): number of points the player has.
    """
    def __init__(self):
        """Constructs and sorts a list of three Die objects and initializes player's points to 0."""
        self._dice = [die.Die(), die.Die(), die.Die()] # Sorts Dice objects in a list
        self._dice.sort()
        self._points = 0 # Initializes player's points to 0

    @property
    def points(self):
        """Returns player's points."""
        return self._points

    def roll_dice(self):
        """Rolls each of the Die objects in the list and sorts the list."""
        for d in self._dice:
            d.roll()
        self._dice.sort()

    def has_pair(self):
        """Returns True if two dice in the list have the same value and increments points by 1."""
        if self._dice[0] == self._dice[1] or self._dice[1] == self._dice[2] or self._dice[2] == self._dice[0]:
            self._points += 1 # Increments player's points by 1
            return True

    def has_three_of_a_kind(self):
        """Returns True if all three dice in the list have the same value and increments points by 3."""
        if self._dice[0] == self._dice[1] and self._dice[1] == self._dice[2]:
            self._points += 3 # Increments player's points by 3
            return True

    def has_series(self):
        """Returns True if the values of each of the dice in the list are in sequence and increments points by 2."""
        if self._dice[2] - self._dice[1] == 1 and self._dice[1] - self._dice[0] == 1:
            self._points += 2 # Increments player's points by 2
            return True
        
    def __str__(self):
        """Returns a string in the format: "D1=2, D2=4, D3=6"."""
        return ("D1="+str(self._dice[0])+" D2="+str(self._dice[1])+" D3="+str(self._dice[2]))
