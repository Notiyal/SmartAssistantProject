# Step 9_1: Dictionaries refactored with Functions

print("\n----------Step 8A: Dictionaries refactored with Functions---------\n")

def create_profile():
  print("Enter below details:- \n")
  name = input("Name: ")
  age = int(input("Age: "))
  city = input("City: ")
  return{"name": name, "age": age, "city": city}

def display_profile(profile):
  print("\n----------User Profile----------")
  for key, value in profile.items():
    print(f"{key} -> {value}")

def add_data(profile):
  key_name = input("\nEnter new data key: ")
  if key_name not in profile:
    key_value = input("Enter new key value: ")
    profile[key_name] = key_value
    print(f"{key_name} added successfully.")
  else:
    print("⚠️ Data already exist! Add a different key.")

def update_data(profile):
  key_name = input("\nEnter which data you want to update: ").lower()
  if key_name not in profile:
    print("⚠️ Data does not exist in the profile! Enter different key name.")
  else:
    key_value = input("Enter the value: ")
    if key_name == "age":
      try:
        key_value = int(key_value)
      except ValueError:
        print("Age must be a number.")
        return
    profile[key_name] = key_value
    print(f"{key_name} updated successfully.")

def delete_data(profile):
  key_name = input("Enter the data need to be deleted: ").lower()
  if key_name not in profile:
    print("⚠️ Data does not exist in the profile! Enter different key name.")
  else:
    deleted_key = profile.pop(key_name, None)
    print(f"{key_name} successfully removed.")

# Main Program

user_profile = create_profile()
display_profile(user_profile)

while True:
  print("\nChoose action add / update / delete / display / exit." )
  action = input("Your choice: ").lower()

  if action == "add":
    add_data(user_profile)
  elif action == "update":
    update_data(user_profile)
  elif action == "delete":
    delete_data(user_profile)
  elif action == "display":
    display_profile(user_profile)
  elif action == "exit":
    print("Exiting...")
    break
  else:
    print(f"{action} does not exist! Enter correct action you want to perform.")
