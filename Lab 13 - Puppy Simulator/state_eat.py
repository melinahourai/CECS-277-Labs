import state_asleep
import state_play
import puppy_state

class StateEat(puppy_state.PuppyState):
    def play(self, puppy):
        """implement the puppy's reaction to playing"""
        puppy.change_state(state_play.StatePlay())
        return "The puppy looks up from its food and chases the ball you threw."

    def feed(self, puppy):
        """implement the puppy's reaction to feeding"""
        puppy.inc_feeds() # Increments amount of times puppy is fed
        if puppy.feeds == 3: # If puppy is fed 3 times
            puppy.change_state(state_asleep.StateAsleep()) # Set to fall asleep
            puppy.reset() # Reset amount of feeds and plays for puppy
            return "The puppy continues to eat as you add another scoop of kibble to its bowl.\nThe puppy ate so much it fell asleep!"
        elif puppy.feeds <3:
            return "The puppy continues to eat as you add another scoop of kibble to its bowl."
