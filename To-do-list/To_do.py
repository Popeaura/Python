# To do list 

tasks = []

def display_task():
    if not task:
        print("\nYour to-do list is empty!")
        else:
        print("\Your to -do list :")
        for index, task in enumerate(task, 1):
            print(f"{index}.{task}")

def display_task():
        task = input("Enter the task:")
        tasks.append(task)
        print(f"Task '{task}' added successfully !")

def remove_task():
    display_task()
    try:
        task_number = int(input("Enter the task number to remove: "))
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' removed successfully!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def mark_complete():
    display_task()
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

      choice = input ("Enter your choice!:")  