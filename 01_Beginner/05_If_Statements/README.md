# If Statements


## Basics of If Statements

An if statement in Python evaluates a condition and executes a block of code if the condition is true. If the condition is false, the code block is skipped.

### Example 1: Basic If Statement

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up.")
```

In this example:
- The `input` function prompts the user to enter their age, which is then typecast to an integer.
- The if statement checks if the user's age is greater than or equal to 18.
- If the condition is true, the message "You are now signed up" is printed.

### Example 2: If-Else Statement

An if-else statement allows us to execute one block of code if the condition is true and another block if the condition is false.

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up.")
else:
    print("You must be 18+ to sign up.")
```

In this example:
- If the user's age is 18 or older, they are signed up.
- If the user's age is less than 18, a different message is printed.

### Example 3: If-Elif-Else Statement

An if-elif-else statement allows us to check multiple conditions before reaching the final else statement.

```python
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up.")
elif age >= 18:
    print("You are now signed up.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You must be 18+ to sign up.")
```

In this example:
- The first condition checks if the age is 100 or more.
- The second condition checks if the age is between 18 and 99.
- The third condition checks if the age is less than 0.
- The else block catches any age values that do not meet the previous conditions.

## Logical Operators in If Statements

Python allows the use of logical operators such as `and`, `or`, and `not` to combine multiple conditions in an if statement.

### Example 4: Using Logical Operators

```python
age = int(input("Enter your age: "))
has_permission = input("Do you have parental permission? (y/n): ").lower() == 'y'

if age >= 18 or has_permission:
    print("You are now signed up.")
else:
    print("You must be 18+ or have parental permission to sign up.")
```

In this example:
- The `or` operator is used to check if the user is 18 or older or has parental permission.

## Boolean Variables in If Statements

Boolean variables (variables that are either `True` or `False`) can be used directly in if statements without the need for comparison.

### Example 5: Using Boolean Variables

```python
for_sale = True

if for_sale:
    print("This item is for sale.")
else:
    print("This item is not for sale.")
```

In this example:
- The boolean variable `for_sale` is used directly in the if statement.

## Common Mistakes and Best Practices

1. **Indentation**: Ensure that the code block inside the if, elif, and else statements is properly indented.
2. **Comparison Operators**: Use `==` for equality checks, not `=` which is an assignment operator.
3. **Order of Conditions**: Pay attention to the order of conditions in if-elif-else chains to ensure logical flow and correctness.

### Example 6: Handling Empty Input

```python
name = input("Enter your name: ")

if name == "":
    print("You did not type in your name.")
else:
    print(f"Hello, {name}")
```

In this example:
- The if statement checks if the `name` variable is an empty string and responds accordingly.

