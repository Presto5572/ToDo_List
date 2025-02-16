# ToDo_List

Summary of Concepts Learned from the To-Do List Project
This project helped you build a To-Do List Manager with increasing complexity, covering key programming concepts in Python, SQL, and GUI development. Here's a summary of the key topics covered:

1. Python Fundamentals & Data Structures
Functions & Methods – Defined reusable functions for task management.
Lists & Tuples – Stored and manipulated tasks efficiently.
Exception Handling (try-except) – Managed user input errors and database operations gracefully.

2. Object-Oriented Programming (OOP)
Classes & Objects – Created a ToDoList class to encapsulate task-related functions.
Instance Methods & Attributes – Stored tasks within a class and updated dynamically.
Encapsulation – Used self to maintain class data integrity.

3. File Handling & Persistence
JSON Storage – Initially saved tasks using json.dump() and loaded them using json.load().
SQLite Database Integration – Migrated data storage to an SQL database.

4. SQL & Database Management
Creating and Managing Tables – Designed a tasks table using SQL.
CRUD Operations (Create, Read, Update, Delete) –
INSERT INTO – Adding tasks to the database.
SELECT * FROM – Retrieving all tasks.
DELETE FROM – Removing tasks by id.
Using Cursors & Connections – Interacted with SQLite databases efficiently.
Tuple Usage in SQL Queries – Prevented SQL errors (DELETE FROM tasks WHERE id = ? needed a tuple: (task_id,)).

5. GUI Development with Tkinter
Tkinter Basics – Created a graphical interface for task management.
Widgets – Used labels, buttons, and listboxes to display tasks.
Event Handling – Linked button clicks to class methods.
This project helped you solidify Python fundamentals, introduce OOP principles, and transition into SQL database management and GUI programming. Now, you’re ready to pivot towards Python for Data Analytics while keeping these skills in your toolkit!

GitHub README for Your Project
Here’s a README file for your GitHub repository:

To-Do List Manager
A simple task management application that allows users to add, view, and remove tasks using Python, SQLite, and Tkinter.

Features:

✅ Add new tasks with categories and due dates

✅ View all tasks stored in a SQLite database

✅ Remove tasks by selecting their unique ID

✅ User-friendly GUI built with Tkinter

Future Improvements
🔹 Implement task priorities
🔹 Add recurring tasks
🔹 Use notifications/reminders
