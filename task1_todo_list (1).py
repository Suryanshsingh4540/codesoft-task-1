"""
CodeSoft Internship - Task 1: To-Do List Application
------------------------------------------------------
"""

import json
import os

DATA_FILE = "todo_data.json"


def load_tasks():
    """Load tasks from the JSON file, or return an empty list."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Save the current list of tasks to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def view_tasks(tasks):
    print("\n--- YOUR TO-DO LIST ---")
    if not tasks:
        print("No tasks yet. Add one!")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✔ Done" if task["done"] else "✗ Pending"
        print(f"{i}. {task['title']}  [{status}]")
    print("------------------------\n")


def add_task(tasks):
    title = input("Enter the task description: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print(f"Task '{title}' added successfully!\n")
    else:
        print("Task cannot be empty.\n")


def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Enter the task number to update: ")) - 1
        if 0 <= idx < len(tasks):
            new_title = input("Enter the new description: ").strip()
            if new_title:
                tasks[idx]["title"] = new_title
                save_tasks(tasks)
                print("Task updated successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            save_tasks(tasks)
            print("Task marked as done!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Enter the task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f"Task '{removed['title']}' deleted.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    tasks = load_tasks()
    menu = """
========== TO-DO LIST ==========
1. View Tasks
2. Add Task
3. Update Task
4. Mark Task as Done
5. Delete Task
6. Exit
=================================
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid choice. Please select 1-6.\n")


if __name__ == "__main__":
    main()
