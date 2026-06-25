import tkinter as tk
from tkinter import messagebox

# Add Task
def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

# Delete Task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a task!")

# Main Window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")

title = tk.Label(root, text="TO-DO LIST", font=("Arial", 18, "bold"))
title.pack(pady=10)

task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task,
                    bg="green", fg="white", width=15)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task,
                       bg="red", fg="white", width=15)
delete_btn.pack(pady=5)

listbox = tk.Listbox(root, width=35, height=15, font=("Arial", 12))
listbox.pack(pady=20)

root.mainloop()