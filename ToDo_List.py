# Imports


# Objective: Create a program that allows users to add, view, update, and delete tasks from a to-do list.
# Create an empty list to store tasks
tasks = []

# Header
print("-------------")
print(" Action Menu ")
print("-------------")

# Display a menu with options:
def show_menu():
    print("> Add a task\n")
    print("> View tasks\n")
    print("> Update a task\n")
    print("> Delete a task\n")
    print("> Exit the program\n")

show_menu() # Executing the function to show the action menu