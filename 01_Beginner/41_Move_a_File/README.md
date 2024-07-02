# Python Move a File 🗃️

## Introduction

This tutorial will guide you through moving files and directories using Python. We will use the `os` module, which is part of the standard Python library. This tutorial aims to be comprehensive and precise, reflecting the rigor and standards of the field. 

## Importing the Required Module

First, we need to import the `os` module. The `os` module provides a way of using operating system-dependent functionality like reading or writing to the file system.

```python
import os
```

## Defining Source and Destination

We need to define the source and destination paths. The source path is the current location of the file, and the destination path is where we want to move the file.

```python
source = 'path/to/your/source/file.txt'  # Replace with your source file path
destination = 'path/to/your/destination/file.txt'  # Replace with your destination file path
```

Ensure the paths are correctly specified. If your paths include backslashes (as in Windows paths), use double backslashes or raw string literals to avoid escape sequences.

```python
source = r'C:\path\to\your\source\file.txt'
destination = r'C:\path\to\your\destination\file.txt'
```

## Handling Exceptions

It's good practice to handle potential errors that might occur during file operations. We will use a try-except block to handle these exceptions.

```python
try:
    # Check if the source file exists
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source file '{source}' was not found.")

    # Check if the destination file already exists
    if os.path.exists(destination):
        print(f"There is already a file at '{destination}'.")
    else:
        # Move the file
        os.replace(source, destination)
        print(f"'{source}' was moved to '{destination}'.")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(f"An error occurred: {e}")
```

## Moving a Directory

The process of moving a directory is similar to moving a file. You only need to specify the directory paths.

```python
source_dir = r'C:\path\to\your\source\folder'
destination_dir = r'C:\path\to\your\destination\folder'

try:
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory '{source_dir}' was not found.")

    # Check if the destination directory already exists
    if os.path.exists(destination_dir):
        print(f"There is already a directory at '{destination_dir}'.")
    else:
        # Move the directory
        os.replace(source_dir, destination_dir)
        print(f"'{source_dir}' was moved to '{destination_dir}'.")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(f"An error occurred: {e}")
```

## Complete Code Example

Here is the complete code combining file and directory movement with exception handling:

```python
import os

def move_file_or_directory(source, destination):
    try:
        # Check if the source exists
        if not os.path.exists(source):
            raise FileNotFoundError(f"Source '{source}' was not found.")

        # Check if the destination already exists
        if os.path.exists(destination):
            print(f"There is already a file or directory at '{destination}'.")
        else:
            # Move the file or directory
            os.replace(source, destination)
            print(f"'{source}' was moved to '{destination}'.")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source_file = r'C:\path\to\your\source\file.txt'
destination_file = r'C:\path\to\your\destination\file.txt'
move_file_or_directory(source_file, destination_file)

source_dir = r'C:\path\to\your\source\folder'
destination_dir = r'C:\path\to\your\destination\folder'
move_file_or_directory(source_dir, destination_dir)
```

