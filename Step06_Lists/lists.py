# Step 6: Lists - stores multiple value in one variable, ordered, changeble and hold mixed data types

print("-----------Lists-------------")

# List of different task for the Assistant
tasks = ["Read a book", "Go for a Walk", "Lear Python"]

# Print the list of tasks
#print("Your tasks: ", tasks)

def show_tasks():
  if not tasks:
    print("No task in your list.")
  else:
    print("\n----Current task list------")
    for iList, task in enumerate(tasks, start=1):
      print(f"{iList}. {task}")

show_tasks()

while True:
  action = input("\nChoose action add / remove / done: ").lower()

  if action == "add":
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    print(f"✅ Task {new_task} added.")
    show_tasks()
  
  elif action == "remove":
    try:
      task_num = int(input("Enter the task number you want to remove: "))
      if 1<= task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        print("❌ Task '{removed}' removed.")
      else:
        print("⚠️ Enter valid number.")
    except ValueError:
      print("⚠️ Invalid task number.")
    show_tasks()
  
  elif action == "done":
    break

  else:
    print("Invalid choice. Please type add, remove, or done.")

# Total numer of task in list
print(f"You have", len(tasks), "tasks in you list.")