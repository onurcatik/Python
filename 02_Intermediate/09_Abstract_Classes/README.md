# Python Abstract Classes: A Comprehensive Guide

Abstract classes in Python serve as blueprints for other classes. They encapsulate a set of behaviors that their derived classes are expected to implement. In this tutorial, we will delve into the concept of abstract classes, their purpose, and how they enforce a contract for subclass implementations.

## What Are Abstract Classes?

An abstract class is a class that cannot be instantiated on its own. It is intended to be a parent class, from which other classes derive. The primary purpose of an abstract class is to define a common interface for all its subclasses. It can contain one or more abstract methods—methods that are declared, but not implemented, in the abstract class. These methods must be overridden in any non-abstract child class.

### Why Use Abstract Classes?

Abstract classes offer several advantages:

- **Enforcing a Contract**: They ensure that all subclasses implement the necessary methods, which helps maintain consistency across different classes.
- **Preventing Instantiation of Incomplete Classes**: Since abstract classes are incomplete by design, attempting to instantiate them directly results in an error. This prevents accidental creation of objects from classes that are not fully implemented.

### Implementing Abstract Classes in Python

Python provides the `ABC` module (Abstract Base Classes) in the `abc` package to define abstract classes. Below is a step-by-step guide to implementing abstract classes.

### Step 1: Importing Required Modules

First, we need to import the necessary modules from the `abc` package:

```python
from abc import ABC, abstractmethod
```

- `ABC`: This is the base class for defining abstract classes.
- `abstractmethod`: This decorator is used to declare a method as abstract.

### Step 2: Defining an Abstract Class

Let's define an abstract class called `Vehicle`. This class will have two abstract methods: `go` and `stop`.

```python
class Vehicle(ABC):

    @abstractmethod
    def go(self):
        """Method to move the vehicle"""
        pass

    @abstractmethod
    def stop(self):
        """Method to stop the vehicle"""
        pass
```

In this example:
- `Vehicle` inherits from `ABC`, making it an abstract class.
- The `go` and `stop` methods are decorated with `@abstractmethod`, meaning they must be implemented by any non-abstract subclass.

### Step 3: Demonstrating Non-Instantiation of Abstract Classes

Attempting to instantiate the `Vehicle` class will result in a `TypeError` because it contains abstract methods:

```python
# This will raise a TypeError
vehicle = Vehicle()
```

Error message:
```
TypeError: Can't instantiate abstract class Vehicle with abstract methods go, stop
```

### Step 4: Creating Subclasses

Now, let's create subclasses that inherit from `Vehicle`. These subclasses must implement the `go` and `stop` methods.

#### Example 1: Car Class

```python
class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")
```

#### Example 2: Motorcycle Class

```python
class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")
```

#### Example 3: Boat Class

```python
class Boat(Vehicle):

    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")
```

### Step 5: Testing the Subclasses

Now, let's create instances of these subclasses and call their methods:

```python
car = Car()
car.go()    # Output: You drive the car
car.stop()  # Output: You stop the car

motorcycle = Motorcycle()
motorcycle.go()    # Output: You ride the motorcycle
motorcycle.stop()  # Output: You stop the motorcycle

boat = Boat()
boat.go()    # Output: You sail the boat
boat.stop()  # Output: You anchor the boat
```

### Ensuring Completeness

If a subclass does not implement all abstract methods, Python will prevent its instantiation. For example, if the `Boat` class omitted the `stop` method, an attempt to create a `Boat` object would result in a `TypeError`.

```python
# Example of missing implementation
class IncompleteBoat(Vehicle):

    def go(self):
        print("You sail the boat")

# This will raise a TypeError
incomplete_boat = IncompleteBoat()
```

Error message:
```
TypeError: Can't instantiate abstract class IncompleteBoat with abstract methods stop
```

### Conclusion

Abstract classes in Python provide a powerful way to enforce a consistent interface across multiple classes. They ensure that derived classes implement specific methods, preventing the creation of incomplete objects. By using the `ABC` module and `abstractmethod` decorator, developers can design robust and maintainable object-oriented systems.

This tutorial has demonstrated how to define abstract classes, enforce method implementation in subclasses, and ensure code completeness and correctness. Abstract classes are an essential tool for designing well-structured Python applications.