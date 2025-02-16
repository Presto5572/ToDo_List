import tkinter as tk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager") # Set window title
        self.root.geometry("400x400") # Set window size

        # Create a label widget
        self.label = tk.Label(root, text="Welcome to Your To-Do List", font=("Arial", 14))
        self.label.pack(pady=10)

        # Create an entry box for input
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        # Create a button
        self.button = tk.Button(root, text="Add Task", command=self.add_task)
        self.button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        print(f"Task added: {task}") # This will later be replaced with an actual functional method


if __name__ == "__main__":
    root = tk.Tk() # Create the main window
    app = ToDoApp(root) # Init the app
    root.mainloop() # Start the Tkinter event loop
