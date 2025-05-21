import character

class Wizard(character.Character):

    def description(self):
        """Returns a string of wizard name and items"""
        return "Altar the Wizard"

    def magic_resistance(self):
        """Returns an integer of wizard magic resistance value"""
        return 3

    def strength(self):
        """Returns an integer of wizard strength value"""
        return 1
