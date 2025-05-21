import puppy_state
import state_asleep

class Puppy:
    """the object that the user interacts with
    Attributes:
        _state
        _feeds
        _plays """
    def __init__(self):
        """initializes the state to asleep state, and then initializes the number of feeds and plays"""
        self._state = state_asleep.StateAsleep()
        self._feeds = 0
        self._plays = 0

    @property
    def feeds(self):
        """number of feeds"""
        return self._feeds

    @property
    def plays(self):
        """number of plays"""
        return self._plays

    def change_state(self, new_state):
        """updates the puppy's state to the new state"""
        self._state = new_state

    def throw_ball(self):
        """calls the play method for whichever state the puppy is in"""
        return self._state.play(self)

    def give_food(self):
        """calls the feed method for whichever state the puppy is in"""
        return self._state.feed(self)

    def inc_feeds(self):
        """increments the number of times the puppy has been fed in a row"""
        self._feeds += 1

    def inc_plays(self):
        """increments the number of times the puppy has played in a row"""
        self._plays += 1

    def reset(self):
        """re-initializes the feeds and plays attributes"""
        self._feeds = 0
        self._plays = 0
