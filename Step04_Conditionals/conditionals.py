# Step 4: Conditionals

print(f"Welcome to the Smart Assistant Decision Center!")

# User age
age = int(input("\nEnter your age: "))

# if-else condition
if age >= 18:
  print("You are eligible to vote.")
else:
  print("You are not eligible to vote yet.")

# Current temperature
temp = float(input("\nEnter current temperature in celcius: "))

# if-elif-else chain
if temp < 0:
  print("It's freezing outside! Wear winter clothes.")
elif temp < 20:
  print("IT's a bit chilly. Wear a jacket.")
elif temp < 30:
  print("Weather is pleasant. Enjoy your day!")
else:
  print("It's hot! Stay hydrated.")

# Nested conditional
is_student = input("\nAre you a student (yes/no): ").lower()

if is_student == "yes":
  grade = int(input("Enter your grade(1=12): "))

  if grade <= 5:
    print("You are in primary school.")
  elif grade <= 10:
    print("You are secondary school.")
  else:
    print("You are in high school.")

else:
  print("You are not a student.")