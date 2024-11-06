print("Welcome!")


class list1:


  def __init__(self):
        self.tasks = []

def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully.")
        else:
            print("Task not found in the list.")

def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks found.")

            def main():
                 todo_list = list1()
while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            list1.add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            list1.remove_task(task)
        elif choice == "3":
            print("Enter Task to view:")
            list1.view_tasks()
        elif choice == "4":
            print("Exit Application!")
            break
        else:
            print("GOODBYE")






       
                    