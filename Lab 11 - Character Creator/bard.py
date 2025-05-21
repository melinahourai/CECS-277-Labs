import character

class Bard(character.Character):

    def description(self):
        """Returns a string of bard name and items"""
        return "Barth the Bard"

    def magic_resistance(self):
        """Returns an integer of bard magic resistance value"""
        return 2

    def strength(self):
        """Returns an integer of bard strength value"""
        return 2
