import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    clear_screen()
    print("Your To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def mark_task_done(tasks):
    show_tasks(tasks)
    task_index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index] = f"{tasks[task_index]} - Done"
        save_tasks(tasks)
        print("Task marked as done.")
    else:
        print("Invalid task number.")

def remove_task(tasks):
    show_tasks(tasks)
    task_index = int(input("Enter task number to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        clear_screen()
        print("To-Do List Application")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()