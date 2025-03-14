"""Create a program that works as a simple task manager. It must:
1. Allow the user to add tasks to a list.
    - Each task must have a name and a priority (low, medium, or high).
    - Use lists to store the tasks and their priorities
    (you can use a list of lists or two separate lists).
2. Display all registered tasks with their respective priorities.
3. Allow the user to complete a task.
    - When completing, remove the task from the list and show the updated list.
4. If the user tries to complete a task that does not exist, display an error message.
"""


class Task:
    """
    A class to represent a task with a name and priority.

    Attributes
    ----------
    name : str
        The name of the task.
    priority : str
        The priority of the task. Must be one of {"low", "medium", "high"}.
    Methods
    -------
    validate_priority(priority):
        Validates and returns the priority if it is valid, otherwise raises a ValueError.
    """

    VALID_PRIORITIES = {"low", "medium", "high"}

    def __init__(self, name, priority):
        """
        Initialize a new task with a name and priority.
        Args:
            name (str): The name of the task.
            priority (str): The priority level of the task.
        Attributes:
            name (str): The name of the task, stripped of leading and trailing whitespace.
            priority (str): The validated priority level of the task.
        """

        self.name = name.strip()
        self.priority = self.validate_priority(priority)

    @classmethod
    def validate_priority(cls, priority):
        """
        Validates the given priority.
        This method strips any leading or trailing whitespace from the priority,
        converts it to lowercase, and checks if it is in the list of valid priorities.
        If the priority is not valid, a ValueError is raised.
        Args:
            priority (str): The priority to validate.
        Returns:
            str: The validated priority in lowercase.
        Raises:
            ValueError: If the priority is not in the list of valid priorities.
        """
        priority = priority.strip().lower()
        if priority not in cls.VALID_PRIORITIES:
            raise ValueError(
                f"Invalid priority! Use: {', '.join(cls.VALID_PRIORITIES)}"
            )
        return priority


class TaskManager:
    """
    A class to manage tasks with functionalities to add, show, and complete tasks.

    Attributes
    ----------
    task_list : list
        A list to store tasks.
    Methods
    -------
    add_task(task):
        Adds a task to the task list.
    show_tasks():
        Displays all tasks in the task list.
    complete_task(task_name):
        Marks a task as completed and removes it from the task list.
    """

    def __init__(self):
        """
        Initializes a new instance of the class.
        Attributes:
            task_list (list): A list to store tasks.
        """
        self.task_list = []

    def add_task(self, task):
        """
        Adds a task to the task list.
        Parameters:
        task (str): The task to be added to the list.
        Returns:
        None
        """
        self.task_list.append(task)
        print("Task added successfully!")

    def show_tasks(self):
        """
        Display the list of tasks.
        This method prints out all the tasks in the task list. If there are no tasks,
        it prints a message indicating that no tasks are registered. Each task is
        displayed with its name and priority, both capitalized.
        Returns:
            None
        """
        if not self.task_list:
            print("No tasks registered.")
        else:
            for task in self.task_list:
                print(
                    f"- {task.name.capitalize()} (Priority: {task.priority.capitalize()})"
                )

    def complete_task(self, task_name):
        """
        Marks a task as completed by removing it from the task list.

        Args:
            task_name (str): The name of the task to be completed. The task name is
            case-insensitive and leading/trailing whitespace is ignored.
        Returns:
            None
        Prints:
            "Task completed successfully!" if the task is found and removed.
            "This task is not in the list!" if the task is not found in the task list.
        """
        task_name = task_name.strip().lower()
        for task in self.task_list:
            if task.name.lower() == task_name:
                self.task_list.remove(task)
                print("Task completed successfully!")
                break
        else:
            print("This task is not in the list!")


# %%
# Using the programm
my_tasks = TaskManager()

# Adding tasks and priorities
while True:
    task_name = input("\nAdd a task (or type 'EXIT' to finish): ").strip()
    if task_name.lower() == "exit":
        break
    if not task_name:
        print("Invalid item! Please enter a valid item.")
        continue

    while True:
        priority = input("Enter the task priority (low, medium, high): ").strip()
        try:
            create_task = Task(task_name, priority)
            my_tasks.add_task(create_task)
            break
        except ValueError:
            print("Please, enter a valid priority.")

# Show tasks
print("\nTasks on the list:")
my_tasks.show_tasks()

# Completing tasks
task_to_complete = input(
    "\nEnter the task that was completed (or 'EXIT' to skip): "
).strip()
if task_to_complete.lower() != "exit":
    my_tasks.complete_task(task_to_complete)

# Show tasks
print("\nRemaining tasks:")
my_tasks.show_tasks()
