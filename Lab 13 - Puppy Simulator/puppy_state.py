import abc

class PuppyState(abc.ABC):
    """Interface that inherits from ABC, has abstract methods, and feed and play methods."""

    @abc.abstractmethod
    def play(self, puppy):
        """Abstract method for play."""
        pass

    @abc.abstractmethod
    def feed(self, puppy):
        """Abstract method for feed."""
        pass
