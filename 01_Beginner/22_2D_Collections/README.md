# Python 2D Collections

## Introduction to 2D Lists

A two-dimensional list is a list that contains other lists as its elements. Each inner list represents a row in the 2D structure, while the elements within each inner list represent the columns.

#### Creating 2D Lists

Let's begin by creating three separate lists: one for fruits, one for vegetables, and one for meats.

```python
# Define one-dimensional lists
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

# Combine these lists into a two-dimensional list
groceries = [fruits, vegetables, meats]

# Print the 2D list
print(groceries)
```

Output:
```
[['apple', 'orange', 'banana', 'coconut'], ['celery', 'carrots', 'potatoes'], ['chicken', 'fish', 'turkey']]
```

#### Accessing Elements in 2D Lists

To access an element in a 2D list, you need two indices: the first for the row and the second for the column.

```python
# Access the first element in the fruits list
print(groceries[0][0])  # Output: apple

# Access the second element in the vegetables list
print(groceries[1][1])  # Output: carrots

# Access the third element in the meats list
print(groceries[2][2])  # Output: turkey
```

#### Iterating Over 2D Lists

You can use nested loops to iterate over each element in a 2D list.

```python
# Iterate over the rows
for row in groceries:
    # Iterate over the elements in each row
    for item in row:
        print(item, end=' ')
    print()  # New line after each row
```

Output:
```
apple orange banana coconut 
celery carrots potatoes 
chicken fish turkey 
```

### Creating 2D Tuples

A two-dimensional tuple is similar to a 2D list but immutable. It is created using nested tuples.

#### Example of a 2D Tuple

Let's create a 2D tuple representing a keypad.

```python
# Define a 2D tuple
numpad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ('*', 0, '#')
)

# Print the 2D tuple
print(numpad)
```

Output:
```
((1, 2, 3), (4, 5, 6), (7, 8, 9), ('*', 0, '#'))
```

#### Accessing Elements in 2D Tuples

Just like with 2D lists, you access elements in 2D tuples using two indices.

```python
# Access the first element in the first row
print(numpad[0][0])  # Output: 1

# Access the second element in the second row
print(numpad[1][1])  # Output: 5

# Access the third element in the third row
print(numpad[2][2])  # Output: 9
```

#### Iterating Over 2D Tuples

You can also use nested loops to iterate over the elements of a 2D tuple.

```python
# Iterate over the rows
for row in numpad:
    # Iterate over the elements in each row
    for num in row:
        print(num, end=' ')
    print()  # New line after each row
```

Output:
```
1 2 3 
4 5 6 
7 8 9 
* 0 # 
```

