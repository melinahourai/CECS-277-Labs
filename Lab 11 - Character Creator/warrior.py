import character

class Warrior(character.Character):

    def description(self):
        """Returns a string of warrior name and items"""
        return "Harcor the Warrior"

    def magic_resistance(self):
        """Returns an integer of warrior magic resistance value"""
        return 0

    def strength(self):
        """Returns an integer of warrior strength value"""
        return 4
