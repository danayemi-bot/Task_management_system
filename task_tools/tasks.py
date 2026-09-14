
# - tasks.py: add, delete, update, complete tasks

def add_tasks():
    ''' Add tasks to the database. '''
    # Initializes an empty list to store tasks collected during this session.
    task_list = []

    try:
        while True:
            # .strip() removes accidental whitespace, and .lower() handles casing when checked below.
            add_task = input("Add task or quit to stop: ").strip()

            # Fixed: Evaluates the cleaned user input directly against "quit".
            if add_task.lower() == "quit":
                break  # Exits the while loop immediately when the user types quit.

            # Checks if input is numbers (e.g., '12') and short, rejecting pure numeric placeholders.
            if add_task.isdigit() and len(add_task) < 3:
                print(f"Please enter a valid task name: {add_task} is not accepted")
                continue  # Skips the rest of the loop and prompts for input again.

            elif add_task == "":
                print("Task list cannot be empty")
                continue  # Re-prompts the user if they submit a blank line.
            else:
                # Fixed: Converted to a proper f-string to output the variable correctly.
                print(f"Task added successfully: {add_task}")

            task_list.append(add_task)  # Adds the validated task string to the tracking list.

        return task_list  # Returns the full collection of tasks once the loop terminates.

    except Exception as err:
        print(f"Error: {err}")


# demo
final_tasks = add_tasks()
if final_tasks:
    print("Tasks added")
    for i, task in enumerate(final_tasks, start=1):
        print(f"{i}. {task.capitalize()}")


# Added parameter name task_list so the function accepts an argument instead of relying on a global variable.
def delete_tasks(task_list):
    ''' Delete tasks from the database. '''
    try:
        while True:
            task_to_delete = input("Enter task to delete or quit to stop: ").strip()
            if task_to_delete.lower() == "quit":
                break

            # Added: A loop-based search mechanism. Because Python lists lack a direct 
            # .lower() method, we iterate through each item to compare strings case-insensitively.
            found_task = None
            for task in task_list:
                if task.lower() == task_to_delete.lower():
                    found_task = task  # Captures the exact original-case task string if a match occurs.
                    break

            if not found_task:
                print(f"The task '{task_to_delete}' does not exist in the database")
            else:
                # Fixed: Removes the exact matched task from the original list instead of appending a nested list.
                task_list.remove(found_task)
                print(f"Task deleted successfully: {found_task}")

        # Fixed: Returns the modified list directly, ensuring safe enumeration later.
        return task_list
    except Exception as err:
        print(f"Error: {err}")


final_remaining_tasks = delete_tasks(final_tasks)
if final_remaining_tasks:
    print("Tasks Remained")
    for i, task in enumerate(final_remaining_tasks, start=1):
        print(f"{i}. {task.capitalize()}")







