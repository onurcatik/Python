# Python CLASS VARIABLES Explained

In this tutorial, we will explore class variables in Python. Class variables are a powerful feature that allows data to be shared among all instances of a class. We will delve into the distinction between class variables and instance variables, and how to effectively use class variables in your Python classes.

## Class Variables vs. Instance Variables

Class variables are defined outside the constructor and are shared among all instances of a class. This means that any modification to a class variable affects all instances of that class. In contrast, instance variables are defined inside the constructor and each instance of the class has its own separate copy of these variables.

### Example: Student Class

Let's create a `Student` class to illustrate the use of class variables and instance variables.

```python
class Student:
    # Class variable
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age  # Instance variable
        Student.num_students += 1  # Increment class variable

# Creating student objects
student1 = Student("SpongeBob", 30)
student2 = Student("Patrick", 35)

# Accessing instance variables
print(f"{student1.name} is {student1.age} years old.")
print(f"{student2.name} is {student2.age} years old.")

# Accessing class variables
print(f"{student1.name} is graduating in the year {Student.class_year}.")
print(f"{student2.name} is graduating in the year {Student.class_year}.")
print(f"Number of students: {Student.num_students}")
```

### Explanation

1. **Class Variables**: `class_year` and `num_students` are class variables. They are defined outside the constructor and are shared among all instances of the `Student` class.
2. **Instance Variables**: `name` and `age` are instance variables. They are defined inside the constructor and each instance of the `Student` class has its own separate copy of these variables.

### Output
```
SpongeBob is 30 years old.
Patrick is 35 years old.
SpongeBob is graduating in the year 2024.
Patrick is graduating in the year 2024.
Number of students: 2
```

## Best Practices

When working with class variables, it is recommended to access them using the class name rather than an instance of the class. This makes it clear that the variable is a class variable and not an instance variable.

### Example

```python
print(f"{student1.name} is graduating in the year {Student.class_year}.")
print(f"Number of students: {Student.num_students}")
```

This approach enhances clarity and readability, making it explicit that `class_year` and `num_students` are class variables.

## Modifying Class Variables

Class variables can be modified, and the changes will be reflected across all instances of the class.

### Example

Let's create a few more student objects and demonstrate how the class variables are affected.

```python
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

# Accessing class variables after creating more student objects
print(f"Number of students: {Student.num_students}")
print(f"Class year: {Student.class_year}")

# Printing all student names
print(f"Student names: {student1.name}, {student2.name}, {student3.name}, {student4.name}")
```

### Output
```
Number of students: 4
Class year: 2024
Student names: SpongeBob, Patrick, Squidward, Sandy
```

## Changing Class Variables

If we change the value of a class variable, it will be updated for all instances of the class.

### Example

```python
Student.class_year = 2025

print(f"{student1.name} is graduating in the year {Student.class_year}.")
print(f"{student2.name} is graduating in the year {Student.class_year}.")
print(f"{student3.name} is graduating in the year {Student.class_year}.")
print(f"{student4.name} is graduating in the year {Student.class_year}.")
```

### Output
```
SpongeBob is graduating in the year 2025.
Patrick is graduating in the year 2025.
Squidward is graduating in the year 2025.
Sandy is graduating in the year 2025.
```

