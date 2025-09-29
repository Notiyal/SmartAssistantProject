# Step 7: Tuples A tuple is an ordered and unchangeable (immutable) collection of items, often used to group related data. Unlike lists, which are mutable, the elements within a tuple cannot be changed or modified after the tuple is created. Tuples are created using parentheses () with items separated by commas, and they are useful for functions to return multiple values or for grouping data where the order and integrity of the values are important. 

print("----- Tuples -------")

# Asking user informartion
user_input = input("Enter details (name, age, city): ")

#splitting user information seperated by comma
parts = user_input.split(',')
name = parts[0].strip()
age = int(parts[1].strip())
city = parts[2].strip()

# Store in tuple
user_profile = (name, age, city)

# Accessing tuples elements
print("------ User information (Tuples)------------")
print("Name: ", user_profile[0])
print("Age: ",user_profile[1])
print("City: ", user_profile[2])

# Unpacking tuple
a, b, c = user_profile
print(f"\nUnpacked Tuple -> Name: {a}, Age: {b}, City: {c}")

print("\nTuples are immutable (cannot be changed)")
try:
  user_profile[1] = age + 3
except TypeError as e:
  print("Error: ", e)
