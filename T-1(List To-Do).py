import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_tasks(tasks):
    if not tasks:
        print("Sorry . It's Empty")
    else:
        print("My List To-Do :")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def Set_task(tasks, task):
    tasks.append(task)
    print(f"Task '{task}' Set Your List To-Do")

def upgrade_task(tasks, index, new_task):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = new_task
        print(f"Task {index} Upgraded :)")
    else:
        print("Invalid task index. Use 'list' to see available tasks.")

def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task {index} Deleted: {removed_task}")
    else:
        print("Invalid task index. Use 'list' to see available tasks.")

def main():
    tasks = []
    
    while True:
        clear_screen()  
        display_tasks(tasks)
        
        print("\nTask Process:")
        print("1. Set My Task")
        print("2. Upgrader My Task")
        print("3. Delete My Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Mention Your task description: ")
            Set_task(tasks, task)
        elif choice == "2":
            index = int(input("Mention your task index to update: "))
            new_task = input("Mention My new task description: ")
            upgrade_task(tasks, index, new_task)
        elif choice == "3":
            index = int(input("Mention My task index to remove: "))
            delete_task(tasks, index)
        elif choice == "4":
            print("See You Soon With A New Task_Update :)")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
