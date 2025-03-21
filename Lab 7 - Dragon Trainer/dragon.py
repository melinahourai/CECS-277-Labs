import entity
import random

class Dragon(entity.Entity):
    """Represents dragon entity."""
    def basic_attack(self, hero):
        """Randomizes damage of a tail attack to the hero and returns string."""
        tail_attack = random.randint(2, 5) # Deals random amount of damage to hero from 2-5...
                                           # for tail attack
        hero.take_damage(tail_attack)
        return (f"{self.name} smashes you with its tail for {tail_attack} damage!")


    def special_attack(self, hero):
        """Randomizes damage of a claw attack to the hero and returns string."""
        claw_attack = random.randint(3, 7) # Deals random amount of damage to hero from 3-7...
                                           # for claw attack
        hero.take_damage(claw_attack)
        return (f"{self.name} slashes you with its claws for {claw_attack} damage!")
