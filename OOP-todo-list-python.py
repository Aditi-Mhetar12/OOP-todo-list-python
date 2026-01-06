import json

class TodoApp:
    def __init__(self):
        self.filename = "tasks.json"
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file)

    def add_task(self):
        try:
            no = int(input("Enter number of tasks: "))
            if no <= 0:
                print("Please enter a positive number.")
                return
            for i in range(1, no + 1):
                task = input(f"Enter task {i}: ")
                self.tasks.append(task)
            self.save_tasks()
            print("Tasks added successfully!")
        except ValueError:
            print("Invalid input! Please enter numbers only.")


    def update_task(self):
        old_task = input("Enter task to update: ")
        if old_task in self.tasks:
            new_task = input("Enter new task: ")
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            self.save_tasks()
            print("Task updated successfully!")
        else:
            print("Task not found!")

    def delete_task(self):
        task = input("Enter task to delete: ")
        if task in self.tasks:
            self.tasks.remove(task)
            self.save_tasks()
            print("Task deleted successfully!")
        else:
            print("Task not found!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available")
        else:
            print("Your Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(i, task)

    def run(self):
        print("------ WELCOME TO OOP BASED TO-DO APP ------")
        while True:
            print("\n1. Add Task")
            print("2. Update Task")
            print("3. Delete Task")
            print("4. View Tasks")
            print("5. Exit")


            choice = input("Enter choice: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.update_task()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                self.view_tasks()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice")


obj = TodoApp()
obj.run()
