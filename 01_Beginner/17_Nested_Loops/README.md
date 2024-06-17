# Nested Loops in Python


## Understanding Nested Loops

A nested loop occurs when a loop is placed inside the code of another loop. The outer loop encapsulates the inner loop, and each iteration of the outer loop triggers the complete cycle of the inner loop.

### Types of Nested Loops

In Python, nested loops can be of different types:
1. **A `for` loop inside another `for` loop**
2. **A `while` loop inside another `while` loop**
3. **A `for` loop inside a `while` loop**
4. **A `while` loop inside a `for` loop**

The type of loop used depends on the specific requirements of the problem being solved.

## Example of Nested Loops

### Displaying Numbers 1 to 9

Let's start with a basic example: displaying numbers from 1 to 9 using a `for` loop.

```python
for x in range(1, 10):
    print(x, end=' ')
```

This code snippet uses a `for` loop to iterate through numbers from 1 to 9. The `end=' '` argument in the `print` function ensures that the numbers are printed on the same line, separated by a space.

### Repeating the Sequence Three Times

To repeat the sequence three times, we can use another loop (the outer loop) to encapsulate the existing loop (the inner loop):

```python
for i in range(3):
    for x in range(1, 10):
        print(x, end=' ')
    print()  # Prints a newline after each complete iteration of the inner loop
```

In this code:
- The outer loop runs three times (`range(3)`).
- The inner loop prints numbers from 1 to 9.
- A `print()` statement is used to create a newline after each iteration of the inner loop, ensuring the sequences are displayed on separate lines.

## Constructing a Rectangle

Next, let's create a more practical example by constructing a rectangle made of a user-defined symbol. We'll take the number of rows and columns as input from the user.

```python
# Accepting user input
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

# Nested loop to construct the rectangle
for i in range(rows):
    for j in range(columns):
        print(symbol, end=' ')
    print()  # Newline after each row
```

### Detailed Explanation

1. **User Input**:
   - `rows`: Number of rows in the rectangle.
   - `columns`: Number of columns in the rectangle.
   - `symbol`: Symbol used to draw the rectangle.

2. **Outer Loop**:
   - Iterates through each row (`range(rows)`).

3. **Inner Loop**:
   - Iterates through each column (`range(columns)`).
   - Prints the symbol without a newline (`end=' '`).

4. **Newline**:
   - The `print()` statement at the end of the outer loop iteration ensures each row is printed on a new line.

## Example Execution

### Input

- Number of rows: 4
- Number of columns: 10
- Symbol: $

### Output

```
$ $ $ $ $ $ $ $ $ $
$ $ $ $ $ $ $ $ $ $
$ $ $ $ $ $ $ $ $ $
$ $ $ $ $ $ $ $ $ $
```

### Input

- Number of rows: 3
- Number of columns: 5
- Symbol: *

### Output

```
* * * * *
* * * * *
* * * * *
```

