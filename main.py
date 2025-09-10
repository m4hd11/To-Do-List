from mylibrary import ToDoList

def To_Do_Sys():
    task = ToDoList()
    task.Load_From_File()

    print("\nHello, Welcome to your 'To-Do-List' program.\n")
    while True:
        print("To-Do-List's options:\n ")
        print("1.Add Task")
        print("2.Delete Task")
        print("3.Show All Tasks")
        print("4.Swap Task Priorities")
        print("5.Exit\n")

        user_choice = input("please choose a number from the list: ")

        if user_choice == '1':
            while True:
                print("\nTask Name: ")
                print("---------------------------------")
                print("Return to menu --->  Press '0'")
                name = input(">> ").strip()
                if name == '0':
                    break

                if any(i.name.lower() == name.lower() for i in task.tasks):
                    print(f"Task '{name}' is already exists!")
                    continue

                print("\nDescription: ")
                print("---------------------------------")
                print("Return to menu --->  Press '0'")

                description = input(">> ").strip()
                if description == '0':
                    break

                used_priorities = {n.priority for n in task.tasks}

                while True:
                    print("Priority (lower number = higher priority)(return to menu by '0'):")
                    print("---------------------------------")
                    priority_input = input(">> ")
                    if priority_input == '0':
                        break

                    if priority_input.isdigit():
                        priority = int(priority_input)
                        if priority <=0:
                            print("Priority must be greater than zero!")
                        elif priority in used_priorities:
                            print(f"Priority '{priority}' is already used. Please choose another one.")
                        else:
                            task.Add_Task(name, description, priority)
                            task.Save_To_File()
                            break
                    else:
                        print("Priority must be a number!")

                if priority_input == '0':
                    break

                break
                
                
        elif user_choice == '2':
            if not task.tasks:
                  print("\nYou have no tasks to delete!")
                  continue
            task.Show_All_Tasks()

            print("\nPlease enter the task's number you wanna delete: ")
            print("---------------------------------")
            print("Return to menu --->  Press '0'")
            user_input = input(">> ").strip()
            if user_input == '0':
                continue
            
            if user_input .isdigit():
                 task_number = int(user_input)
                 task.Delete_Task(task_number)
                 task.Save_To_File()
            else:
                print("\nInvalid input! Please enter a number.\n")

        elif user_choice == '3':
            task.Show_All_Tasks()

        elif user_choice == '4':
            if not task.tasks  or len(task.tasks) < 2:
                print("\nYou need at least two tasks for swap!")
                continue
            task.Show_All_Tasks()

            while True:

                print("\nEnter the number of the first task you want to swap: ")
                print("---------------------------------")
                print("Return to menu --->  Press '0'")
                first_num_input = input(">> ").strip()
                if first_num_input == '0':
                    break
                if not first_num_input.isdigit():
                    print("Invalid input! Please enter a number.")
                    continue
                first_num = int(first_num_input)
                if 1 <= first_num <= len(task.tasks):
                    break
                else:
                    print(f"Invalid task number! choose between 1 and {len(task.tasks)}")
            if first_num_input == '0':
                continue

            while True:
                print("\nEnter the number of the second task you want to swap: ")
                print("---------------------------------")
                print("Return to menu --->  Press '0'")
                second_num_input = input(">> ").strip()
                if second_num_input == '0':
                    break
                if not second_num_input.isdigit():
                    print("Invalid input! Please enter a number.")
                    continue
                second_num = int(second_num_input)
                if 1 <= second_num <= len(task.tasks):
                    if second_num == first_num:
                        print("\nPlease choose two different task's number!\n")
                        continue
                    break
                else:
                    print(f"Invalid task number! choose between 1 and {len(task.tasks)}")
            if second_num_input == '0':
                continue

            sorted_tasks = sorted(task.tasks, key=lambda t: t.priority)
            task1 = sorted_tasks[first_num - 1]
            task2 = sorted_tasks[second_num -1]

            task1.priority, task2.priority = task2.priority, task1.priority
            print(f"\nPriorities of '{task1.name}' and '{task2.name}' swapped successfully!")
            task.Save_To_File()

        elif user_choice == '5':
            task.Save_To_File()
            print("\nExiting from the program!")
            print("\nSee you later!")
            break
        else:
            print("\nWrong input!\n")

if __name__ == "__main__":
    To_Do_Sys()