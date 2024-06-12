# String Methods 

## Table of Contents
- [String Methods](#string-methods)
  - [Table of Contents](#table-of-contents)
  - [Getting User Input](#getting-user-input)
  - [Calculating the Length of a String](#calculating-the-length-of-a-string)
  - [Finding Substrings](#finding-substrings)
  - [Capitalizing Strings](#capitalizing-strings)
  - [Changing Case](#changing-case)
  - [Checking if a String is Numeric](#checking-if-a-string-is-numeric)
  - [Checking if a String is Alphabetic](#checking-if-a-string-is-alphabetic)
  - [Counting Substrings](#counting-substrings)
  - [Replacing Substrings](#replacing-substrings)
  - [Practical Exercise: Validating User Input](#practical-exercise-validating-user-input)

## Getting User Input

We start by asking the user for their full name.

```python
name = input("Enter your full name: ")
```

## Calculating the Length of a String

The `len` function returns the number of characters in a string, including spaces.

```python
result = len(name)
print(f"The length of your name is: {result}")
```

## Finding Substrings

The `find` method returns the index of the first occurrence of a specified substring. If the substring is not found, it returns `-1`.

```python
# Finding the first occurrence of a space
result = name.find(" ")
print(f"The first occurrence of a space is at index: {result}")

# Finding the first occurrence of 'B'
result = name.find("B")
print(f"The first occurrence of 'B' is at index: {result}")

# Finding the last occurrence of 'o' using rfind
result = name.rfind("o")
print(f"The last occurrence of 'o' is at index: {result}")
```

## Capitalizing Strings

The `capitalize` method returns a string with the first character capitalized and the rest lowercased.

```python
name = name.capitalize()
print(f"Capitalized name: {name}")
```

## Changing Case

The `upper` and `lower` methods convert all characters in a string to uppercase or lowercase, respectively.

```python
# Converting to uppercase
name_upper = name.upper()
print(f"Uppercase name: {name_upper}")

# Converting to lowercase
name_lower = name.lower()
print(f"Lowercase name: {name_lower}")
```

## Checking if a String is Numeric

The `isdigit` method returns `True` if all characters in the string are digits, otherwise it returns `False`.

```python
result = name.isdigit()
print(f"Is the name all digits? {result}")

# Testing with a numeric string
numeric_string = "12345"
result = numeric_string.isdigit()
print(f"Is the string '12345' all digits? {result}")
```

## Checking if a String is Alphabetic

The `isalpha` method returns `True` if all characters in the string are alphabetic and there is at least one character, otherwise it returns `False`.

```python
result = name.isalpha()
print(f"Is the name all alphabetic? {result}")

# Testing with a string containing spaces and digits
test_string = "JohnDoe123"
result = test_string.isalpha()
print(f"Is the string 'JohnDoe123' all alphabetic? {result}")
```

## Counting Substrings

The `count` method returns the number of non-overlapping occurrences of a substring in the string.

```python
phone_number = input("Enter your phone number: ")
dash_count = phone_number.count("-")
print(f"The number of dashes in the phone number is: {dash_count}")
```

## Replacing Substrings

The `replace` method returns a copy of the string where all occurrences of a substring are replaced with another substring.

```python
# Replacing dashes with spaces
phone_number = phone_number.replace("-", " ")
print(f"Phone number with spaces: {phone_number}")

# Removing dashes completely
phone_number = phone_number.replace("-", "")
print(f"Phone number without dashes: {phone_number}")
```

## Practical Exercise: Validating User Input

In this exercise, we will validate a username based on the following rules:
1. The username can be no more than 12 characters long.
2. The username must not contain any spaces.
3. The username must not contain any digits.

```python
username = input("Enter a username: ")

# Rule 1: Username must be no more than 12 characters long
if len(username) > 12:
    print("Your username can't be more than 12 characters.")
else:
    # Rule 2: Username must not contain spaces
    if username.find(" ") != -1:
        print("Your username can't contain spaces.")
    else:
        # Rule 3: Username must not contain digits
        if not username.isalpha():
            print("Your username can't contain numbers.")
        else:
            print(f"Welcome, {username}!")
```

