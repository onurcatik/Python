# Python File Detection 📁

## Introduction

This tutorial provides a comprehensive overview of basic file detection using Python. We will cover checking if a file or directory exists and determining the type of a given path (file or directory). The Python `os` module, which is part of the standard library, will be utilized for these operations.

## Importing the OS Module

First, ensure you import the `os` module. This module provides a way of using operating system-dependent functionality like checking file paths.

```python
import os
```

## Checking if a File Exists

To check if a file or directory exists, we use the `os.path.exists()` function. This function returns `True` if the path exists and `False` otherwise.

### Example Code

Let's create a text file named `test.txt` on the desktop and check its existence:

1. Create a variable `path` that stores the path to `test.txt`.
2. Use `os.path.exists()` to check if the file exists.
3. Print appropriate messages based on the existence check.

```python
# Define the path to the file
path = r'C:\Users\YourUsername\Desktop\test.txt'

# Check if the path exists
if os.path.exists(path):
    print("The location exists.")
else:
    print("The location doesn't exist.")
```

> **Note:** Use raw strings (`r'path'`) or double backslashes (`\\`) in the file path to avoid issues with escape sequences.

### Output

If the file exists:
```
The location exists.
```

If the file does not exist:
```
The location doesn't exist.
```

## Checking if the Path is a File

To determine if a given path is a file, use the `os.path.isfile()` function. This function returns `True` if the path is a file and `False` otherwise.

### Example Code

```python
# Check if the path is a file
if os.path.isfile(path):
    print("That is a file.")
else:
    print("That is not a file.")
```

### Output

If the path is a file:
```
That is a file.
```

If the path is not a file:
```
That is not a file.
```

## Checking if the Path is a Directory

To determine if a given path is a directory, use the `os.path.isdir()` function. This function returns `True` if the path is a directory and `False` otherwise.

### Example Code

```python
# Check if the path is a directory
if os.path.isdir(path):
    print("That is a directory.")
else:
    print("That is not a directory.")
```

### Output

If the path is a directory:
```
That is a directory.
```

If the path is not a directory:
```
That is not a directory.
```

## Combining the Checks

You can combine these checks to determine whether the path is a file, a directory, or does not exist. Here's an example that integrates all the checks:

### Example Code

```python
# Define the path to the file or directory
path = r'C:\Users\YourUsername\Desktop\test.txt'

# Check if the path exists
if os.path.exists(path):
    if os.path.isfile(path):
        print("That is a file.")
    elif os.path.isdir(path):
        print("That is a directory.")
else:
    print("The location doesn't exist.")
```

### Output

If the path is a file:
```
That is a file.
```

If the path is a directory:
```
That is a directory.
```

If the path does not exist:
```
The location doesn't exist.
```
