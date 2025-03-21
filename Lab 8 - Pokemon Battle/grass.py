import pokemon
import random

class Grass(pokemon.Pokemon):
    """Inherits from the Pokemon class and sets the poke_type to 2."""
    def __init__(self, name=None):
        """Calls super to set the name and type."""
        grass_names = ["Oddish", "Bellsprout", "Exeggcute"] # Creates a list of the grass type pokemon's names
        if name: # If a name is not provided then a random name is chosen from the list
            name_choice = name
        else:
            name_choice = random.choice(grass_names) # Randomly chooses the name of the grass type pokemon
        self._grass = 2
        super().__init__(name_choice, 2) # Sets the name and type of the pokemon

    def get_special_menu(self):
        """Overrides special menu method from pokemon class."""
        return "Choose a Move:\n1. Razor Leaf\n2. Solar Beam"

    def _special_move(self, opponent, move):
        """Overrides special move method from pokemon class."""
        if move == 1:
            return self._razor_leaf(opponent) # Returns the special move of razor leaf to the opponent, damaging opponent pokemon
        else:
            return self._solar_beam(opponent) # Returns the special move of solar beam to the opponent, damaging opponent pokemon

    def _razor_leaf(self, opponent):
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
        return f"{self._name} slices {opponent._name} with a RAZOR for {damage} damage!\n{effective}"


    def _solar_beam(self, opponent):
        """Randomizes damage, finds multiplier based on pokemon type, and returns damage string."""
        damage = random.randint(2, 6) # Randomizes the damage of the pokemon that will be applied to opponent
        multiplier = self._battle_table[self._p_type][opponent._p_type]
        damage = int(damage * multiplier) # Calculates the total integer damage
        opponent._take_damage(damage)
        if multiplier == 0.5:
            effective = "It was not very effective."
        elif multiplier == 2:
            effective = "It was SUPER effective!"
        else:
            effective = '' # When multiplier is neither 0.5 or 2
        return f"{self._name} BEAMS {opponent._name} with SOLAR RAYS for {damage} damage!\n{effective}"
