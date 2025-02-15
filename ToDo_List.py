# Objective: Create a program that allows users to add, view, update, and delete tasks from a to-do list.

# Imports
import time
import sqlite3

# Class
class ToDoList:
    def __init__(self):
        self.init_db() # Call the db setup method when the class is initialized

    # Initializes a db using SQLite
    def init_db(self):
    # Connect to SQLite database (creates file if it doesn't exist)
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()

        # Create 'tasks' table if it doesn't already exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                category TEXT,
                due_date TEXT
            )
        """)

        # Commit and close
        conn.commit()
        conn.close()

    def show_all_tasks(self):
        # Connect to the database
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()

        # Fetch all tasks
        cursor.execute("SELECT id, task, category, due_date FROM tasks")
        tasks = cursor.fetchall() # Get all results

        print(tasks)  # Debugging step: See what’s being retrieved

        # Checks if there are tasks
        if not tasks:
            print("No tasks found.")
        else:
            print("\n~ To-Do List ~")
            for index, (id, task, category, due_date) in enumerate(tasks, start=1):
                print(f"{id}. {task}. - {category} (Due: {due_date})")

        # Close the connection
        conn.close()

    # Add task function
    def add_task(self):
        task = input("Enter a task description: ")
        category = input("Enter category (Work, Personal, Urgent, etc.): ")
        due_date = input("Enter due date (YYYY-MM-DD): ")

        # Connect to the database
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()

            # Correct INSERT statement
        cursor.execute("""
            INSERT INTO tasks (task, category, due_date) 
            VALUES (?, ?, ?)
        """, (task, category, due_date))  # Provide values as a tuple
        
        # Commit and close
        conn.commit()
        conn.close()

        print("Task added successfully")

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




