# Step 3: Operators

# Take numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithemetic Operators +, -, *, /, //, %, **
print("\n--- Arithemetic Operators ---")
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2}")
print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
print(f"Modulus: {num1} % {num2} = {num1 % num2}")
print(f"Exponent: {num1} ** {num2} = {num1 ** num2}")

# Comparison Operators ==, !=, >, <, >=, <=
print("\n--- Comparision Operator ---")
print(f"Equal To: {num1} == {num2} : {num1 == num2} ")
print(f"Not Equal To: {num1} != {num2} : {num1 != num2}")
print(f"Greater Than: {num1} > {num2} : {num1 > num2}")
print(f"Less Than: {num1} < {num2} : {num1 < num2}")
print(f"Greater Than Equal To: {num1} >= {num2} : {num1 >= num2}")
print(f"Less Than Equal To: {num1} <= {num2} : {num1 <= num2}")

# Logical Operators and, or, not
print("\n--- Logical Operators ---")
a = True
b = False
print(f"AND Operator: {a} and {b} : {a and b}")
print(f"OR Operator: {a} or {b} : {a or b}")
print(f"NOT Operator: not {a} : not {b}")

# Assignment Operators =, +=, -=, *=, /=
print("\n--- Assignment Operator ---")
x = num1
print(f"Equals: x = {num1}")

x += num2
print(f"Plus Equals: x += {num2} -> x = {x}")

x *= 2
print(f"Multiply Equals: x *= 2 -> x = {x}")

x /= 3
print(f"Divide Equals: x /= 3 -> x = {x}")