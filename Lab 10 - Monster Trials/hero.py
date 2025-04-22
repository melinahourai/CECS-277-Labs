import entity
import random

class Hero(entity.Entity):
    """the user's character that extends from entity"""
    def __init__(self, name):
        """passes the name and default hp to the superclass's init"""
        super().__init__(name, 25)

    def melee_attack(self,enemy):
        """deals 2D6 damage to the enemy and returns a string description of the attack"""
        damage = random.randint(1,6) + random.randint(1,6) # 2D6 damage
        enemy.take_damage(damage)
        return f"{self.name} slashes a {enemy.name} with a sword for {damage} damage! " # Attack description
        
    def ranged_attack(self,enemy):
        """deals 1D12 damage to the enemy and returns a string description of the attack"""
        damage = random.randint(1, 12) # 1D12 damage
        enemy.take_damage(damage)
        return f"{self.name} pierces a {enemy.name} with an arrow for {damage} damage! " # Attack description
