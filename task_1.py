tasks = []

def display_menu():
    """Display the menu options."""
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Exit")

def add_task():
    """Add a task to the list."""
    task_description = input("Enter task description: ")
    tasks.append(task_description)
    print("Task added successfully!")

def view_tasks():
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def mark_completed():
    """Mark a task as completed."""
    view_tasks()
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            print("Exiting the program. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
