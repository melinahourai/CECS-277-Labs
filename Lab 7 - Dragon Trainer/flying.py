import dragon
import random

class FlyingDragon(dragon.Dragon):
    """Represents a flying dragon."""
    def __init__(self, name, hp):
        """Sets name and hp and assigns a default number of swoops."""
        super().__init__(name, hp)
        self._swoop_attacks = 3 # Sets the default number of swoops dragon has to 3


    def special_attack(self,hero):
        """Checks if flying dragon has any swoops left and returns string accordingly."""
        if self._swoop_attacks > 0:
            special_attack = random.randint(5,8) # Randomizes the amount of damage to the hero from 5-8
            hero.take_damage(special_attack)
            self._swoop_attacks -= 1 # Decrements the number of swoops dragon has by 1 if used
            return (f"{self.name} swoops down and attacks you for {special_attack} damage.")
        else:
            return (f"{self.name} tries to swoop down at you but is all out of swoop attacks.")



    def __str__(self):
        """Gets string from entity class and concatenates the number of swoop shots."""
        return (f"{super().__str__()} \nSwoop attacks remaining: {self._swoop_attacks}")
