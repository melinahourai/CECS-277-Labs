import abc
import random

class Pokemon(abc.ABC):
    """Represents an abstract pokemon.
    Attributes:
        name(str) – name of the pokemon.
        hp(int) –  hit points of the pokemon.
        p_type(int) - type of pokemon.
    """
    def __init__(self, name, p_type):
        """Sets the name and pokemon type, assigns a 2D list to battle table, and sets hp to 25."""
        self._name = name
        self._p_type = p_type
        self._battle_table = [[1, .5, 2], [2, 1, .5], [.5, 2, 1]] # Assigns the battle table to a 2D list.
        self._hp = 25 # Sets the initial hp of all pokemon to 25

    @property
    # Gets the value of _hp rather than setting by using a decorator
    def hp(self):
        return self._hp

    def get_normal_menu(self):
        """Returns the normal menu."""
        return f"Choose a Move:\n1. Slam\n2. Tackle"

    def _normal_move(self, opponent, move):
        """Calls the normal move based on user choice."""
        if move == 1:
            return self._slam(opponent)
        else:
            return self._tackle(opponent)

    def _slam(self, opponent):
        """Randomizes some damage, calls take_damage on opponent, and returns string"""
        damage = random.randint(2, 6) # Randomizes the damage that the pokemon will deal to the opponent...
                                            # pokemon from 2 - 6 for the slam attack
        opponent._take_damage(damage) # The randomized damage is taken from the hp of the opponent pokemon
        return f"{self._name} SLAMS {opponent._name} for {damage} damage!"

    def _tackle(self, opponent):
        """Randomizes some damage, calls take_damage on opponent, and returns string"""
        damage = random.randint(3, 5) # Randomizes the damage that the pokemon will deal to the opponent...
                                            # pokemon from 3 - 5 for the tackle attack
        opponent._take_damage(damage)
        return f"{self._name} TACKLES {opponent._name} for {damage} damage!"

    @abc.abstractmethod
    def get_special_menu(self):
        """Returns special menu"""
        pass

    @abc.abstractmethod
    def _special_move(self, opponent, move):
        """Calls the special move based on user choice."""
        pass

    def attack(self, opponent, type, move):
        """Uses parameters to choose to call either normal or special move for pokemon type"""
        if type == 1:
            return self._normal_move(opponent, move)

        else:
            return self._special_move(opponent, move)


    def __str__(self):
        """Returns string for hp."""
        return f"{self._name} HP: {self._hp}/25"

    def _take_damage(self, dmg):
        """Represents the damage the pokemon takes."""
        self._hp -= dmg # Decrements the self hp of the pokemon by the damage dealt by the opponent pokemon
        if self._hp <= 0: # If the hp of pokemon is less than or equal to 0, then hp is set back to 0.
            self._hp = 0
