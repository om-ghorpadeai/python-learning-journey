# Day 12 - Simple To-Do List Manager

tasks = []

while True:
    print("\n=== To-Do List Manager ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(i, "-", task)

    elif choice == "3":
        task_number = int(input("Enter task number to remove: "))
        if 0 < task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print("Removed task:", removed)
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Exiting To-Do List Manager.")
        break

    else:
        print("Invalid option. Try again.")
