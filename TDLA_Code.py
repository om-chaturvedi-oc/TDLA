<--CODE-->

import tkinter as tk
from tkinter import messagebox

tasks = []  # List to store tasks

def add_task():
task_name = entry_task.get()
if task_name:
task = {"name": task_name, "completed": False}
tasks.append(task)
listbox_tasks.insert(tk.END, task_name)
entry_task.delete(0, tk.END)
else:
messagebox.showwarning("Empty Task", "Please enter a task name.")

def mark_task_completed():
selected_index = listbox_tasks.curselection()
if selected_index:
task_index = selected_index[0]
tasks[task_index]["completed"] = True
listbox_tasks.itemconfig(task_index, fg="Blue")
else:
messagebox.showwarning("No Task Selected", "Please select a task to mark as completed.")

def remove_task():
selected_index = listbox_tasks.curselection()
if selected_index:
task_index = selected_index[0]
removed_task = tasks.pop(task_index)
listbox_tasks.delete(task_index)
messagebox.showinfo("Task Removed", f"Task '{removed_task['name']}' removed.")
else:
messagebox.showwarning("No Task Selected", "Please select a task to remove.")

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create and configure the task list
listbox_tasks = tk.Listbox(window, width=50)
listbox_tasks.pack(pady=10)

# Create a scrollbar for the task list
scrollbar_tasks = tk.Scrollbar(window)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

# Connect the scrollbar to the task list
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Define the default message
default_message = "Enter a task..."

# Create the task input field
entry_task = tk.Entry(window, width=50)
entry_task.pack(pady=10)

# Set the default message
entry_task.insert(0, default_message)

# Function to clear the default message on entry focus
def clear_default_message(event):
if entry_task.get() == default_message:
entry_task.delete(0, tk.END)

# Bind the entry field to the focus in event
entry_task.bind("<FocusIn>", clear_default_message)

# Create the buttons
button_add_task = tk.Button(window, text="Add Task", command=add_task, bg="light green")
button_add_task.pack(side="left", padx=15, pady=5)

button_mark_completed = tk.Button(window, text="Mark Completed", command=mark_task_completed, bg="yellow")
button_mark_completed.pack(side="left", padx=5, pady=5)

button_remove_task = tk.Button(window, text="Remove Task", command=remove_task, bg="red")
button_remove_task.pack(side="left", padx=15, pady=5)

# Run the main event loop
window.mainloop()
