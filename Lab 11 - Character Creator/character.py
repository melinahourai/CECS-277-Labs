import abc

class Character(abc.ABC):

    @abc.abstractmethod
    def description(self):
        """Abstract method for a string of character name and items"""
        pass

    @abc.abstractmethod
    def magic_resistance(self):
        """Abstract method for an integer of character magic resistance value"""
        pass

    @abc.abstractmethod
    def strength(self):
        """Abstract method for an integer of character strength value"""
        pass

    def __str__(self):
        """returns a string descrpition of the character, magic resistance, and strength"""
        return f"Name: {self.description()}\nMR: {self.magic_resistance()}\nSTR: {self.strength()}"

