# Python Lists, Sets, and Tuples 

## 1. Lists

### Characteristics
- **Ordered**: Elements in a list have a defined order.
- **Changeable**: You can modify the elements after the list has been created.
- **Allow Duplicates**: Lists can contain duplicate elements.

### Creating a List
To create a list, enclose the values in square brackets `[]`.

```python
fruits = ["apple", "orange", "banana", "coconut"]
print(fruits)
```

### Accessing Elements
You can access elements using their index. The first element has an index of 0.

```python
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: orange
```

### Modifying Elements
Lists are changeable, meaning you can modify elements.

```python
fruits[0] = "pineapple"
print(fruits)  # Output: ["pineapple", "orange", "banana", "coconut"]
```

### List Methods
Lists come with several built-in methods for manipulating elements.

- **append()**: Adds an element to the end of the list.
  
  ```python
  fruits.append("pineapple")
  print(fruits)  # Output: ["pineapple", "orange", "banana", "coconut", "pineapple"]
  ```

- **remove()**: Removes the first occurrence of the specified element.
  
  ```python
  fruits.remove("pineapple")
  print(fruits)  # Output: ["orange", "banana", "coconut", "pineapple"]
  ```

- **insert()**: Inserts an element at the specified position.
  
  ```python
  fruits.insert(0, "apple")
  print(fruits)  # Output: ["apple", "orange", "banana", "coconut", "pineapple"]
  ```

- **sort()**: Sorts the list.
  
  ```python
  fruits.sort()
  print(fruits)  # Output: ["apple", "banana", "coconut", "orange", "pineapple"]
  ```

- **reverse()**: Reverses the order of the list.
  
  ```python
  fruits.reverse()
  print(fruits)  # Output: ["pineapple", "orange", "coconut", "banana", "apple"]
  ```

### Iterating Over a List
You can iterate over the elements of a list using a `for` loop.

```python
for fruit in fruits:
    print(fruit)
```

### Finding Length
Use the `len()` function to find the number of elements in the list.

```python
print(len(fruits))  # Output: 5
```

### Checking Membership
Use the `in` operator to check if an element is in the list.

```python
print("apple" in fruits)  # Output: True
print("pineapple" in fruits)  # Output: False
```

## 2. Sets

### Characteristics
- **Unordered**: Elements do not have a defined order.
- **Immutable**: You cannot change the elements after the set has been created, but you can add or remove elements.
- **No Duplicates**: Sets do not allow duplicate elements.

### Creating a Set
To create a set, enclose the values in curly braces `{}`.

```python
fruits = {"apple", "orange", "banana", "coconut"}
print(fruits)
```

### Adding and Removing Elements
Use the `add()` method to add an element and `remove()` to remove an element.

```python
fruits.add("pineapple")
print(fruits)  # Output: {"apple", "orange", "banana", "coconut", "pineapple"}

fruits.remove("apple")
print(fruits)  # Output: {"orange", "banana", "coconut", "pineapple"}
```

### Set Methods
Sets come with several built-in methods for manipulating elements.

- **add()**: Adds an element to the set.
  
  ```python
  fruits.add("apple")
  ```

- **remove()**: Removes the specified element.
  
  ```python
  fruits.remove("banana")
  ```

- **clear()**: Removes all elements from the set.
  
  ```python
  fruits.clear()
  print(fruits)  # Output: set()
  ```

### Iterating Over a Set
You can iterate over the elements of a set using a `for` loop.

```python
for fruit in fruits:
    print(fruit)
```

### Finding Length
Use the `len()` function to find the number of elements in the set.

```python
print(len(fruits))  # Output: 4
```

### Checking Membership
Use the `in` operator to check if an element is in the set.

```python
print("apple" in fruits)  # Output: True
print("pineapple" in fruits)  # Output: False
```

## 3. Tuples

### Characteristics
- **Ordered**: Elements in a tuple have a defined order.
- **Immutable**: You cannot change the elements after the tuple has been created.
- **Allow Duplicates**: Tuples can contain duplicate elements.

### Creating a Tuple
To create a tuple, enclose the values in parentheses `()`.

```python
fruits = ("apple", "orange", "banana", "coconut")
print(fruits)
```

### Accessing Elements
You can access elements using their index. The first element has an index of 0.

```python
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: orange
```

### Tuple Methods
Tuples come with two built-in methods for manipulating elements.

- **count()**: Returns the number of times a specified value occurs in a tuple.
  
  ```python
  print(fruits.count("banana"))  # Output: 1
  ```

- **index()**: Searches the tuple for a specified value and returns the position of where it was found.
  
  ```python
  print(fruits.index("orange"))  # Output: 1
  ```

### Iterating Over a Tuple
You can iterate over the elements of a tuple using a `for` loop.

```python
for fruit in fruits:
    print(fruit)
```

### Finding Length
Use the `len()` function to find the number of elements in the tuple.

```python
print(len(fruits))  # Output: 4
```

### Checking Membership
Use the `in` operator to check if an element is in the tuple.

```python
print("apple" in fruits)  # Output: True
print("pineapple" in fruits)  # Output: False
```

## Summary
- **Lists**: Ordered and changeable collections that allow duplicate elements. Created using square brackets `[]`.
- **Sets**: Unordered and immutable collections that do not allow duplicate elements. Created using curly braces `{}`.
- **Tuples**: Ordered and immutable collections that allow duplicate elements. Created using parentheses `()`.

