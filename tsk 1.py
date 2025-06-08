import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, master):
        self.master = master
        master.title("To Do List")
        master.geometry("400x300")
        master.configure(bg="#7CA2D6") 

        self.tasks = []

        self.input_frame = tk.Frame(master)
        self.input_frame.pack(pady=8)

        self.task_entry = tk.Entry(self.input_frame, width=30)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_button = tk.Button(self.input_frame, text="Add", command=self.addtask, width=8)
        self.add_button.grid(row=0, column=1, padx=5)

        self.list_frame = tk.Frame(master)
        self.list_frame.pack(pady=8)

        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox = tk.Listbox(self.list_frame, width=40, height=10, yscrollcommand=self.scrollbar.set)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.action_frame = tk.Frame(master)
        self.action_frame.pack(pady=5)

        self.complete_button = tk.Button(self.action_frame, text="Mark Done", command=self.markcomplete, width=10)
        self.complete_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(self.action_frame, text="Delete", command=self.deletetask, width=10)
        self.delete_button.grid(row=0, column=1, padx=5)

    def updatetasklistbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            status = "[X]" if task["done"] else "[ ]"
            self.task_listbox.insert(tk.END, f"{i+1}. {status} {task['description']}")

    def addtask(self):
        description = self.task_entry.get().strip()
        if description:
            self.tasks.append({"description": description, "done": False})
            self.task_entry.delete(0, tk.END)
            self.updatetasklistbox()
        else:
            messagebox.showwarning("Input Error", "Task can't be empty.")

    def markcomplete(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            self.updatetasklistbox()
        else:
            messagebox.showwarning("Selection Error", "Select  mark as done.")

    def deletetask(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.updatetasklistbox()
        else:
            messagebox.showwarning("Selection Error", "Select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

