import state_eat
import puppy_state

class StateAsleep(puppy_state.PuppyState):
    """concrete state of when puppy is asleep"""
    def play(self, puppy):
        """returns string description of reaction to attempting play when asleep"""
        return "The puppy is asleep. It doesn't want to play right now."

    def feed(self, puppy):
        """changes puppy state to eat and returns a string description"""
        puppy.change_state(state_eat.StateEat())
        return "The puppy wakes up and comes running to eat."
