import pokemon
import random

class Fire(pokemon.Pokemon):
    """Inherits from the Pokemon class and sets the pokemon_type to 0."""
    def __init__(self, name=None):
        """Calls super to set the name and type."""
        fire_names = ["Ponyta", "Growlithe", "Vulpix"] # Creates a list of the fire type pokemon's names
        if name: # If a name is not provided then a random name is chosen from the list
            name_choice = name
        else:
            name_choice = random.choice(fire_names) # Randomly chooses the name of the fire type pokemon
        self._fire = 0
        super().__init__(name_choice, 0) # Sets the name and type of the pokemon


    def get_special_menu(self):
        """Overrides special menu method from pokemon class."""
        return "Choose a Move:\n1. Ember\n2. Fire Blast"

    def _special_move(self, opponent, move):
        """Overrides special move method from pokemon class."""
        if move == 1:
            return self._ember(opponent) # Returns the special move of ember to the opponent, damaging opponent pokemon
        else:
            return self._fire_blast(opponent) # Returns the special move of blast to the opponent, damaging opponent...
                                              # pokemon

    def _ember(self, opponent):
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
        return f"{self._name} BLOWS EMBERS at {opponent._name} for {damage} damage!\n{effective}"

    def _fire_blast(self, opponent):
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
        return f"{self._name} BLASTS {opponent._name} with FIRE for {damage} damage!\n{effective}"
