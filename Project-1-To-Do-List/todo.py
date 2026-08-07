import json

print("DecodeLabs To-Do List Project")

try:
    with open("tasks.json", "r") as file:
        my_tasks = json.load(file)

except FileNotFoundError:
    my_tasks = []

while True:
    print("\nMenu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_task = input("Enter a new task: ")

        task_data = {
            "id": len(my_tasks) + 1,
            "task": new_task
        }

        my_tasks.append(task_data)

        with open("tasks.json", "w") as file:
            json.dump(my_tasks, file, indent=4)

        print("Task added successfully!")

    elif choice == "2":
        if len(my_tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour To-Do List:")

            for task in my_tasks:
                print(f"{task['id']}. {task['task']}")

    elif choice == "3":
        if len(my_tasks) == 0:
            print("No tasks available to delete.")

        else:
            print("\nYour To-Do List:")

            for task in my_tasks:
                print(f"{task['id']}. {task['task']}")

            task_id = int(input("Enter task number to delete: "))

            task_found = False

            for task in my_tasks:
                if task["id"] == task_id:
                    my_tasks.remove(task)
                    task_found = True
                    break

            if task_found:
                for number, task in enumerate(my_tasks, start=1):
                    task["id"] = number

                with open("tasks.json", "w") as file:
                    json.dump(my_tasks, file, indent=4)

                print("Task deleted successfully!")

            else:
                print("Task number not found.")

    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")