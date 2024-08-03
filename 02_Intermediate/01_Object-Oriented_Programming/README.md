#  Python Object-Oriented Programming

## Introduction

Object-Oriented Programming (OOP) is a crucial concept in Python, enabling us to bundle related attributes and methods into objects. This tutorial provides a detailed exploration of Python's OOP, focusing on creating and manipulating objects and classes.

## Objects and Classes

In Python, an **object** is a collection of related attributes and methods. Attributes are variables that describe the object's properties, and methods are functions that describe the object's behavior. To illustrate, consider real-world objects: a phone, a cup, and a book. Each has distinct attributes and methods.

### Example: Real-World Objects

1. **Phone**
   - **Attributes**: version number, power status, price.
   - **Methods**: make a call, receive a call, turn on, turn off.

2. **Cup**
   - **Attributes**: liquid content, temperature, is it empty.
   - **Methods**: fill, drink, empty.

3. **Book**
   - **Attributes**: title, number of pages.
   - **Methods**: open, read, close.

### Defining a Class

A **class** is a blueprint for creating objects. It defines the structure and behavior (attributes and methods) that the objects created from the class will have.

```python
class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
```

### Creating Objects

To create an object, we instantiate the class and provide the required attributes.

```python
# Creating car objects
car1 = Car("Mustang", 2024, "Red", False)
car2 = Car("Corvette", 2025, "Blue", True)
car3 = Car("Charger", 2026, "Yellow", True)

# Accessing attributes
print(car1.model)  # Output: Mustang
print(car2.year)   # Output: 2025
print(car3.color)  # Output: Yellow
```

### Using Methods

Methods define what an object can do. We can call these methods to perform actions.

```python
# Using methods
car1.drive()   # Output: You drive the Red Mustang
car1.stop()    # Output: You stop the Red Mustang
car2.describe() # Output: 2025 Blue Corvette
```

## Organizing Code

For better organization, classes can be placed in separate Python files and imported as modules.

```python
# car.py
class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

# main.py
from car import Car

car1 = Car("Mustang", 2024, "Red", False)
car1.drive()   # Output: You drive the Red Mustang
```

