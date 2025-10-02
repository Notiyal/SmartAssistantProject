# Step 8: Dictionaries - Key-Value Pairs, ordered (from python 3.7+), changeble (mutable), no duplicate keys, immutable keys, syntax specific uses '{}'

print("------ Dictionaries --------")

print("\nEnter below details:-")
name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")

# Creating a dictionaries for user profile
user_profile = {
  "name": name,
  "age" : age,
  "city": city
}

# Display dictionary
print("\n-------- User Profile Dictionary -----")
# print(user_profile)
for key, value in user_profile.items():
  print(f"{key} -> {value}")

while True:
  print("\nChoose an action: add / update / delete / display / exit")
  action = input("Your choice: ").lower()

  # Add
  if action == "add":
    add_key = input("Enter the key: ")
    if add_key not in user_profile:
      key_value = input("Enter the value: ")
      user_profile[add_key] = key_value
    else:
      print("⚠️ Data (key) already exist. Enter different key.")

  # Update
  elif action == "update":
    update_key = input("Enter the key which you want to update: ")
    if update_key not in user_profile:
      print("⚠️Data (key) does not exist. Enter different key.")
    else:
      update_value = input("Enter the value: ")
      user_profile[update_key] = update_value

  # Delete
  elif action == "delete":
    delete_key = input("Enter the key you want to delete: ")
    if delete_key not in user_profile:
      print("⚠️ Data (key) does not exist. Enter different key.")
    else:
      user_profile.pop(delete_key)

  # Display
  elif action == "display":
    print("\n-------- User Profile Dictionary -----")
    # print(user_profile)
    for key, value in user_profile.items():
      print(f"{key} -> {value}")

  # Exit
  elif action == "exit":
    print("Thank you! Exiting...")
    break

  else:
    print("\n⚠️ Invalid choice! select correct choice.")