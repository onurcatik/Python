# Python: Deleting Files and Directories 🗑️

In this tutorial, we will explore the methods available in Python for deleting files and directories. We will focus on using the `os` and `shutil` modules, both of which are part of Python's standard library. This guide will provide comprehensive code snippets and detailed explanations, ensuring you understand each step thoroughly.

## Introduction

Python provides a straightforward approach to file and directory manipulation through its standard library. Deleting files and directories is a common operation that can be efficiently handled using the `os` and `shutil` modules. This tutorial will cover three primary functions:
- `os.remove()`: Deletes a file.
- `os.rmdir()`: Deletes an empty directory.
- `shutil.rmtree()`: Deletes a directory and all its contents.

## Deleting a File

To delete a file, we use the `os.remove()` function. Let's start by creating a file named `test.txt` and then delete it using Python.

### Step 1: Create a File

First, create a file named `test.txt` in your project directory.

### Step 2: Delete the File

Here is the code to delete `test.txt`:

```python
import os

# Define the path to the file
path = "test.txt"

# Delete the file
os.remove(path)
print(f"{path} was deleted")
```

### Handling Exceptions

It is important to handle exceptions that may occur when attempting to delete a file that does not exist. This can be done using a try-except block:

```python
import os

path = "test.txt"

try:
    os.remove(path)
    print(f"{path} was deleted")
except FileNotFoundError:
    print("File not found")
```

## Deleting an Empty Directory

To delete an empty directory, we use the `os.rmdir()` function. Let's create an empty directory named `empty_folder` and then delete it.

### Step 1: Create an Empty Directory

First, create an empty directory named `empty_folder` in your project directory.

### Step 2: Delete the Empty Directory

Here is the code to delete `empty_folder`:

```python
import os

# Define the path to the empty directory
path = "empty_folder"

# Delete the empty directory
os.rmdir(path)
print(f"{path} was deleted")
```

### Handling Exceptions

Handle exceptions that may occur, such as attempting to delete a non-empty directory or not having the required permissions:

```python
import os

path = "empty_folder"

try:
    os.rmdir(path)
    print(f"{path} was deleted")
except FileNotFoundError:
    print("Directory not found")
except PermissionError:
    print("You do not have permission to delete this directory")
except OSError as e:
    print(f"Error: {e}")
```

## Deleting a Directory with Contents

To delete a directory along with all its contents, we use the `shutil.rmtree()` function. This function should be used with caution as it will remove everything in the specified directory.

### Step 1: Create a Directory with Contents

Create a directory named `folder` and add a file named `test.txt` inside it.

### Step 2: Delete the Directory and Its Contents

Here is the code to delete `folder` and all its contents:

```python
import shutil

# Define the path to the directory
path = "folder"

# Delete the directory and its contents
shutil.rmtree(path)
print(f"{path} was deleted")
```

### Handling Exceptions

Handle exceptions that may occur when deleting directories and their contents:

```python
import shutil

path = "folder"

try:
    shutil.rmtree(path)
    print(f"{path} was deleted")
except FileNotFoundError:
    print("Directory not found")
except PermissionError:
    print("You do not have permission to delete this directory")
except OSError as e:
    print(f"Error: {e}")
```

## Conclusion

In summary, we have discussed three essential functions for deleting files and directories in Python:
- `os.remove()`: Deletes a file.
- `os.rmdir()`: Deletes an empty directory.
- `shutil.rmtree()`: Deletes a directory and all its contents.

Each function has its specific use case and requires appropriate exception handling to ensure robust code. Below is a complete example that includes all the discussed methods and exception handling:

```python
import os
import shutil

def delete_file(path):
    try:
        os.remove(path)
        print(f"{path} was deleted")
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("You do not have permission to delete this file")

def delete_empty_directory(path):
    try:
        os.rmdir(path)
        print(f"{path} was deleted")
    except FileNotFoundError:
        print("Directory not found")
    except PermissionError:
        print("You do not have permission to delete this directory")
    except OSError as e:
        print(f"Error: {e}")

def delete_directory_with_contents(path):
    try:
        shutil.rmtree(path)
        print(f"{path} was deleted")
    except FileNotFoundError:
        print("Directory not found")
    except PermissionError:
        print("You do not have permission to delete this directory")
    except OSError as e:
        print(f"Error: {e}")

# Example usage
delete_file("test.txt")
delete_empty_directory("empty_folder")
delete_directory_with_contents("folder")
```

By understanding and applying these functions, you can efficiently manage file and directory deletions in your Python projects.