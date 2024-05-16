# Explicit Type Casting
print("Explicit Type Casting:")
print("----------------------")

# Define variables of different data types
name = "John"  # String
age = 25       # Integer
GPA = 3.5      # Float
student = True # Boolean

# Printing the data types of variables
print("Type of name:", type(name))     # Output: <class 'str'>
print("Type of age:", type(age))       # Output: <class 'int'>
print("Type of GPA:", type(GPA))       # Output: <class 'float'>
print("Type of student:", type(student))  # Output: <class 'bool'>

# Convert age to a float
age = float(age)
print("Age as float:", age)            # Output: Age as float: 25.0

# Convert GPA to an integer
GPA = int(GPA)
print("GPA as integer:", GPA)          # Output: GPA as integer: 3

# Convert student to a string
student = str(student)
print("Student as string:", student)   # Output: Student as string: True

# Convert age to a boolean
age = bool(age)
print("Age as boolean:", age)          # Output: Age as boolean: True

print("\nImplicit Type Casting:")
print("----------------------")

# Implicit Type Casting
# Arithmetic Operations
x = 10
y = 2.0
x = x / y
print("Result of division:", x)        # Output: Result of division: 5.0
