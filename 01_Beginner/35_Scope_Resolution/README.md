# What is Python Scope Resolution? 🔬

## Introduction

In Python, scope resolution refers to the process of finding the value of a variable based on its scope. The concept of scope determines where a variable can be accessed within the code. Python uses a specific order called the LEGB rule to resolve the scope of variables: Local, Enclosed, Global, and Built-in.

## Variable Scope

Variable scope defines where a variable is visible and accessible. In Python, variables can have different scopes based on where they are defined.

### Local Scope

A variable declared within a function is said to have local scope. This means the variable is only accessible within that function.

```python
def function_one():
    a = 1
    print(a)  # Output: 1

def function_two():
    b = 2
    print(b)  # Output: 2

function_one()
function_two()
```

In this example:
- `a` is local to `function_one`.
- `b` is local to `function_two`.

### Enclosed Scope

Enclosed scope refers to variables in the enclosing function's scope. This occurs when a function is nested within another function.

```python
def outer_function():
    x = 1

    def inner_function():
        print(x)  # Output: 1

    inner_function()

outer_function()
```

Here, `x` is in the enclosed scope of `inner_function`.

### Global Scope

Variables declared outside any function have a global scope. These variables are accessible from any function within the module.

```python
x = 3

def function_one():
    print(x)  # Output: 3

def function_two():
    print(x)  # Output: 3

function_one()
function_two()
```

In this case, `x` is in the global scope and is accessible by both `function_one` and `function_two`.

### Built-in Scope

Built-in scope refers to the names that are preassigned in Python. For example, the `math` module contains the exponential constant `e`.

```python
from math import e

def function_one():
    print(e)  # Output: 2.718281828459045

function_one()
```

## Scope Resolution: The LEGB Rule

Python resolves variables using the LEGB rule, which stands for Local, Enclosed, Global, and Built-in. This rule defines the order in which Python looks for variable values.

### Example of the LEGB Rule

Consider the following example:

```python
e = 3

def outer_function():
    x = 1

    def inner_function():
        print(x)  # Output: 1

    inner_function()

def function_with_built_in():
    from math import e
    print(e)  # Output: 2.718281828459045

outer_function()
function_with_built_in()
print(e)  # Output: 3
```

In this code:
- `inner_function` finds `x` in the enclosed scope of `outer_function`.
- `function_with_built_in` finds `e` from the `math` module due to the import statement, overriding the global `e`.
- The global `e` remains accessible outside of functions.

## Conclusion

Variable scope in Python defines where a variable is accessible. Python uses the LEGB rule to resolve variable scopes:
- **Local**: Variables defined within a function.
- **Enclosed**: Variables in the scope of the enclosing function.
- **Global**: Variables defined at the top level of a module or script.
- **Built-in**: Predefined variables in Python.

