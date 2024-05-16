
# Type Casting

In this tutorial, we're diving into the world of type casting in Python. Type casting is the process of converting a value of one data type to another. Whether you're converting integers to floats, strings to booleans, or any other combination, Python makes it straightforward and flexible. So, let's get started!

**Explicit Type Casting:**

First, let's explore explicit type casting. This involves manually converting a value or variable into a different data type using specific casting functions.

**1. String, Integer, Float, and Boolean:**

```python
# Define variables of different data types
name = "John"  # String
age = 25      # Integer
GPA = 3.5     # Float
student = True  # Boolean

# Printing the data types of variables
print("Type of name:", type(name))  # Output: <class 'str'>
print("Type of age:", type(age))    # Output: <class 'int'>
print("Type of GPA:", type(GPA))    # Output: <class 'float'>
print("Type of student:", type(student))  # Output: <class 'bool'>
```

**2. Converting to Float:**

```python
# Convert age to a float
age = 25
age = float(age)
print("Age as float:", age)  # Output: Age as float: 25.0
```

**3. Converting to Integer:**

```python
# Convert GPA to an integer
GPA = 3.5
GPA = int(GPA)
print("GPA as integer:", GPA)  # Output: GPA as integer: 3
```

**4. Converting to String:**

```python
# Convert student to a string
student = True
student = str(student)
print("Student as string:", student)  # Output: Student as string: True
```

**5. Converting to Boolean:**

```python
# Convert age to a boolean
age = 25
age = bool(age)
print("Age as boolean:", age)  # Output: Age as boolean: True
```

---

**Implicit Type Casting:**

Now, let's delve into implicit type casting. Python performs implicit type casting automatically when certain operations are carried out, such as arithmetic expressions.

**1. Arithmetic Operations:**

```python
# Implicit type casting in arithmetic operations
x = 10
y = 2.0
x = x / y
print("Result of division:", x)  # Output: Result of division: 5.0
```

In this example, even though `x` was initially an integer, it gets implicitly converted to a float when divided by a float (`y`).
