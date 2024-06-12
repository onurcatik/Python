# String Indexing 


## Basics of String Indexing

In Python, strings are sequences of characters. Each character in a string has a position or index, starting from zero for the first character and increasing by one for each subsequent character. 

### Accessing Individual Characters

To access an individual character in a string, you use the indexing operator with the position of the character you want to access.

```python
credit_number = "1234-5678-9012-3456"
print(credit_number[0])  # Output: 1
print(credit_number[1])  # Output: 2
print(credit_number[2])  # Output: 3
print(credit_number[3])  # Output: 4
print(credit_number[4])  # Output: -
```

### Slicing Strings

You can also access a range of characters using slicing. Slicing is done by specifying a starting index, an ending index, and an optional step.

```python
# Getting the first four characters
print(credit_number[0:4])  # Output: 1234

# Omitting the starting index (defaults to 0)
print(credit_number[:4])  # Output: 1234

# Getting the next set of four characters
print(credit_number[5:9])  # Output: 5678

# Omitting the ending index (goes up to the end of the string)
print(credit_number[5:])  # Output: 5678-9012-3456
```

### Negative Indexing

Python allows negative indexing, where `-1` refers to the last character, `-2` to the second last, and so on.

```python
# Accessing the last character
print(credit_number[-1])  # Output: 6

# Accessing the second last character
print(credit_number[-2])  # Output: 5
```

### Slicing with Steps

The step parameter allows you to skip characters in the string.

```python
# Every second character
print(credit_number[::2])  # Output: 13-58923-46

# Every third character
print(credit_number[::3])  # Output: 14-83-5

# Reversing the string
print(credit_number[::-1])  # Output: 6543-2109-8765-4321
```

### Practical Examples

#### Extracting the Last Four Digits of a Credit Card Number

Suppose you want to extract the last four digits of a credit card number for display purposes.

```python
credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
print(f"****-****-****-{last_digits}")  # Output: ****-****-****-3456
```

#### Reversing a String

To reverse a string, you can use a negative step.

```python
credit_number = "1234-5678-9012-3456"
reversed_credit_number = credit_number[::-1]
print(reversed_credit_number)  # Output: 6543-2109-8765-4321
```

