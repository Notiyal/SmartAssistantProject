# Smart Assistant Project (Python Project Tutorial)

This is a **step-by-step tutorial project** in Python.  
Each step introduces **one Python concept** and builds on the previous step, so by the end you’ll have a **Smart Personal Assistant** with features like AI, Data Analysis, BI, and Excel automation.

---

## 📂 Steps

### ✅ [Step 1: Hello World & User Input](Step01_Hello_World\hello_world.py)
**Concepts Covered:**
- Printing messages (`print`)
- Taking user input (`input`)
- f-strings for string formatting

**How to Run:**
```bash ```
python Step01_Hello_World\hello_world.py


### ✅ [Step 2: Variable & Data Types](Step02_Variable_DataTypes\variable_datatypes.py)

**Concepts Covered:**
- Variables
- Data Types: str, int, float, bool
- Type conversion with int()
- Boolean conversion from string
- f-strings for formatted output

**How to Run:**
```bash```
python Step02_Variable_DataTypes\variable_datatypes.py


### ✅ [Step 3: Operators](Step03_Operators\operators.py)
**Concepts Covered:**
- Arithmetic Operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparison Operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical Operators: `and`, `or`, `not`
- Assignment Operators: `=`, `+=`, `-=`, `*=`, `/=`

**How to Run:**
```bash```
python Step03_Operators\operators.py


### ✅ [Step 4: Conditionals](Step04_Conditionals\conditionals.py)
**Concepts Covered:**
- if statement
- if…else
- if…elif…else
- Nested conditionals

**How to Run:**
```bash```
python Step04_Conditionals\conditionals.py

### ✅ [Step 5: Loops (for, while)] (Step05_Loops\loops.py)

In this step, we learn how to repeat actions using **for** and **while** loops.

### 🔹 Code Highlights
- **For loop** → repeats a fixed number of times (`range(1,6)` counts 1 to 5).
- **While loop** → keeps running until a condition is met (`exit` keyword stops it).

**How to Run:**
```bash```
python Step05_Loops\loops.py

### ✅ [Step 6: Lists](Step06_Lists\lists.py)

**Concepts Covered:**
- Creating and accessing lists
- Adding and removing items (`append`, `remove`, `pop`)
- Looping through a list
- Counting items with `len()`
- Taking user input to dynamically **add or remove tasks**

**How to Run:**
```bash```
python Step06_Lists\lists.py

### ✅ [Step 7: Tuples](Step07_Tuples\tuples.py)

**Concepts Covered:**
- Creating tuples
- Accessing tuple elements
- Tuple unpacking
- Immutability of tuples (cannot change values)
- Taking **user input** and storing profile in a tuple

**How to Run:**
```bash```
python Step07_Tuples\tuples.py

### ✅ [Step 8: Dictionaries](Step08_Dictionaries\dictionaries.py)
- Create a user profile with name, age, city, and email (entered by user).
- Update profile details (e.g., age).
- Optionally remove city.
- Task manager:
  - Add a new task.
  - Remove a task by its number.
- Shows how dictionaries can store structured information.

**How to Run:**
```bash```
python Step08_Dictionaries\dictionaries.py



### ✅ [Step 9: Functions] (Step09_Functions\functions.py)
- Define reusable blocks of code using `def`.
- Functions can:
  - Take inputs (parameters).
  - Return outputs (values).
- Example:
  - `greet_user()` prints a welcome message.
  - `create_profile()` asks user details and returns a dictionary.


**How to Run:**
```bash``
python Step09_Functions\functions.py

### ✅ [Step 9_1: Dictionaries Refactored with Functions](Step09_Functions\profile_manager.py)
- Reused Step 8 (Profile Manager) but made it cleaner with **functions**:
  - `create_profile()` → creates dictionary from user input.
  - `display_profile()` → shows profile neatly.
  - `add_data()`, `update_data()`, `delete_data()` → manage dictionary.
- Single menu loop for user actions.
- Demonstrates **functions + dictionaries** working together.

**How to Run:**
```bash``
python Step09_Functions\profile_manager.py

### ✅ [Step 10: Functions] (Step10_Loops_Functions\task_manager_refactor.py)
🧠 Concepts Covered

- Creating and calling functions
- Passing and returning values
- Using loops inside functions
- Menu-driven user interface
  
**How to Run:**
```bash``
python Step10_Loops_Functions\task_manager_refactor.py
