import pokemon
import random

class Water(pokemon.Pokemon):
    """Inherits from the Pokemon class and sets the pokemon_type to 1."""
    def __init__(self, name=None):
        """Calls super to set the name and type."""
        water_names = ["Staryu", "Magikarp","Horsea"] # Creates a list of the water type pokemon's names
        if name: # If a name is not provided then a random name is chosen from the list
            name_choice = name
        else:
            name_choice = random.choice(water_names) # Randomly chooses the name of the water type pokemon
        self._water = 1
        super().__init__(name_choice, 1) # Sets the name and type of the pokemon

    def get_special_menu(self):
        """Overrides special menu method from pokemon class."""
        return "Choose a Move:\n1. Water Gun\n2. Bubble Beam"

    def _special_move(self, opponent, move):
        """Overrides special move method from pokemon class."""
        if move == 1:
            return self._water_gun(opponent) # Returns the special move of water gun to the opponent, damaging opponent pokemon
        else:
            return self._bubble_beam(opponent) # Returns the special move of bubble beam to the opponent, damaging opponent pokemon

    def _water_gun(self, opponent):
        """Randomizes damage, finds multiplier based on pokemon type, and returns damage string."""
        damage = random.randint(1, 7) # Randomizes the damage of the pokemon that will be applied to opponent
        multiplier = self._battle_table[self._p_type][opponent._p_type]
        damage = int(damage * multiplier) # Calculates the total integer damage
        opponent._take_damage(damage)
        if multiplier == 0.5:
            effective = "It was not very effective."
        elif multiplier == 2:
            effective = "It was SUPER effective!"
        else:
            effective = '' # When multiplier is neither 0.5 or 2
        return f"{self._name} blasts {opponent._name} with a WATER GUN for {damage} damage!\n{effective}"

    def _bubble_beam(self, opponent):
        """Randomizes damage, finds multiplier based on pokemon type, and returns damage string."""
        damage = random.randint(3, 5) # Randomizes the damage of the pokemon that will be applied to opponent
        multiplier = self._battle_table[self._p_type][opponent._p_type]
        damage = int(damage * multiplier) # Calculates the total integer damage
        opponent._take_damage(damage)
        if multiplier == 0.5:
            effective = "It was not very effective."
        elif multiplier == 2:
            effective = "It was SUPER effective!"
        else:
            effective = '' # When multiplier is neither 0.5 or 2
        return f"{self._name} BEAMS {opponent._name} with BUBBLES for {damage} damage!\n{effective}"
