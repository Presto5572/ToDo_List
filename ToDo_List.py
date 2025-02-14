# Objective: Create a program that allows users to add, view, update, and delete tasks from a to-do list.

# Imports
import time

# Create an empty list to store tasks
tasks = [
    "Buy groceries",
    "Finish homework",
    "Call mom",
    "Workout",
    "Read a book"
]

# Header
def show_header():
    print("--------------")
    print("Menu Selection")
    print("--------------")

# Display a menu with options:
def show_menu():
    print("1. Add a task\n")
    print("2. View tasks\n")
    print("3. Update a task\n")
    print("4. Delete a task\n")
    print("5. Complete a task\n")
    print("6. Exit the program\n")

#------------------------
# Add task function
def add_new_task():
    tasks.append(new_task)

# Show all task function
def show_all_tasks():
    if len(tasks) == 0:
        print("There are no tasks that have been recorded in the database.")
    else:
        print("\n~ To-Do List ~")
        print("----------------")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Updates a currently living task
def update_task():
    tasks[task_num - 1] = new_task
    print(f"Task {task_num} updated successfully.")
#-------------------------

show_header() # Executing the function to show the header
show_menu() # Executing the function to show the action menu

while True: # User choosing actions from the menu
    choice = int(input("Choose an option (1-6): "))
    if choice == 1: # Adding
        new_task = input("What would you like to name the task?: ")
        add_new_task()
        print("Adding a new task...\n")
        time.sleep(1)
        print(f"Task added: {new_task}\n") # Confirms that the task was added
    elif choice == 2: # Opening
        print("\nOpening task view...\n")
        time.sleep(1)
        show_all_tasks()
        print("----------------\n")
    elif choice == 3: # Updating
        show_all_tasks()
        if len(tasks) == 0:
            continue # If there are no tasks to show, then go back to menu selection
        try:
            task_num = int(input("Select the task number in which you would like the update: "))

            if 1 <= task_num <= len(tasks):
                new_task = input("Enter the updated task name: ")
                update_task()
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

        print("Updating a task...\n")
    elif choice == 4: # Deleting
        show_all_tasks()
        if len(tasks) == 0:
            continue

        try:
            delete_task = int(input("\nWhat task would you like to delete?: "))
            
            if 1 <= delete_task <= len(tasks):
                removed_task = tasks.pop(delete_task - 1)
                print(f"\nTask '{delete_task}' has been deleted.")
            else:
                print("\nInvalid task number. Please try again.\n")

        except ValueError:
            print("\nInvalid input. Please enter a valid number.\n")      
    elif choice == 5: # Completing
        show_all_tasks()
        if len(tasks) == 0:
            continue
        
        try:
            task_num = int(input("Enter the task number to mark as complete: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1] = tasks[task_num - 1] + ' [✓]'# Puts a checkmark on the completed task
                print(f"\nTask {task_num} marked as complete.\n")
            else:
                print(f"{task_num} is an invalid number. Please try again.\n")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.\n")
    elif choice == 6: # Exiting
        print("Exiting the program...\n")
        break
    else: # Wrong input
    
        print("--------------------------\n")
        print("Wrong input. Choose again.\n")
        show_header()
        show_menu()



