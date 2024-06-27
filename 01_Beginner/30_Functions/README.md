# Functions in Python

In Python, functions are essential building blocks that allow for reusable code. This tutorial will provide a thorough understanding of functions, their definitions, usage, and how to handle arguments and return values.

## Defining and Invoking Functions

### Definition

To define a function in Python, use the `def` keyword followed by the function name, parentheses `()`, and a colon `:`. The function body must be indented.

```python
def function_name():
    # Function body
    pass
```

### Example: Singing Happy Birthday

Consider a scenario where you need to sing "Happy Birthday" three times. Instead of repeating the code or using loops, you can use functions.

```python
def happy_birthday():
    print("Happy Birthday to You")
    print("Happy Birthday to You")
    print("Happy Birthday Dear [Name]")
    print("Happy Birthday to You")

# Invoking the function three times
happy_birthday()
happy_birthday()
happy_birthday()
```

### Invoking a Function

To invoke a function, type its name followed by parentheses.

```python
happy_birthday()
```

## Functions with Parameters and Arguments

### Parameters and Arguments

Parameters are placeholders for the values that a function operates on, while arguments are the actual values provided when the function is called.

### Example: Personalized Happy Birthday Song

Let's modify the `happy_birthday` function to include a parameter for the name.

```python
def happy_birthday(name):
    print(f"Happy Birthday to You")
    print(f"Happy Birthday to You")
    print(f"Happy Birthday Dear {name}")
    print(f"Happy Birthday to You")

# Invoking the function with different names
happy_birthday("Bro")
happy_birthday("Steve")
happy_birthday("Joe")
```

### Multiple Parameters

A function can have multiple parameters. For instance, if we want to include both a name and an age:

```python
def happy_birthday(name, age):
    print(f"Happy Birthday to You")
    print(f"Happy Birthday to You")
    print(f"Happy Birthday Dear {name}")
    print(f"Happy Birthday to You")
    print(f"You are {age} years old")

# Invoking the function with different names and ages
happy_birthday("Bro", 20)
happy_birthday("Steve", 30)
happy_birthday("Joe", 40)
```

### Positional and Keyword Arguments

The order of arguments matters, but you can also use keyword arguments to specify them in any order.

```python
happy_birthday(age=20, name="Bro")
```

## Return Statement

The `return` statement is used to end a function and send a result back to the caller.

### Example: Arithmetic Operations

Let's create functions for basic arithmetic operations that return results.

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Using the functions
result_add = add(1, 2)
result_subtract = subtract(1, 2)
result_multiply = multiply(1, 2)
result_divide = divide(1, 2)

print(result_add)        # Output: 3
print(result_subtract)   # Output: -1
print(result_multiply)   # Output: 2
print(result_divide)     # Output: 0.5
```

## Example: Complex Function with Return

Let's write a function to create a full name by capitalizing the first and last names and returning the full name.

```python
def create_full_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return f"{first_name} {last_name}"

# Using the function
full_name = create_full_name("spongebob", "squarepants")
print(full_name)  # Output: Spongebob Squarepants
```