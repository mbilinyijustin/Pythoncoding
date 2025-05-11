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
        print("📭 No tasks found,")
        return

    for i, task in enumerate(tasks, 1):
        status = "✅ Done" if task["done"] else "❌ Note done"
        due = task.get('due_date')
        due_str = f" | Due: {due.strftime('%Y-%m-%d')}" if due else ""
        category = task.get("category", "Uncategorized")
        #print(f"{i}. {task['task']} ({status}) - Added: {task['timestamp']}")
        print(f"{i}. {task['task']} ({category}) - {status}{due_str} - Added: {task['timestamp'].strftime('%Y-%m-%d %H:%M:%s')}")


def add_task(tasks):
    #task_name = input("Enter the task: ")
    task_desc = input("Enter new task: ")
    category = input("Enter category (e.g., Work, School, Personal):")
    due = input("Enter due date (YYYY-MM-DD) or leave blank: ")

    try:
        due_date = datetime.striptime(due, "%Y-%m-%d") if due else None
    except ValueError:
        print("⚠ Invalid date format. Skipping due date.")
        due_date = None

    new_task = {
        "task": task_desc,
        "category": category,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "done": False
    }

    tasks.append(new_task)
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
            print("❌ Invalid task number.")
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


def search_tasks(tasks):
    keyword = input("Enter a keyword to search: ").lower()
    found = False
    for index, task in enumerate(tasks):
        if keyword in task['task'].lower():
            status = "✅" if task['done'] else "❌"
            print(f"{index + 1}. {task['task']} - {status} - Added: {task['timestamp']}")
            found = True
    if not found:
        print("🔍 No matching task found.")


def sort_tasks(tasks):
    print("🔀 Sort by:")
    print("1. Date added (oldest first)")
    print("2. Date added (newest first)")
    print("3. Status (✅ done  first)")
    print("4. Status (❌ not done first)")
    print("5. Category (Categorized first")
    print("6. Category (Uncategorized first")
    print("7. Alphabetical (A-Z)")
    print("8. Alphabetical (Z-A)")
    choice = input("Choose an option: ")

    if choice == "1":
        tasks.sort(key=lambda x: x['timestamp'])  # ascending
    elif choice == "2":
        tasks.sort(key=lambda x: x['timestamp'], reverse=True)  # descending
    elif choice == "3":
        tasks.sort(key=lambda x: not ['done'])  # True = 1, Fakse = 0
    elif choice == "4":
        tasks.sort(key=lambda x: x['done'])  # not done first
    elif choice == "5":
        tasks.sort(key=lambda x: (x.get('category') is None, x.get('category', '').lower()))
    elif choice == "6":
        tasks.sort(key=lambda x: (x.get('category') is not None, x.get('category', '').lower()))
    elif choice == "7":
        tasks.sort(key=lambda x: x['task'].lower())
    elif choice == "8":
        tasks.sort(key=lambda x: x['task'].lower(), reverse=True)
    else:
        print("❌ Invalid choice")
        return

    print("✅ Task sorted successfully.")
    show_tasks(tasks)


def filter_by_category(tasks):
    keyword = input("Enter category name to filter: ")
    found = False
    for i, task in enumerate(tasks):
        category = task.get('category', 'Uncategorized')  #Default if key is missing
        if category.lower() == keyword.lower():
            status = "✅" if task['done'] else "❌"
            print(f"{i + 1}. {task['task']} ({category}) - {status} - Added: {task['timestamp']}")
            found = True
    if not found:
        print("❌ No tasks found in this category.")

def check_reminders(tasks):
    today = datetime.today().date()
    found = False

    print("🔔 Upcoming or Overdue Tasks:")
    for task in tasks:
        due = task.get('due_date')
        if due and due.get() <= today and not task['done']:
            print(f"⚠️ {task['task']} - Due: {due.strftime('%Y-%m-%d')}")
            found = True

    if not found:
        print("🎉 No upcoming or Overdue tasks.")


def main():
    tasks = load_tasks()

    while True:
        print("\n📜 TO-DO LIST MENU:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete task")
        print("5. 🔍 Search task")
        print("6. Sort tasks")
        print("7. View task by category")
        print("8. View Due & Overdue Reminders")
        print("9. Exit")

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
            search_tasks(tasks)
        elif choice == "6":
            sort_tasks(tasks)
        elif choice == "7":
            filter_by_category(tasks)
        elif choice == "8":
            check_reminders(tasks)
        elif choice == "9":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
