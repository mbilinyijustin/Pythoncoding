import json
import os
from datetime import datetime
import shutil

TASKS_FILE = "tasks.json"


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                if task.get("timestamp"):
                    task["timestamp"] = datetime.strptime(task["timestamp"], "%Y-%m-%d %H:%M:%S")
                if task.get("due_date"):
                    task["due_date"] = datetime.strptime(task["due_date"], "%Y-%m-%d")
            return tasks
    except FileNotFoundError:
        return []
    #if not os.path.exists(TASKS_FILE):
     #  return []
    #with open(TASKS_FILE, "r") as file:
     #  return json.load(file)


def save_tasks(tasks):

    #make backup
    if os.path.exists("tasks.json"):
        shutil.copy("tasks.json", "tasks_backup.jason")
    def convert(task):
        task_copy = task.copy()
        if isinstance(task_copy.get("timestamp"), datetime):
            task_copy["timestamp"] = task_copy["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(task_copy.get("due_date"), datetime):
            task_copy["due_date"] = task_copy["due_date"].strftime("%Y-%m-%d")
        return task_copy


    with open("tasks.json", 'w') as file:
        json.dump([convert(task) for task in tasks], file, indent=4)




def show_tasks(tasks):
    if not tasks:
        print("📭 No tasks found,")
        return

    for i, task in enumerate(tasks, 1):
        status = "✅ Done" if task["done"] else "❌ Note done"
        due = task.get('due_date')
        if due:
            #if due is a datetime object
            due_str = f" | Due: {due.strftime('%Y-%m-%d')}"
        else:
            due_str = ""

        #Convert string timestamp to datetime object
        timestamp = task['timestamp']
        if isinstance(timestamp, str):
            timestamp = datetime.strptime((timestamp, "%Y-%m-%d %H:%M:%S"))

        category = task.get("category", "Uncategorized")
        #print(f"{i}. {task['task']} ({status}) - Added: {task['timestamp']}")
        print(f"{i}. {task['task']} ({category}) - {status}{due_str} - Added: {task['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")


def add_task(tasks):
    #task_name = input("Enter the task: ")
    task_desc = input("Enter new task: ")
    category = input("Enter category (e.g., Work, School, Personal):")
    due = input("Enter due date (YYYY-MM-DD) or leave blank: ")

    try:
        due_date = datetime.strptime(due, "%Y-%m-%d") if due else None
    except ValueError:
        print("⚠ Invalid date format. Skipping due date.")
        due_date = None

    new_task = {
        "task": task_desc,
        "category": category,
        "due_date": due_date,
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
    print("\n🔔 Upcoming or Overdue Tasks:")
    today = datetime.today().date()
    has_reminders = False

    #found = False
    for task in tasks:
        due_str = task.get('due_date')
        if due_str:
            try:
                due_date = datetime.strptime(due_str, "%Y-%m-%d").date()
            except ValueError:
                continue #Skip if the date format is wrong

            #Show only if due today or earlier and not yet done
            if due_date <= today and not task['done']:
                has_reminders = True
                print(f"- {task['task']} (category: {task.get('category', 'Uncategorized')}) | Due: {due_str}")

                #print(f"- {task['task']} (Due: {due_date.date()})")

                print(f"- {task['task']} (⚠️ Invalid due date format)")

    if not has_reminders:
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
