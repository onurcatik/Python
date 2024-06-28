# Python Keyword Arguments

## Introduction

Keyword arguments in Python are a powerful feature that enhances code readability and flexibility. This tutorial aims to provide a thorough understanding of keyword arguments, their benefits, and their usage. We will cover the following topics:
- Definition of keyword arguments
- Benefits of keyword arguments
- Examples demonstrating keyword arguments
- Mixing positional and keyword arguments
- Practical use cases in built-in functions
- Exercise: Creating a function using keyword arguments

## Definition of Keyword Arguments

In Python, a keyword argument is an argument that is preceded by an identifier (parameter name) in a function call. This allows you to pass arguments to a function using the parameter names rather than just their order.

### Syntax
```python
def function_name(param1, param2):
    # function body
    pass

# Using keyword arguments
function_name(param1=value1, param2=value2)
```

## Benefits of Keyword Arguments

1. **Readability**: Keyword arguments improve the readability of your code by explicitly stating what each argument represents.
2. **Order Independence**: The order of arguments does not matter when using keyword arguments, allowing for more flexible function calls.

## Examples

### Basic Function with Positional Arguments

Consider a simple function that prints a greeting message:

```python
def hello(greeting, title, first_name, last_name):
    print(f"{greeting}, {title} {first_name} {last_name}")

# Using positional arguments
hello("Hello", "Mr.", "SpongeBob", "SquarePants")
```

Output:
```
Hello, Mr. SpongeBob SquarePants
```

### Switching to Keyword Arguments

Using keyword arguments, we can call the same function without worrying about the order of the arguments:

```python
hello(greeting="Hello", title="Mr.", first_name="SpongeBob", last_name="SquarePants")

# Changing the order of keyword arguments
hello(last_name="SquarePants", first_name="SpongeBob", greeting="Hello", title="Mr.")
```

Output:
```
Hello, Mr. SpongeBob SquarePants
Hello, Mr. SpongeBob SquarePants
```

## Mixing Positional and Keyword Arguments

When mixing positional and keyword arguments, positional arguments must come first:

```python
# Correct usage
hello("Hello", title="Mr.", first_name="SpongeBob", last_name="SquarePants")

# Incorrect usage (will raise a SyntaxError)
hello(title="Mr.", first_name="SpongeBob", last_name="SquarePants", "Hello")
```

## Practical Use Cases in Built-in Functions

### `print` Function

The `print` function in Python has several keyword arguments, such as `end` and `sep`.

#### Using the `end` Argument

By default, `print` ends with a newline character. You can change this using the `end` keyword argument:

```python
for i in range(1, 6):
    print(i, end=" ")
```

Output:
```
1 2 3 4 5 
```

#### Using the `sep` Argument

The `sep` keyword argument specifies the separator between multiple values:

```python
print("1", "2", "3", "4", "5", sep="-")
```

Output:
```
1-2-3-4-5
```

## Exercise: Creating a Function with Keyword Arguments

Let's create a function that generates a formatted phone number. The function will accept a country code, area code, first three digits, and last four digits.

### Function Definition

```python
def get_phone_number(country_code, area_code, first_digits, last_digits):
    return f"{country_code}-{area_code}-{first_digits}-{last_digits}"
```

### Function Call with Keyword Arguments

```python
phone_num = get_phone_number(country_code="1", area_code="123", first_digits="456", last_digits="7890")
print(phone_num)
```

Output:
```
1-123-456-7890
```

By using keyword arguments, we ensure the function call is clear and unambiguous, enhancing readability and maintainability.

