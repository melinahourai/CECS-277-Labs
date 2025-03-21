import entity
import random

class Hero(entity.Entity):
    """Represents hero entity."""
    def sword_attack(self, dragon):
        """Randomizes damage of a sword attack to a dragon and returns string."""
        sword_dmg = random.randint(1, 6) + random.randint(1, 6) # Deals random amount of damage from 1-6 +  1-6...
                                                                # to dragon because rolled two 6 sided dice
        dragon.take_damage(sword_dmg)
        return f"You slash {dragon.name} with your sword for {sword_dmg} damage."


    def arrow_attack(self, dragon):
        """Randomizes damage of an arrow attack to a dragon and returns string."""
        arrow_dmg = random.randint(1, 12) # Deals random amount of damage from 1-12 to dragon
        dragon.take_damage(arrow_dmg)
        return f"You hit the {dragon.name} with an arrow for {arrow_dmg} damage."
