import task
class TaskList:
    def __init__(self):
        """Reads in the list of tasks from the file and stores them in the tasklist...
        ...by opening the file. It reads in each line then constructs the Task object, appending and sorting...
        it to a list."""

        self._tasklist = []

        task_list = open("tasklist.txt", "r") # opens the tasklist file and reads the lines
        for line in task_list:
            (desc, date, time) = line.strip().split(",")
            self._tasklist.append(task.Task(desc, date, time)) # appends the tasklist file to a list
        self._tasklist.sort()

    def add_task(self, desc, date, time):
        """Constructs a new task using the parameters and appends it to the tasklist, sorting the list."""
        self._tasklist.append(task.Task(desc, date, time)) # constructs new task
        self._tasklist.sort() # appends the new task to the tasklist


    def get_current_task(self):
        """Returns the task at the beginning of the list."""
        if self._tasklist == []:
            return "All tasks completed"
        else:
            return self._tasklist[0]

    def mark_complete(self):
        """Removes and returns the current task from the tasklist."""
        if self._tasklist == []:
            return "No tasks to complete"
        else:
            return self._tasklist.pop(0)

    def save_file(self):
        """Writes the contents of the tasklist back to the file using Task's repr method."""
        task_list = open("tasklist.txt", "w")
        for i in self._tasklist:
            task_list.write(f"{repr(i)}\n")


    def __len__(self):
        """Returns the number of tasks in the tasklist."""
        return len(self._tasklist)

    def __iter__(self):
        """Initializes the iterator attribute n and returns self."""
        self._n = 0
        return self

    def __next__(self):
        """Iterate the iterator one position at a time. When the iterator reaches the end of the tasklist, a ...
        StopIteration exception is raised. Otherwise, it returns the Task object at the current position of iterator."""

        if self._n >= len(self._tasklist):
            raise StopIteration
        else:
            current_task = self._tasklist[self._n]
            self._n += 1
            return current_task
