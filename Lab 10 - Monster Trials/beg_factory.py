import enemy_factory
import beg_goblin
import beg_troll
import random

class BegFactory(enemy_factory.EnemyFactory):
    """Class creates easy enemies, extends from EnemyFactory."""
    def create_random_enemy(self):
        """Randomly constructs and returns one of the beginner enemies (BegGoblin or BegTroll)."""
        enemy_choice = random.randint(1,2) # randomly constructed integer
        if enemy_choice == 1:
            return beg_troll.BegTroll() # returns beginner troll
        else:
            return beg_goblin.BegGoblin() # returns beginner goblin

