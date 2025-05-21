import abc
import character

class Decorator(character.Character, abc.ABC):
    def __init__(self, c):
        """sets character attribute to c"""
        self._character = c

    def description(self):
        """Overrides abstract description method and calls on character attribute"""
        return self._character.description()

    def magic_resistance(self):
        """Overrides abstract magic resistance method and calls on character attribute"""
        return self._character.magic_resistance()

    def strength(self):
        """Overrides abstract strength method and calls on character attribute """
        return self._character.strength()
