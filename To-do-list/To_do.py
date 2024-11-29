# To-Do List App

tasks = []

def display_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def remove_task():
    display_tasks()
    try:
        task_number = int(input("Enter the task number to remove: "))
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' removed successfully!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def mark_completed():
    display_tasks()
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        tasks[task_number - 1] += " (Completed)"
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_completed()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select again.")

if __name__ == "__main__":
    main()
