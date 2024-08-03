# Python MULTIPLE INHERITANCE🐟

## Introduction
In this tutorial, we will explore the concepts of multiple and multi-level inheritance in Python. These are advanced features of object-oriented programming that allow a class to inherit from more than one parent class (multiple inheritance) or from a hierarchy of classes (multi-level inheritance).

### Multiple Inheritance
Multiple inheritance occurs when a child class inherits from more than one parent class. This allows the child class to utilize properties and methods from multiple sources.

### Multi-Level Inheritance
Multi-level inheritance occurs when a class is derived from a class that is also derived from another class. This creates a chain of inheritance.

## Example of Multiple Inheritance

Let's start by implementing multiple inheritance with an example involving animals.

### Step 1: Define Parent Classes
We will create two parent classes: `Prey` and `Predator`.

```python
class Prey:
    def flee(self):
        print("This animal is fleeing.")

class Predator:
    def hunt(self):
        print("This animal is hunting.")
```

### Step 2: Define Child Classes
Next, we will create three child classes: `Rabbit`, `Hawk`, and `Fish`. Each child class will inherit from one or both of the parent classes.

```python
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass
```

### Step 3: Instantiate and Test Objects
We will create instances of each class and test their inherited methods.

```python
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()  # Output: This animal is fleeing.
# rabbit.hunt()  # AttributeError: 'Rabbit' object has no attribute 'hunt'

hawk.hunt()  # Output: This animal is hunting.
# hawk.flee()  # AttributeError: 'Hawk' object has no attribute 'flee'

fish.flee()  # Output: This animal is fleeing.
fish.hunt()  # Output: This animal is hunting.
```

### Explanation
- `Rabbit` inherits from `Prey`, so it can flee.
- `Hawk` inherits from `Predator`, so it can hunt.
- `Fish` inherits from both `Prey` and `Predator`, so it can both flee and hunt.

## Example of Multi-Level Inheritance

Next, let's explore multi-level inheritance by adding another layer of inheritance.

### Step 1: Define a Grandparent Class
We will create a new class called `Animal` which will be the parent class for `Prey` and `Predator`.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")
```

### Step 2: Modify Parent Classes to Inherit from Animal
We will update the `Prey` and `Predator` classes to inherit from `Animal`.

```python
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")
```

### Step 3: Modify Child Classes
Update the child classes to utilize the constructor from the `Animal` class.

```python
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass
```

### Step 4: Instantiate and Test Objects
Create instances of each class with names and test all inherited methods.

```python
rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()  # Output: Bugs is eating.
rabbit.sleep()  # Output: Bugs is sleeping.
rabbit.flee()  # Output: Bugs is fleeing.

hawk.eat()  # Output: Tony is eating.
hawk.sleep()  # Output: Tony is sleeping.
hawk.hunt()  # Output: Tony is hunting.

fish.eat()  # Output: Nemo is eating.
fish.sleep()  # Output: Nemo is sleeping.
fish.flee()  # Output: Nemo is fleeing.
fish.hunt()  # Output: Nemo is hunting.
```

### Explanation
- `Animal` class provides the basic methods `eat` and `sleep`.
- `Prey` and `Predator` classes inherit from `Animal` and add their specific methods `flee` and `hunt`.
- `Rabbit`, `Hawk`, and `Fish` inherit from `Prey` and/or `Predator`, thus gaining access to all methods in the hierarchy.

## Conclusion
In Python, multiple inheritance allows a class to inherit from more than one parent class, while multi-level inheritance enables a class to inherit from a parent class which in turn inherits from another class. These inheritance models provide a powerful way to reuse and organize code, but they should be used judiciously to maintain clarity and simplicity in the codebase.

In summary:
- **Multiple Inheritance**: A class can inherit from more than one parent class.
- **Multi-Level Inheritance**: A class can inherit from a parent class, which in turn inherits from another class.

By understanding and implementing these concepts, developers can create more flexible and reusable code structures in their Python applications.