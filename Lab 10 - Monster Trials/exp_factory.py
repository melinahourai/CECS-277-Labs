import enemy_factory
import exp_troll
import exp_goblin
import random

class ExpFactory(enemy_factory.EnemyFactory):
    """Creates difficult enemies, extends from enemy factory"""
    def create_random_enemy(self):
        """randomly constructs and returns one of the expert enemies (ExpGoblin or ExpTroll)"""
        enemy_choice = random.randint(1,2) # Randomly constructs one of the expert enemies
        if enemy_choice == 1: # Returns enemy 1
            return exp_troll.ExpTroll()
        else: # Returns enemy 2
            return exp_goblin.ExpGoblin()


