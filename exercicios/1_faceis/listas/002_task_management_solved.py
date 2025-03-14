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

task_list = []

# Adding tasks and priorities
while True:
    task = input("Add a task (or type 'EXIT' to finish): ").capitalize()
    if task == "Exit":
        break
    priority = input("Enter the task priority (low, medium, high): ").capitalize()
    task_list.append([task, priority])

print("\nRegistered tasks:")
for task, priority in task_list:
    print(f"- {task} (Priority: {priority})")

# Completing tasks
complete_task = input("Enter the task that was completed: ").capitalize()
for task in task_list:
    if task[0] == complete_task:
        task_list.remove(task)
        print("Task completed successfully!")
        break
else:
    print("This task is not in the list!")

# Pending tasks
if task_list:
    print("\nPending tasks:")
    for task, priority in task_list:
        print(f"- {task} (Priority: {priority})")
else:
    print("\nAll tasks have been completed. Congratulations!")
