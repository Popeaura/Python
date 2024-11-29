# To do list 

tasks = []

def display_task():
    if not task:
        print("\nYour to-do list is empty!")
        else:
        print("\Your to -do list :")
        for index, task in enumerate(task, 1):
            print(f "{index}.{task}")

def display_task():
        task = input("Enter the task:")
        tasks.append(task)
        print(f"Task '{task}' added successfully !")