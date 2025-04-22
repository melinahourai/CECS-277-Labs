import entity
import random

class BegGoblin(entity.Entity):
    """extends from entity - factory constructs beginner goblin"""
    def __init__(self):
        """gives a default name and randomizes hp"""
        super().__init__("Goblin", random.randint(7,9))

    def melee_attack(self, enemy):
        """randomizes damage and deals the damage to the enemy(the hero) and returns a string describing the attack"""
        damage = random.randint(4, 6) # Beginner goblin damage
        enemy.take_damage(damage)
        return f"{self.name} bites {enemy.name} for {damage} damage! "
