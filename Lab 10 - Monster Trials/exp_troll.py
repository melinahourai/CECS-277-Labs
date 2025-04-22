import entity
import random

class ExpTroll(entity.Entity):
    """Type of monster the factory constructs, extends from entity"""
    def __init__(self):
        """Constructs the expert troll"""
        super().__init__("Horrible Troll", random.randint(15,18))

    def melee_attack(self, enemy):
        """Randomizes attack based on enemy type"""
        damage = random.randint(8, 12) # Expert troll damage
        enemy.take_damage(damage)
        return f"{self.name} slams {enemy.name} for {damage} damage! "
