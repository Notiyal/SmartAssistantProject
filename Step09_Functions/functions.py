# Step 9: Functions

print("--------- Functions ---------")

def greet_user():
  print("\nHello! Welcome to Smart Assistant Project")

def display(name, age, city):
  print("\n---- User Profile ----")
  print(f"Name: {name} \nAge: {age} \nCity: {city}")

def create_profile():
  print("\nEnter below details:-")
  name = input("Name: ")
  age = int(input("Age: "))
  city = input("City: ")

  profile = {"name": name, "age": age, "city": city}
  return profile

greet_user()

user_profile = create_profile()
display(user_profile["name"], user_profile["age"], user_profile["city"])