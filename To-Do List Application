import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
        return
    print("\n--- TASK LIST ---")
    for idx, task in enumerate(tasks, 1):
        status = "[X]" if task["completed"] else "[ ]"
        print(f"{idx}. {status} {task['title']}")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== TODO APPLICATION ===")
        print("1. List Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Select option (1-5): ").strip()
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            title = input("Enter task title: ").strip()
            if title:
                tasks.append({"title": title, "completed": False})
                save_tasks(tasks)
                print("Task added successfully!")
        elif choice == "3":
            display_tasks(tasks)
            if tasks:
                try:
                    idx = int(input("Task number to complete: ")) - 1
                    if 0 <= idx < len(tasks):
                        tasks[idx]["completed"] = True
                        save_tasks(tasks)
                        print("Task marked as completed!")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number!")
        elif choice == "4":
            display_tasks(tasks)
            if tasks:
                try:
                    idx = int(input("Task number to delete: ")) - 1
                    if 0 <= idx < len(tasks):
                        removed = tasks.pop(idx)
                        save_tasks(tasks)
                        print(f"Task '{removed['title']}' deleted!")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number!")
        elif choice == "5":
            print("Exiting application...")
            break

if __name__ == "__main__":
    main()
