import decorator

class Cloak(decorator.Decorator):

    def description(self):
        """Returns a string of character name and items plus cloaked"""
        return "Cloaked " + super().description()

    def magic_resistance(self):
        """Returns an integer of character magic resistance value + 1"""
        return super().magic_resistance() + 1


    def strength(self):
        """Returns an integer of character strength value + 1"""
        return super().strength() + 1
