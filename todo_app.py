import json
from datetime import datetime
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("No tasks found,")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅ Done" if task["done"] else "❌ Note done"
        print(f"{i}. {task['task']} ({status}) - Added: {task['timestamp']}")


def add_task(tasks):
    task_name = input("Enter ne task: ")
    task = {
        "task": task_name,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added.")


def mark_task_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done:"))
        if 0 < num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print("✅ Task marked as done.")
        else:
            print("❌ Invald task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🚮 Deleted task: {removed['task']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n📜 TO-DO LIST MENU:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an Option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
