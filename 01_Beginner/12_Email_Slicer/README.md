# Python Email Slicer


## Program Description
The email slicer program will prompt the user to input their email address. It will then parse the email address to extract and display the username and domain name separately. This is achieved by leveraging Python's string indexing and slicing capabilities.

## Step-by-Step Implementation

### Step 1: Accept User Input
First, we need to prompt the user to enter their email address and store this input in a variable.

```python
email = input("Enter your email: ")
```

### Step 2: Find the Index of the '@' Symbol
To separate the username and domain, we need to find the position of the '@' symbol in the email address. We will use the `index` method to achieve this.

```python
at_index = email.index('@')
```

### Step 3: Extract the Username and Domain
Using the index of the '@' symbol, we can slice the email string to extract the username and domain.

```python
username = email[:at_index]
domain = email[at_index + 1:]
```

### Step 4: Print the Results
Finally, we will display the extracted username and domain using formatted strings.

```python
print(f"Your username is: {username}")
print(f"Your domain is: {domain}")
```

## Full Program Code
Here is the complete code for the email slicer program:

```python
# Python Email Slicer Program

# Step 1: Accept user input
email = input("Enter your email: ")

# Step 2: Find the index of the '@' symbol
at_index = email.index('@')

# Step 3: Extract the username and domain
username = email[:at_index]
domain = email[at_index + 1:]

# Step 4: Print the results
print(f"Your username is: {username}")
print(f"Your domain is: {domain}")
```

## Optimized Code
If you prefer a more concise version of the program, you can combine steps to reduce the number of lines. However, this may sacrifice some readability.

```python
# Concise Python Email Slicer Program

# Step 1: Accept user input and slice in one line
email = input("Enter your email: ")

# Step 2 and 3: Extract username and domain using inline slicing
print(f"Your username is: {email[:email.index('@')]}")
print(f"Your domain is: {email[email.index('@') + 1:]}")
```

