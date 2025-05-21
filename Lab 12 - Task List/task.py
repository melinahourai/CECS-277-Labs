class Task:
    def __init__(self, desc, date, time):
        """Initializes a task with description, date and time."""
        self._desc = desc
        self._date = date
        self._time = time

    @property
    def date(self):
        """The due date of the task."""
        return self._date

    def __str__(self):
        """Returns a string representation of the task information to the user."""
        return f"{self._desc} - Due: {self._date} at {self._time}"

    def __repr__(self):
        """Returns a string used to write the task to the file."""
        return f"{self._desc},{self._date},{self._time}"

    def __lt__(self, other):
        """Compares tasks based on year, month, day, hour, minute, and by the task description...
        in alphabetical order."""
        if self._date.split("/")[2] < other.date.split("/")[2]: # compares the task
            return True
        elif self._date.split("/")[2] > other.date.split("/")[2]:
            return False
        elif self._date.split("/")[0] < other.date.split("/")[0]:
            return True
        elif self._date.split("/")[0] > other.date.split("/")[0]:
            return False
        elif self._date.split("/")[1] < other.date.split("/")[1]:
            return True
        elif self._date.split("/")[1] > other.date.split("/")[1]:
            return False
        elif self._time.split(":")[0] < other._time.split(":")[0]:
            return True
        elif self._time.split(":")[0] > other._time.split(":")[0]:
            return False
        elif self._time.split(":")[1] < other._time.split(":")[1]:
            return True
        elif self._time.split(":")[1] > other._time.split(":")[1]:
            return False
        elif self._desc < other._desc:
            return True
        else:
            return False

        
