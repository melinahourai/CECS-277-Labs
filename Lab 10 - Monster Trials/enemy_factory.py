import abc

class EnemyFactory(abc.ABC):
    """interface that is a template for all enemy factories"""
    @abc.abstractmethod
    def create_random_enemy(self):
        """abstract method that each concrete factory overrides to create and return enemy objects"""
        pass
