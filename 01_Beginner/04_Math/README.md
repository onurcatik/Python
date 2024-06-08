# Math
 

### Basic Arithmetic Operators

In Python, arithmetic operations can be performed using standard operators. Let's start with some basic operations:

**Addition**

To increment a variable by one:
```python
friends = 0
friends = friends + 1
print(friends)  # Output: 1

# Using augmented assignment operator
friends += 1
print(friends)  # Output: 2
```

**Subtraction**

To decrement a variable:
```python
friends = 2
friends = friends - 2
print(friends)  # Output: 0

# Using augmented assignment operator
friends -= 2
print(friends)  # Output: -2
```

**Multiplication**

To multiply a variable:
```python
friends = 5
friends = friends * 3
print(friends)  # Output: 15

# Using augmented assignment operator
friends *= 3
print(friends)  # Output: 45
```

**Division**

To divide a variable:
```python
friends = 10
friends = friends / 2
print(friends)  # Output: 5.0

# Using augmented assignment operator
friends /= 2
print(friends)  # Output: 2.5
```

**Exponentiation**

To raise a variable to a power:
```python
friends = 5
friends = friends ** 2
print(friends)  # Output: 25

# Using augmented assignment operator
friends **= 2
print(friends)  # Output: 625
```

**Modulus**

To find the remainder of a division:
```python
friends = 10
remainder = friends % 3
print(remainder)  # Output: 1
```

### Built-in Math Functions

Python provides several built-in functions for common mathematical operations.

**Round**

Rounds a number to the nearest integer:
```python
x = 3.14
result = round(x)
print(result)  # Output: 3
```

**Absolute Value**

Finds the absolute value of a number:
```python
y = -4
result = abs(y)
print(result)  # Output: 4
```

**Power**

Raises a number to a given power:
```python
y = 4
result = pow(y, 3)
print(result)  # Output: 64
```

**Maximum and Minimum**

Finds the maximum and minimum values:
```python
x = 3.14
y = 4
z = 5
result_max = max(x, y, z)
result_min = min(x, y, z)
print(result_max)  # Output: 5
print(result_min)  # Output: 3.14
```

### Math Module Functions and Constants

The `math` module provides more advanced mathematical functions and constants.

**Importing the Math Module**

```python
import math
```

**Pi and E Constants**

Accessing the values of Pi and E:
```python
print(math.pi)  # Output: 3.141592653589793
print(math.e)   # Output: 2.718281828459045
```

**Square Root**

Finding the square root of a number:
```python
x = 9
result = math.sqrt(x)
print(result)  # Output: 3.0
```

**Ceiling and Floor**

Rounding numbers up and down:
```python
x = 9.1
result_ceil = math.ceil(x)
print(result_ceil)  # Output: 10

x = 9.9
result_floor = math.floor(x)
print(result_floor)  # Output: 9
```

### Exercises

#### Exercise 1: Calculate the Circumference of a Circle

Formula: \(C = 2 \times \pi \times r\)

```python
import math

radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
circumference_rounded = round(circumference, 2)
print(f"The circumference is {circumference_rounded} centimeters")
```

#### Exercise 2: Calculate the Area of a Circle

Formula: \(A = \pi \times r^2\)

```python
import math

radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)
area_rounded = round(area, 2)
print(f"The area of the circle is {area_rounded} square centimeters")
```

#### Exercise 3: Calculate the Hypotenuse of a Right Triangle

Formula: \(c = \sqrt{a^2 + b^2}\)

```python
import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = math.sqrt(a**2 + b**2)
print(f"The hypotenuse is {c}")
```

This tutorial provides a solid foundation for performing various mathematical operations in Python. These concepts are essential for many programming tasks, and understanding them will enhance your ability to write efficient and effective code.