# Objective: Create a program that allows users to add, view, update, and delete tasks from a to-do list.

# Imports
import time
import json

# Class
class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename # JSON filename for saving tasks
        self.tasks = self.load_tasks() # Load tasks from file
    
    # Load tasks
    def load_tasks(self):
        """Load tasks from the JSON file."""
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Start fresh if file is missing or corrupted

    # Save tasks
    def save_tasks(self):
        """Save tasks to the JSON file."""
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)


    # Add task function
    def add_task(self):
        task = input("Enter a task description: ")
        category = input("Enter category (Work, Personal, Urgent, etc.): ")
        due_date = input("Enter due date (YYYY-MM-DD): ")

        new_task = {"task": task, "category": category, "due_date": due_date}
        self.tasks.append(new_task) # Now tasks contain dictionaries
        self.save_tasks()

        print("Task added successfully.")

    # Show all task function
    def show_all_tasks(self):
            """Display all tasks in the list."""
            if not self.tasks:
                print("No tasks recorded.")
            else:
                print("\n~ To-Do List ~")
                for index, task in enumerate(self.tasks, start=1):
                    print(f"{index}. {task['task']} | {task['category']} | {task['due_date']}")

    # Updates a currently living task
    def update_task(self):
        self.tasks[task_num - 1] = new_task
        print(f"Task {task_num} updated successfully.")

    # Removes a chosen task
    def remove_task(self):
            """Remove a task by index."""
            self.show_all_tasks()
            try:
                choice = int(input("Enter task number to remove: ")) - 1
                if 0 <= choice < len(self.tasks):
                    removed_task = self.tasks.pop(choice)
                    self.save_tasks()
                    print(f"Removed task: {removed_task['task']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")


# Main
def main():
    todo_list = ToDoList() # Creates a Todo List object
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo_list.add_task()
        elif choice == "2":
            todo_list.show_all_tasks()
        elif choice == "3":
            todo_list.remove_task()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()




