# Python Copy a File: A Comprehensive Guide

In this tutorial, we will explore how to copy files in Python using the `shutil` module. This guide will cover the fundamental functions provided by the `shutil` module to handle file copying operations. We will also include detailed code snippets to illustrate each concept.

## Introduction to `shutil`

The `shutil` module in Python provides a range of high-level operations on files and collections of files. This includes support for copying and removing files. Among the various methods available in `shutil`, we will focus on three primary functions for copying files:

1. `shutil.copyfile()`
2. `shutil.copy()`
3. `shutil.copy2()`

Each function serves a specific purpose and offers different levels of copying capabilities.

### 1. `shutil.copyfile()`

The `shutil.copyfile()` function is used to copy the contents of a source file to a destination file. It does not copy file metadata such as permissions, ownership, and timestamps. This function is best suited for simple file copying tasks where only the file content needs to be duplicated.

#### Syntax

```python
shutil.copyfile(src, dst)
```

- `src`: Path to the source file.
- `dst`: Path to the destination file.

#### Example

```python
import shutil

# Define the source and destination file paths
source_file = 'test.txt'
destination_file = 'copy.txt'

# Copy the contents of the source file to the destination file
shutil.copyfile(source_file, destination_file)

print(f"File copied from {source_file} to {destination_file}")
```

### 2. `shutil.copy()`

The `shutil.copy()` function performs the same operation as `shutil.copyfile()` but also copies the file's permission mode. The destination can be a directory or another file.

#### Syntax

```python
shutil.copy(src, dst)
```

- `src`: Path to the source file.
- `dst`: Path to the destination file or directory.

#### Example

```python
import shutil

# Define the source and destination file paths
source_file = 'test.txt'
destination_file = 'copy_with_permissions.txt'

# Copy the contents of the source file to the destination file along with permissions
shutil.copy(source_file, destination_file)

print(f"File copied from {source_file} to {destination_file} with permissions")
```

### 3. `shutil.copy2()`

The `shutil.copy2()` function extends the capabilities of `shutil.copy()` by copying the file's metadata in addition to the contents and permissions. This includes file creation and modification times.

#### Syntax

```python
shutil.copy2(src, dst)
```

- `src`: Path to the source file.
- `dst`: Path to the destination file or directory.

#### Example

```python
import shutil

# Define the source and destination file paths
source_file = 'test.txt'
destination_file = 'copy_with_metadata.txt'

# Copy the contents, permissions, and metadata of the source file to the destination file
shutil.copy2(source_file, destination_file)

print(f"File copied from {source_file} to {destination_file} with metadata")
```

## Practical Usage

To demonstrate the usage of these functions, let us assume we have a file named `test.txt` with the following content:

```
Yo, this is some text. See ya!
```

Our goal is to copy this file within the same directory and also explore copying to different locations.

### Example: Copying Within the Same Directory

```python
import shutil

source_file = 'test.txt'
destination_file = 'copy.txt'

shutil.copyfile(source_file, destination_file)

print(f"File copied from {source_file} to {destination_file}")
```

### Example: Copying to a Different Directory

```python
import shutil
import os

source_file = 'test.txt'
destination_directory = os.path.expanduser('~/Desktop')
destination_file = os.path.join(destination_directory, 'copy_on_desktop.txt')

shutil.copyfile(source_file, destination_file)

print(f"File copied from {source_file} to {destination_file}")
```

### Example: Using `shutil.copy()` and `shutil.copy2()`

```python
import shutil

source_file = 'test.txt'

# Copy using shutil.copy()
shutil.copy(source_file, 'copy_with_permissions.txt')
print("File copied with permissions")

# Copy using shutil.copy2()
shutil.copy2(source_file, 'copy_with_metadata.txt')
print("File copied with metadata")
```

