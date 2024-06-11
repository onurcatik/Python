# Logical Operators 


## Logical Operators Overview

### `and` Operator

The `and` operator evaluates to `True` if and only if both operands are `True`. If either operand is `False`, the entire expression evaluates to `False`. This operator is particularly useful when checking if multiple conditions are met simultaneously.

### `or` Operator

The `or` operator evaluates to `True` if at least one of the operands is `True`. It only evaluates to `False` when both operands are `False`. This operator is useful when you need to check if at least one condition is met.

### `not` Operator

The `not` operator is a unary operator that inverts the boolean value of its operand. If the operand is `True`, applying `not` will make it `False`, and vice versa. This operator is useful for toggling boolean conditions.

## Detailed Examples and Code Snippets

### Example 1: Using the `and` Operator

Consider a program to check if the temperature falls within a specific range. We want to print a message indicating whether the temperature is good or bad based on the given range.

```python
temp = 25  # Temperature in Celsius

if temp > 0 and temp < 30:
    print("The temperature is good.")
else:
    print("The temperature is bad.")
```

**Explanation:**

- The condition `temp > 0 and temp < 30` uses the `and` operator to check if the temperature is between 0 and 30 degrees Celsius.
- If both conditions are `True`, the message "The temperature is good." is printed.
- Otherwise, the message "The temperature is bad." is printed.

Let's test this with different temperatures:

```python
temp = -10
if temp > 0 and temp < 30:
    print("The temperature is good.")
else:
    print("The temperature is bad.")
# Output: The temperature is bad.

temp = 40
if temp > 0 and temp < 30:
    print("The temperature is good.")
else:
    print("The temperature is bad.")
# Output: The temperature is bad.
```

### Example 2: Using the `or` Operator

Next, let's use the `or` operator to check if the temperature falls outside a specific range.

```python
temp = 40  # Temperature in Celsius

if temp <= 0 or temp >= 30:
    print("The temperature is bad.")
else:
    print("The temperature is good.")
```

**Explanation:**

- The condition `temp <= 0 or temp >= 30` uses the `or` operator to check if the temperature is less than or equal to 0 or greater than or equal to 30 degrees Celsius.
- If at least one condition is `True`, the message "The temperature is bad." is printed.
- Otherwise, the message "The temperature is good." is printed.

Let's test this with different temperatures:

```python
temp = -15
if temp <= 0 or temp >= 30:
    print("The temperature is bad.")
else:
    print("The temperature is good.")
# Output: The temperature is bad.

temp = 20
if temp <= 0 or temp >= 30:
    print("The temperature is bad.")
else:
    print("The temperature is good.")
# Output: The temperature is good.
```

### Example 3: Using the `not` Operator

Now, let's explore the `not` operator with a boolean variable. We'll check if it is sunny outside and print a corresponding message.

```python
sunny = True  # Boolean variable indicating if it is sunny

if sunny:
    print("It is sunny outside.")
else:
    print("It is cloudy outside.")
```

**Explanation:**

- If `sunny` is `True`, the message "It is sunny outside." is printed.
- If `sunny` is `False`, the message "It is cloudy outside." is printed.

Using the `not` operator, we can invert the condition:

```python
sunny = False  # Boolean variable indicating if it is sunny

if not sunny:
    print("It is cloudy outside.")
else:
    print("It is sunny outside.")
```

**Explanation:**

- The condition `not sunny` inverts the value of `sunny`.
- If `sunny` is `False`, the message "It is cloudy outside." is printed.
- If `sunny` is `True`, the message "It is sunny outside." is printed.

