class Entity:
    """Represents an entity (in this case either hero or dragon)
    Attributes:
        name (string): name of entity.
        max_hp (int): max hp of entity.
        hp (int): remaining hp of entity.
    """

    def __init__(self, name, max_hp=50):
        """Sets the name, max_hp, and hp of the entity."""
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp # Assigns max hp and hp attributes to the max hp value


    @property
    def name(self):
        return self._name # Gets the values of name without setting it


    @property
    def hp(self):
        return self._hp # Gets the values of hp without setting it


    def take_damage(self, dmg):
        """Represents the damage the entity takes."""
        self._hp = int(self._hp - dmg) # Subtracts the dmg value from the entity's hp
        if self._hp < 0: # If hp goes past 0, the hp gets reset back to 0
            self._hp = 0


    def __str__(self):
        """Returns entity name and remaining hp."""
        return f"{self._name}: {self._hp} / {self._max_hp}"
