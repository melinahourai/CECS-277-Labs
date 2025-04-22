import entity
import random

class BegTroll(entity.Entity):
    """Class extends from Entity class, constructs the beginner troll monster class."""
    def __init__(self):
        """Using super, gives the troll a default name and randomizes hp."""
        super().__init__("Troll", random.randint(8, 10)) # default name of "Troll" and hp ranging from 8 - 10

    def melee_attack(self, enemy):
        """Randomizes the damage dealt to the hero from the troll monster. Returns a string describing attack."""
        damage = random.randint(5, 9) # randomizes the damage of the attack from 5 - 9
        enemy.take_damage(damage) # the randomized damage is applied to the hero
        return f"{self.name} bites {enemy.name} for {damage} damage! "
