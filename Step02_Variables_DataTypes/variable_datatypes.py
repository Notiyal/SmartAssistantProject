# Step 2: Variable & Data Types

# Asking user for details
name = input("What is your name? ")
age = int(input("What is your age? "))
city = input("Which city do you live in? ")
student = input("Are you a student? (yes/no): ")

# Convert (yes/no) to boolean
is_student = student.lower() == "yes"

# Printing details using f-stings
print("\n--- Your Profile ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Student: {is_student}")

# Operations
future_age = age + 5
print(f"In five years, you will be {future_age} years old")