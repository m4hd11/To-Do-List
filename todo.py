import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os


class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = int(priority)


class ToDoList:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.csv"
        self.Load_From_File()

    def Add_Task(self, name, description, priority):
        if any(task.name.lower() == name.lower() for task in self.tasks):
            return False, "This task name already exists!"

        if any(task.priority == priority for task in self.tasks):
            return False, f"Priority {priority} already used."

        self.tasks.append(Task(name, description, priority))
        self.Save_To_File()
        return True, "Task added successfully!"

    def Delete_Task(self, index):
        self.tasks.sort(key=lambda t: t.priority)
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.Save_To_File()
            return True, "Task deleted."
        return False, "Invalid index!"

    def Swap_Priorities(self, index1, index2):
        self.tasks.sort(key=lambda t: t.priority)
        if 0 <= index1 < len(self.tasks) and 0 <= index2 < len(self.tasks):
            self.tasks[index1].priority, self.tasks[index2].priority = (
                self.tasks[index2].priority,
                self.tasks[index1].priority,
            )
            self.Save_To_File()
            return True, "Priorities swapped successfully!"
        return False, "Invalid task indices!"

    def Save_To_File(self):
        self.tasks.sort(key=lambda t: t.priority)
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "description", "priority"])
            for task in self.tasks:
                writer.writerow([task.name, task.description, task.priority])

    def Load_From_File(self):
        if not os.path.exists(self.filename):
            return
        self.tasks.clear()
        with open(self.filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.tasks.append(
                    Task(row["name"], row["description"], int(row["priority"]))
                )


class ToDoApp:
    def __init__(self, root):
        self.todo = ToDoList()
        self.root = root
        self.root.title("To-Do List 📝")
        self.root.geometry("600x400")
        self.root.configure(bg="#f2f2f2")

        self.task_listbox = tk.Listbox(root, font=("Segoe UI", 11), height=12, width=70)
        self.task_listbox.pack(pady=15)

        self.refresh_tasks()

        frame = tk.Frame(root, bg="#f2f2f2")
        frame.pack(pady=5)

        tk.Button(frame, text="➕ Add Task", width=15, command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="❌ Delete Task", width=15, command=self.delete_task).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="🔄 Swap Priorities", width=15, command=self.swap_priorities).grid(row=0, column=2, padx=5)
        tk.Button(frame, text="🔃 Refresh", width=15, command=self.refresh_tasks).grid(row=0, column=3, padx=5)

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.todo.tasks.sort(key=lambda t: t.priority)
        for i, task in enumerate(self.todo.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{i}. {task.name} | {task.description} | Priority: {task.priority}")

    def add_task(self):
        name = simpledialog.askstring("Add Task", "Task name:")
        if not name:
            return
        description = simpledialog.askstring("Add Task", "Description:")
        if not description:
            return
        try:
            priority = int(simpledialog.askstring("Add Task", "Priority (1 = highest):"))
        except:
            messagebox.showerror("Error", "Priority must be a number!")
            return

        success, msg = self.todo.Add_Task(name, description, priority)
        if success:
            self.refresh_tasks()
        else:
            messagebox.showerror("Error", msg)

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            return
        index = selection[0]
        success, msg = self.todo.Delete_Task(index)
        if success:
            self.refresh_tasks()
        else:
            messagebox.showerror("Error", msg)

    def swap_priorities(self):
        if len(self.todo.tasks) < 2:
            messagebox.showinfo("Info", "You need at least two tasks to swap.")
            return

        try:
            idx1 = int(simpledialog.askstring("Swap", "Enter first task number:")) - 1
            idx2 = int(simpledialog.askstring("Swap", "Enter second task number:")) - 1
        except:
            messagebox.showerror("Error", "You must enter valid numbers.")
            return

        if idx1 == idx2:
            messagebox.showwarning("Warning", "Please select two different tasks.")
            return

        success, msg = self.todo.Swap_Priorities(idx1, idx2)
        if success:
            self.refresh_tasks()
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showerror("Error", msg)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
