import decorator

class Shield(decorator.Decorator):

    def description(self):
        """Returns a string of character name and items plus shielded"""
        return "Shielded " + super().description()

    def magic_resistance(self):
        """Returns an integer of character magic resistance value"""
        return super().magic_resistance() + 0

    def strength(self):
        """Returns an integer of character strength value + 2"""
        return super().strength() + 2
