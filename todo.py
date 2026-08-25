# My To-Do List App - by Pranavi
tasks = []

while True:
    print("\n--- Pranavi's TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    choice = input("Enter choice (1-3): ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print(f"Added: {task}")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet! Add one.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
    elif choice == "3":
        print("Bye Pranavi! Have a productive day!")
        break
    else:
        print("Invalid choice, try again!")