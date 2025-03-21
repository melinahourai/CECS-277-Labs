import random

class Die:
    """Represents a single Die, Defaults to a 6-sided die.
    Attributes:
        _sides (int): number of sides on the die.
        _value (int): the value of the rolled die.
    """
    def __init__(self, sides=6):
        """Sets the number of sides of the die (default 6)."""
        self._sides = sides
        self._value = self.roll()

    def roll(self):
        """Rolls the die to set the value of the die. Returns that value (random value between 1 - # of sides)."""
        self._value = random.randint(1, self._sides)
        return self._value

    def __str__(self):
        """Returns the string representation of the die."""
        return str(self._value)

    def __lt__(self, other):
        """Compares the two dice to see if the self's value is less than the other's value."""
        return self._value < other._value

    def __eq__(self, other):
        """Compares the two dice to see if the self's value is equal to the other's value."""
        return self._value == other._value

    def __sub__(self, other):
        """Subtracts the two dice values to see if it has an equal difference."""
        return (self._value - other._value)
