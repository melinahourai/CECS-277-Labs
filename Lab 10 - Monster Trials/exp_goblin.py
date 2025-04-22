import entity
import random

class ExpGoblin(entity.Entity):
    """Type of monster the factory constructs, extends from entity"""
    def __init__(self):
        """Constructs the expert goblin"""
        super().__init__("Horrible Goblin", random.randint(12,15))

    def melee_attack(self, enemy):
        """Randomizes attack based on enemy type"""
        damage = random.randint(5,8) # Expert goblin damage
        enemy.take_damage(damage)
        return f"{self.name} slams {enemy.name} for {damage} damage! " # Attack description

