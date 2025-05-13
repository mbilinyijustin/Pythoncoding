import json
import os
import shutil

TASKS_FILE = "tasks.json"
USERS_FILE = "users.json"


def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)


def register_user():
    users = load_users()
    username = input("Choose a username: ")
    if username in users:
        print("🚫 Username already exists!")
        return None
    password = input("Choose a password: ")
    users[username] = password
    save_users(users)
    print("✅ User registered successfully!")
    return username


def login_user():
    users = load_users()
    username = input("Enter username: ")
    password = input("Enter password: ")
    if users.get(username) == password:
        print(f"✅ welcome back, {username}!")
        return username
    else:
        print("🚫 Invalid username or password.")
        return None


def get_user_task_file(username):
    return f"{username}_tasks.json"


def load_tasks(username):
    try:
        with open(f"{username}_tasks.json", "r") as f:
            tasks = json.load(f)
            for task in tasks:
                if task.get("due_date"):
                    try:
                        task["due_date"] = datetime.fromisoformat(task["due_date"])
                    except ValueError:
                        pass
            return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(username, tasks):
    serializable_tasks = []
    for task in tasks:
        task_copy = task.copy()
        if isinstance(task_copy.get("due_date"), datetime):
            task_copy["due_date"] = task_copy["due_date"].isoformat()
        serializable_tasks.append(task_copy)

    # filename = get_user_task_file(username)
    with open(f"{username}_tasks.json", "w") as f:
        json.dump(serializable_tasks, f, indent=2)


def loadi_tasks():
    try:
        with open(f"", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                if task.get("timestamp"):
                    task["timestamp"] = datetime.strptime(task["timestamp"], "%Y-%m-%d %H:%M:%S")
                if task.get("due_date"):
                    task["due_date"] = datetime.strptime(task["due_date"], "%Y-%m-%d")
            return tasks
    except FileNotFoundError:
        return []
    # if not os.path.exists(TASKS_FILE):
    #  return []
    # with open(TASKS_FILE, "r") as file:
    #  return json.load(file)


def savee_tasks(tasks):
    # make backup
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


from datetime import datetime


def show_tasks(tasks):
    print("\n 📝 Your tasks:")
    if not tasks:
        print("📭 No tasks found.")
        return

    for i, task in enumerate(tasks, 1):
        status = "✅ Done" if task["done"] else "❌ Note done"
        due = task.get('due_date')
        category = task.get("category", "Uncategorized")

        # Always try to get the timestamp safely
        timestamp_str = "Unknown"
        try:
            timestamp = datetime.strptime(task['timestamp'], "%Y-%m-%d %H:%M:%S")
            timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        except (KeyError, ValueError, TypeError):
            pass  # Leave as "Unknown" if something goes wrong

        # Handle due date formatting
        due_str = ""
        if isinstance(due, datetime):
            due_str = f" | Due: {due.strftime('%Y-%m-%d')}"
        elif isinstance(due, str):
            try:
                parsed_due = datetime.strptime(due, "%Y-%m-%d")
                due_str = f" | Due: {parsed_due.strftime('%Y-%m-%d')}"
            except ValueError:
                pass  # Ignore if not a valid date string

        print(f"{i}. {task['task']} ({category}) - {status}{due_str} - Added: {timestamp_str}")


def add_task(tasks):
    # task_name = input("Enter the task: ")
    task_desc = input("Enter new task: ").strip()
    category = input("Enter category (e.g., Work, School, Personal):").strip()
    due = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()

    # check for duplicate task
    for task in tasks:
        if task['task'].lower() == task_desc.lower() and task.get('category', '').lower() == category.lower():
            print("⚠️ Task already exists in this category!")
            return  # Exit without adding

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
    savee_tasks(tasks)
    print("✅ Task added.")


def mark_task_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done:"))
        if 0 < num <= len(tasks):
            tasks[num - 1]["done"] = True
            savee_tasks(tasks)
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
            savee_tasks(tasks)
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
        category = task.get('category', 'Uncategorized')  # Default if key is missing
        if category.lower() == keyword.lower():
            status = "✅" if task['done'] else "❌"
            print(f"{i + 1}. {task['task']} ({category}) - {status} - Added: {task['timestamp']}")
            found = True
    if not found:
        print("❌ No tasks found in this category.")


def check_reminders(tasks):
    print("\n🔔 Upcoming or Overdue Tasks:")
    today = datetime.today().date()
    due_count = 0

    for task in tasks:
        if task.get('done'):
            continue  # Skip completed tasks

        due = task.get('due_date')
        if not due:
            continue  # Skip tasks without a due date

        try:
            # Handle due_date being either a string or datetime object
            if isinstance(due, str):
                due_date = datetime.strptime(due, "%Y-%m-%d").date()
            elif isinstance(due, datetime):
                due_date = due.date()
            else:
                continue
        except ValueError:
            print(f"- {task['task']} (⚠️ Invalid due date format)")
            continue

        if due_date <= today:
            due_count += 1
            print(
                f"- {task['task']} (Category: {task.get('category', 'Uncategorized')}) | Due: {due_date.strftime(
                    '%Y-%m-%d')}")

    if due_count == 0:
        print("🎉 No upcoming or Overdue tasks.")
    else:
        print(f"\n📌 Total Due or Overdue Tasks: {due_count}")


def main():
    print("Welcome to Task Manager 🧠")
    current_user = None

    while not current_user:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            current_user = register_user()
        elif choice == "2":
            current_user = login_user()
        elif choice == "3":
            print("👋 Goodbye!")
            return
        else:
            print("❌ Invalid choice.")

    tasks = load_tasks(current_user)

    while True:
        print(f"\n📋 Main Menu for {current_user}")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6. Sort Tasks")
        print("7. Filter by Category")
        print("8. Check Reminders")
        print("9. Logout")
        print("0. Exit")

        option = input("Choose an action: ").strip()

        if option == "1":
            show_tasks(tasks)
        elif option == "2":
            add_task(tasks)
            save_tasks(current_user, tasks)
        elif option == "3":
            mark_task_done(tasks)
            save_tasks(current_user, tasks)
        elif option == "4":
            delete_task(tasks)
            save_tasks(current_user, tasks)
        elif option == "5":
            search_tasks(tasks)
        elif option == "6":
            sort_tasks(tasks)
            save_tasks(current_user, tasks)
        elif option == "7":
            filter_by_category(tasks)
        elif option == "8":
            check_reminders(tasks)
        elif option == "9":
            print("🔐 Logged out.")
            main()  # Go back to log in/register
            return
        elif option == "0":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()
