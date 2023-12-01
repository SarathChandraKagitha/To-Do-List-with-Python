class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the to-do list.")
        else:
            print(f"Task '{task}' not found in the to-do list.")

# Example usage
todo_list = TodoList()
todo_list.add_task("Finish coding assignment")
todo_list.add_task("Buy groceries")
todo_list.view_tasks()
todo_list.remove_task("Buy groceries")
todo_list.view_tasks()
