import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_list()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

def update_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

window = tk.Tk()
window.title("To-Do List App")

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

add_btn = tk.Button(window, text="Add Task", width=20, command=add_task)
add_btn.pack()

remove_btn = tk.Button(window, text="Remove Selected Task", width=20, command=remove_task)
remove_btn.pack(pady=5)

listbox = tk.Listbox(window, width=50, height=10)
listbox.pack(pady=10)

window.mainloop()
