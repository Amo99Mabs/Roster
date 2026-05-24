tasks = []

def add_task():
    task = input("➕ Enter a new task: ")
    tasks.append(task)
    print(f"✅ Task '{task}' added.")

def list_tasks(): 
    if not tasks:
        print("📭 No tasks yet.")
    else:
        print("📝 Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"  #{index} → {task}")

def delete_task():
    list_tasks()
    try:
        index = int(input("🗑️ Enter task # to delete: "))
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"❌ Task '{removed}' deleted.")
        else:
            print("🚫 Invalid index.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    print("🧾 Welcome to the Roster App!")

    while True:
        print("\nChoose an option:")
        print("1️⃣ Add Task")
        print("2️⃣ Delete Task")
        print("3️⃣ List Tasks")
        print("4️⃣ Quit")

        choice = input("👉 Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice, please try again.")

if __name__ == "__main__":
    main()



