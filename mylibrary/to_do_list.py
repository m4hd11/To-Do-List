import csv
import os

class Task():
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = int(priority)
    
class ToDoList():

    def __init__(self):
        self.tasks = []
        self.filename = "tasks.csv"

    def Add_Task(self, name, description, priority):
        for task in self.tasks:
            if task.name.lower() == name.lower():
                print(f"\nTask '{name}' is already exist!")
                return
        
        for task in self.tasks:
            if task.priority == priority:
                print(f"\nPriority '{priority}' is already used! please choose another one!\n")
                return
    
        new_task = Task(name, description, priority)
        self.tasks.append(new_task)
        print(f"\nThe new task '{name}' added to your 'To-Do-List!'\n")

    def Delete_Task(self, task_number):

        sorted_tasks = sorted(self.tasks, key= lambda task: task.priority)

        if 1<= task_number <= len(sorted_tasks):
            task_to_delete = sorted_tasks[task_number - 1]
            self.tasks.remove(task_to_delete)
            print(f"\nThe task '{task_to_delete.name}' removed successfully!\n")
        else:
            print(f"\nInvalid task number!!\n") 

    def Show_All_Tasks(self):
        if not self.tasks:
            print("\nYou have nothing to do!\n")
            return
        
        sorted_tasks = sorted(self.tasks, key= lambda task: task.priority)

        print("\nThis is a list of all task you have to do:\n")
        for index, task in enumerate(sorted_tasks, start=1):
            print(f"{index}. {task.name} | Description: {task.description} | Priority: {task.priority}\n")

    def Save_To_File(self):
        sorted_tasks = sorted(self.tasks, key= lambda task: task.priority)
        with open (self.filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["name", "description", "priority"])
            for task in sorted_tasks:
                writer.writerow([task.name, task.description, task.priority])
        print("Tasks saved to file successfully\n")

    def Load_From_File(self):
        if not os.path.exists(self.filename):
            return
        
        with open (self.filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            self.tasks.clear()
            for row in reader:
                name = row['name']
                description = row['description']
                priority = int(row['priority'])
                self.tasks.append(Task(name, description, priority))
        print("Tasks loaded from file successfully\n")

        

