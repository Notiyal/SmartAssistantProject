# Step 10_1: Lists + Dictionaries + Functions
# Managing multiple tasks in a list of dictionaries

print("\n--------------- Task Manager(Enhanced) -----------------\n")

# Initialize empty list to store all the tasks
tasks = []

# Display all the task
def display_task():
  if not tasks:
    print("\nNo task available\n")
    return
  
  print("\n-----------Your Task------------")
  for idx, task in enumerate(tasks, start=1):
    print(f"{idx}. {task['title']} - {task['status']} - {task['priority']}")
    print(f"  Description: {task['description']}")
  print()

# Functions
def add_task():
  # Add new task

  title = input("\nEnter task title: ")
  desc = input("Enter task description: ")
  priority = input("Enter task priority (High/Medium/Low): ").capitalize()

  task = {
    "title": title,
    "description": desc,
    "priority": priority,
    "status": "Pending"
  }

  tasks.append(task)
  print(f"Task {title} added successfully.\n")

# Update task from thr list
def update_task():
  display_task()
  if not tasks:
    return
  
  try:
    choice = int(input("\nEnter task number to be updated: ")) - 1
    if 0 <= choice < len(tasks):
      new_status = input("Enter new status (Pending/In Progress/Completed): ").capitalize()
      tasks[choice]["status"] = new_status
      print(f"Task {tasks[choice]['title']} updated successfully\n")
  except ValueError:
    print("Enter a valid number")

# Delete the task
def delete_task():
  display_task()

  if not tasks:
    return
  
  try:
    choice = int(input("\nEnter task need to be deleted: ")) - 1
    if 0 <= choice < len(tasks):
      removed = tasks.pop(choice)
      print(f"Task {removed['title']} deleted successfully.\n")
    else:
      print("Invalid selection.")  
  except ValueError:
    print("Enter a valid number.")
  
# Main Loop 
while True:
  action = input("Choose an action (add / delete / update / display / exit): ").lower()

  if action == "add":
    add_task()
  elif action == "delete":
    delete_task()
  elif action == "update":
    update_task()
  elif action == "display":
    display_task()
  elif action == "exit":
    print("Exiting...")
    break
  else:
    print("Invalid action! Please choose the correct course of action.\n")