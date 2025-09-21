# Step 5: Loops (for ,while)

# for loop
for i in range (1, 6):
  print(i, end=" ")
print("\n")

# while loop
print("Type 'exit' to stop the assistant.")

while True:
  command = input("Enter a command: ")
  if command.lower() == "exit":
    print("Exiting loop, Goodbye!")
    break
  else:
    print(f"You entered: {command}")