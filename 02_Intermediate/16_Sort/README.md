## Python Sorting: A Comprehensive Guide

In Python, sorting is a fundamental operation often required in various programming tasks. Python provides two primary methods for sorting data: the `sort()` method and the `sorted()` function. The method you choose depends on the type of data structure you're working with. In this tutorial, we will cover sorting techniques for lists, tuples, dictionaries, and custom objects, ensuring a rigorous understanding of the underlying concepts.

### 1. Sorting Lists

A list is one of the most commonly used data structures in Python. Sorting a list can be achieved effortlessly using the `sort()` method or the `sorted()` function.

#### Example: Sorting a List of Strings

Let's create a list of fruits:

```python
fruits = ["banana", "orange", "apple", "coconut"]
print(fruits)
```

Output:

```python
['banana', 'orange', 'apple', 'coconut']
```

To sort the list in alphabetical order, we can use the `sort()` method, which modifies the list in place:

```python
fruits.sort()
print(fruits)
```

Output:

```python
['apple', 'banana', 'coconut', 'orange']
```

Alternatively, you can use the `sorted()` function, which returns a new sorted list without modifying the original list:

```python
sorted_fruits = sorted(fruits)
print(sorted_fruits)
```

Output:

```python
['apple', 'banana', 'coconut', 'orange']
```

#### Sorting in Reverse Order

To sort the list in reverse alphabetical order, use the `reverse=True` keyword argument:

```python
fruits.sort(reverse=True)
print(fruits)
```

Output:

```python
['orange', 'coconut', 'banana', 'apple']
```

### 2. Sorting Tuples

Tuples in Python are immutable, meaning they cannot be modified after creation. Therefore, the `sort()` method is not available for tuples. Instead, we use the `sorted()` function, which returns a sorted list.

#### Example: Sorting a Tuple

First, let's convert our list of fruits into a tuple:

```python
fruits_tuple = ("banana", "orange", "apple", "coconut")
print(fruits_tuple)
```

Output:

```python
('banana', 'orange', 'apple', 'coconut')
```

To sort the tuple, we apply the `sorted()` function:

```python
sorted_tuple = sorted(fruits_tuple)
print(sorted_tuple)
```

Output:

```python
['apple', 'banana', 'coconut', 'orange']
```

Notice that the result is a list. If we want to keep the result as a tuple, we can convert it back:

```python
sorted_fruits_tuple = tuple(sorted(fruits_tuple))
print(sorted_fruits_tuple)
```

Output:

```python
('apple', 'banana', 'coconut', 'orange')
```

#### Sorting in Reverse Order

To sort the tuple in reverse alphabetical order, use the `reverse=True` argument:

```python
reversed_fruits_tuple = tuple(sorted(fruits_tuple, reverse=True))
print(reversed_fruits_tuple)
```

Output:

```python
('orange', 'coconut', 'banana', 'apple')
```

### 3. Sorting Dictionaries

Sorting dictionaries can be more complex due to their key-value pair structure. By default, dictionaries are unordered collections in Python (before Python 3.7). We typically sort dictionaries by keys or by values.

#### Example: Sorting a Dictionary by Keys

Let's create a dictionary where the fruit names are keys, and their corresponding calorie values are the values:

```python
fruits_dict = {
    "banana": 105,
    "orange": 73,
    "apple": 72,
    "coconut": 354
}
print(fruits_dict)
```

Output:

```python
{'banana': 105, 'orange': 73, 'apple': 72, 'coconut': 354}
```

To sort the dictionary by its keys in alphabetical order:

```python
sorted_fruits_dict = dict(sorted(fruits_dict.items()))
print(sorted_fruits_dict)
```

Output:

```python
{'apple': 72, 'banana': 105, 'coconut': 354, 'orange': 73}
```

#### Sorting by Values

Sorting a dictionary by its values requires using the `key` argument with a lambda function:

```python
sorted_by_values = dict(sorted(fruits_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)
```

Output:

```python
{'apple': 72, 'orange': 73, 'banana': 105, 'coconut': 354}
```

#### Sorting in Reverse Order

To sort by values in descending order:

```python
sorted_by_values_desc = dict(sorted(fruits_dict.items(), key=lambda item: item[1], reverse=True))
print(sorted_by_values_desc)
```

Output:

```python
{'coconut': 354, 'banana': 105, 'orange': 73, 'apple': 72}
```

### 4. Sorting Custom Objects

When dealing with custom objects, sorting can be done based on specific attributes of the object using the `key` argument with a lambda function.

#### Example: Sorting a List of Objects

Let's define a `Fruit` class:

```python
class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name}: {self.calories} calories"
```

Next, create a list of `Fruit` objects:

```python
fruits = [
    Fruit("banana", 105),
    Fruit("apple", 72),
    Fruit("orange", 73),
    Fruit("coconut", 354)
]
print(fruits)
```

Output:

```python
[banana: 105 calories, apple: 72 calories, orange: 73 calories, coconut: 354 calories]
```

#### Sorting by Name

To sort the list of `Fruit` objects by their `name` attribute:

```python
sorted_fruits = sorted(fruits, key=lambda fruit: fruit.name)
print(sorted_fruits)
```

Output:

```python
[apple: 72 calories, banana: 105 calories, coconut: 354 calories, orange: 73 calories]
```

#### Sorting by Calories

To sort by the `calories` attribute:

```python
sorted_by_calories = sorted(fruits, key=lambda fruit: fruit.calories)
print(sorted_by_calories)
```

Output:

```python
[apple: 72 calories, orange: 73 calories, banana: 105 calories, coconut: 354 calories]
```

#### Sorting in Reverse Order

To sort by calories in descending order:

```python
sorted_by_calories_desc = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True)
print(sorted_by_calories_desc)
```

Output:

```python
[coconut: 354 calories, banana: 105 calories, orange: 73 calories, apple: 72 calories]
```

### Conclusion

Sorting in Python is a versatile and powerful tool that can be applied to various data structures, including lists, tuples, dictionaries, and custom objects. By understanding and utilizing the `sort()` method and the `sorted()` function, along with key arguments and lambda functions, you can efficiently sort data in your Python programs. This tutorial has provided a comprehensive guide to sorting, ensuring precision and adherence to professional standards in Python programming.