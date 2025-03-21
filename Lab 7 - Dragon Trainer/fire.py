import dragon
import random

class FireDragon(dragon.Dragon):
    """Represents a fire dragon."""
    def __init__(self, name, hp):
        """Sets name and hp and assigns number of fire shots."""
        super().__init__(name, hp)
        self._fire_shots = 2 # Sets the default number of fire shots dragon has to 2


    def special_attack(self, hero):
        """Checks if fire dragon has fire shots left and returns a string accordingly."""
        if self._fire_shots > 0:
            special_attack = random.randint(6,9) # Randomizes the amount of damage to the hero from 6-9
            hero.take_damage(special_attack)
            self._fire_shots -= 1 # Decrements the number of fire shots dragon has by 1 if used
            return (f"{self.name} engulfs you in flames for {special_attack} damage!")
        else:
            return(f"{self.name} tries to spit fire at you but is all out of fire shots.")


    def __str__(self):
        """Gets string from entity class and concatenates the number of fire shots."""
        return f"{super().__str__()} \nFire Shots remaining: {self._fire_shots}"
