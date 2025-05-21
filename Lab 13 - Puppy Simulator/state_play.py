import state_asleep
import puppy_state

class StatePlay(puppy_state.PuppyState):
    """Concrete state of when puppy wants to play."""
    def play(self, puppy):
        """The puppy's reaction to playing according to if it plays too much and changes state."""
        puppy.inc_plays() # increments the amount of times the puppy has played
        if puppy.plays == 3:
            puppy.change_state(state_asleep.StateAsleep()) # if the puppy has played at least 3 times already, it falls asleep
            puppy.reset() # resets the amount of feeds and plays for puppy
            return "You throw the ball again and the puppy excitedly chases it.\nThe puppy played so much it fell asleep!"
        elif puppy.plays < 3: # if the amount of plays the puppy has is less than 3 it can continue to play without sleeping
            return "You throw the ball again and the puppy excitedly chases it."

    def feed(self, puppy):
        """Returns a string description of reaction to attempting to eat while playing."""
        return "The puppy is too busy playing with the ball to eat right now."
