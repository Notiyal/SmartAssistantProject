# Step 10: Loops + Functions (Task Manager Refactor)
# Concepts: functions, loops, menu-driven structure

# Display tasks list
def show_tasks(tasks):
  if not tasks:
    print("\nNo tasks found!")
  else:
    for idx, task in enumerate(tasks, start=1):
      print(f"{idx}. {task}")

# Add task
def add_task(tasks):
  new_task = input("Enter the task: ")
  tasks.append(new_task)
  print("\nNew task added successfully.")

# Update task
def update_task(tasks):
  show_tasks(tasks)
  task_number = int(input("\nEnter task number which needed to be updated: "))
  new_task = input("Enter the task: ")
  tasks[task_number - 1] = new_task
  print("Task updated")

# Remove task
def remove_task(tasks):
  show_tasks(tasks)
  if not tasks:
    return
  
  try:
    task_number = int(input("\nEnter the task number which needed to be removed: "))
    if 1<= task_number <= len(tasks):
      tasks.pop(task_number - 1)
      print("Task removed successfully.")
  except ValueError:
    print("Enter valid task number")
  
# Main program
def task_manger():
  tasks = []

  print("\nWelcome to Task Manager")

  while True:
    print("\nChoose an action:")
    print("1. Add task")
    print("2. Update task")
    print("3. Remove task")
    print("4. Display tasks list")
    print("5. Exit")

    choice = input("\nEnter you choice (1-5): ")

    if choice == "1":
      add_task(tasks)
    elif choice == "2":
      update_task(tasks)
    elif choice == "3":
      remove_task(tasks)
    elif choice == "4":
      show_tasks(tasks)
    elif choice == "5":
      print("Exiting...")
      break
    else:
      print("Invalid choice! Please select between 1-4")

# Run the program

if __name__ == "__main__":
  task_manger()