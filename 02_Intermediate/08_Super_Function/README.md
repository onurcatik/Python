# SUPER() in Python Explained

## Introduction

In object-oriented programming (OOP), the concept of inheritance allows a class (known as the child or subclass) to inherit attributes and methods from another class (known as the parent or superclass). Python, being an object-oriented language, supports inheritance and provides a built-in function called `super()` to enhance the functionality of inherited methods. This tutorial will delve into the details of the `super()` function, how it works, and why it is a crucial tool in Python programming.

## Understanding the `super()` Function

The `super()` function in Python is used within a child class to call methods from its parent class. This function plays a vital role when you want to extend or customize the functionality of an inherited method without completely overriding it. By using `super()`, you can build upon the existing functionality of the superclass's methods while adding or modifying features in the subclass.

### Basic Concept of Inheritance

Before diving into `super()`, it's essential to understand the basic concept of inheritance:

- **Parent Class (Superclass):** The class from which properties and methods are inherited.
- **Child Class (Subclass):** The class that inherits properties and methods from the parent class.

### Example of Inheritance Without `super()`

Let's start with a basic example to illustrate inheritance:

```python
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        # Directly assigning inherited attributes
        self.color = color
        self.is_filled = is_filled
        self.radius = radius
```

In this example, the `Circle` class inherits from the `Shape` class. However, we manually assign the `color` and `is_filled` attributes within the `Circle` class, duplicating the code that already exists in the parent class. This approach is prone to errors and violates the DRY (Don't Repeat Yourself) principle.

### Enhancing the Example with `super()`

To avoid code duplication and follow best practices, we can use the `super()` function to call the constructor of the parent class:

```python
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        # Using super() to call the parent class constructor
        super().__init__(color, is_filled)
        self.radius = radius
```

With this approach, `super()` takes care of initializing the `color` and `is_filled` attributes, while the `Circle` class focuses on its specific attributes, such as `radius`.

### Full Example: Shapes with `super()`

Let's create a complete example using three different shapes: `Circle`, `Square`, and `Triangle`. Each shape will have its own attributes, but they will share the common attributes `color` and `is_filled`, inherited from the `Shape` class.

```python
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
```

### Creating and Testing Objects

Now, let's create objects of each shape and verify that the attributes are correctly assigned:

```python
# Creating a Circle object
circle = Circle(color="red", is_filled=True, radius=5)
print(f"Circle: Color={circle.color}, Is Filled={circle.is_filled}, Radius={circle.radius} cm")

# Creating a Square object
square = Square(color="blue", is_filled=False, width=6)
print(f"Square: Color={square.color}, Is Filled={square.is_filled}, Width={square.width} cm")

# Creating a Triangle object
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)
print(f"Triangle: Color={triangle.color}, Is Filled={triangle.is_filled}, Width={triangle.width} cm, Height={triangle.height} cm")
```

The output will be:

```
Circle: Color=red, Is Filled=True, Radius=5 cm
Square: Color=blue, Is Filled=False, Width=6 cm
Triangle: Color=yellow, Is Filled=True, Width=7 cm, Height=8 cm
```

### Extending Functionality with `super()`

In addition to calling the parent class's constructor, `super()` can also be used to extend the functionality of inherited methods. Let's add a `describe()` method in the `Shape` class, which describes the attributes of the shape.

```python
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        return f"Color: {self.color}, Filled: {'Yes' if self.is_filled else 'No'}"
```

We can then override this method in the child classes to provide more specific descriptions, while still calling the parent class's `describe()` method using `super()`.

```python
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        description = super().describe()
        return f"{description}, Radius: {self.radius} cm"

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        description = super().describe()
        return f"{description}, Width: {self.width} cm"

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        description = super().describe()
        return f"{description}, Width: {self.width} cm, Height: {self.height} cm"
```

Testing these methods:

```python
print(circle.describe())
print(square.describe())
print(triangle.describe())
```

The output will be:

```
Color: red, Filled: Yes, Radius: 5 cm
Color: blue, Filled: No, Width: 6 cm
Color: yellow, Filled: Yes, Width: 7 cm, Height: 8 cm
```

### Method Overriding and Extending

When a child class defines a method with the same name as a method in the parent class, this is known as method overriding. The child's version of the method takes precedence. However, using `super()`, you can extend the functionality of the parent class's method, as demonstrated above.

