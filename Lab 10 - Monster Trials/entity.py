import abc

class Entity(abc.ABC):
    """Abstract class that the monsters and the hero extend from.
    Attributes -
    _name: string of entity name
    _hp: int represents hp of entity
    """
    def __init__(self, name, hp):
        """sets the name and hp attributes"""
        self._name = name
        self._hp = hp

    @property
    def name(self):
        """gets the name of the entity"""
        return self._name # Gets name value

    @property
    def hp(self):
        """gets the hp of the entity"""
        return self._hp # Gets hp value

    def take_damage(self,dmg):
        """deals the damage the entity takes and does not let it go below zero"""
        self._hp -= dmg # Deals damage to hp
        if self._hp <= 0:
            self._hp = 0 # Sets hp to 0 if it is a negative value

    def __str__(self):
        """returns a string with the entity's name and hp"""
        return f"{self._name} HP: {self._hp}"

    @abc.abstractmethod
    def melee_attack(self,enemy): # Attack entity does to another entity
        """abstract method to represent the attack the entity does to another entity"""
        pass
