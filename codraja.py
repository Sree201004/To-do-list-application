import json
import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

class Task:
    def __init__(self, description, priority='medium', due_date=None):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def to_dict(self):
        return {
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date,
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, task_dict):
        task = cls(
            description=task_dict['description'],
            priority=task_dict['priority'],
            due_date=task_dict['due_date']
        )
        task.completed = task_dict['completed']
        return task

    def __str__(self):
        return f"[{'x' if self.completed else ' '}] {self.description} (Priority: {self.priority}, Due: {self.due_date})"


class ToDoList:
    def __init__(self, file_name='tasks.json'):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, 'r') as file:
                tasks_data = json.load(file)
                return [Task.from_dict(task) for task in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description, priority='medium', due_date=None):
        task = Task(description, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.todo_list = ToDoList()

        self.task_listbox = tk.Listbox(root, width=50, height=20)
        self.task_listbox.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_task_completed)
        self.complete_button.pack()

        self.refresh_tasks()

    def add_task(self):
        description = simpledialog.askstring("Task Description", "Enter task description:")
        if not description:
            return

        priority = simpledialog.askstring("Task Priority", "Enter task priority (low, medium, high):")
import json
import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime, date

class Task:
    def __init__(self, description, priority='medium', due_date=None):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def to_dict(self):
        return {
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, task_dict):
        due_date = task_dict['due_date']
        if due_date:
            due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
        task = cls(
            description=task_dict['description'],
            priority=task_dict['priority'],
            due_date=due_date
        )
        task.completed = task_dict['completed']
        return task

    def __str__(self):
        return f"[{'x' if self.completed else ' '}] {self.description} (Priority: {self.priority}, Due: {self.due_date})"


class ToDoList:
    def __init__(self, file_name='tasks.json'):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, 'r') as file:
                tasks_data = json.load(file)
                return [Task.from_dict(task) for task in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description, priority='medium', due_date=None):
        task = Task(description, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.todo_list = ToDoList()

        self.task_listbox = tk.Listbox(root, width=50, height=20)
        self.task_listbox.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_task_completed)
        self.complete_button.pack()

        self.refresh_tasks()

    def add_task(self):
        description = simpledialog.askstring("Task Description", "Enter task description:")
        if not description:
            return

        priority = simpledialog.askstring("Task Priority", "Enter task priority (low, medium, high):")
import json
import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

class Task:
    def __init__(self, description, priority='medium', due_date=None):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def to_dict(self):
        return {
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, task_dict):
        due_date = task_dict['due_date']
        if due_date:
            due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
        task = cls(
            description=task_dict['description'],
            priority=task_dict['priority'],
            due_date=due_date
        )
        task.completed = task_dict['completed']
        return task

    def __str__(self):
        return f"[{'x' if self.completed else ' '}] {self.description} (Priority: {self.priority}, Due: {self.due_date})"


class ToDoList:
    def __init__(self, file_name='tasks.json'):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, 'r') as file:
                tasks_data = json.load(file)
                return [Task.from_dict(task) for task in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description, priority='medium', due_date=None):
        task = Task(description, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.todo_list = ToDoList()

        self.task_listbox = tk.Listbox(root, width=50, height=20)
        self.task_listbox.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_task_completed)
        self.complete_button.pack()

        self.refresh_tasks()

    def add_task(self):
        description = simpledialog.askstring("Task Description", "Enter task description:")
        if not description:
            return

        priority = simpledialog.askstring("Task Priority", "Enter task priority (low, medium, high):")
        if priority not in ['low', 'medium', 'high']:
            priority = 'medium'

        due_date_str = simpledialog.askstring("Due Date", "Enter due date (YYYY-MM-DD) [optional]:")
        due_date = None
        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
            except ValueError:
                messagebox.showerror("Invalid Date", "Invalid date format. Use YYYY-MM-DD.")
                return

        self.todo_list.add_task(description, priority, due_date)
        self.refresh_tasks()

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.todo_list.remove_task(index)
            self.refresh_tasks()
        except IndexError:
            messagebox.showerror("Error", "No task selected.")

    def mark_task_completed(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.todo_list.mark_task_completed(index)
            self.refresh_tasks()
        except IndexError:
            messagebox.showerror("Error", "No task selected.")

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            self.task_listbox.insert(tk.END, str(task))


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

