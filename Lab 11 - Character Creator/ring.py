import decorator

class Ring(decorator.Decorator):

    def description(self):
        """Returns a string of character name and items plus ringed"""
        return "Ringed " + super().description()

    def magic_resistance(self):
        """Returns an integer of character magic resistance value + 2"""
        return super().magic_resistance() +2

    def strength(self):
        """Returns an integer of character strength value"""
        return super().strength() + 0
