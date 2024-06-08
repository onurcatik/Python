# User input


## Accepting User Input

In Python, the `input()` function is used to accept user input from the console. This function pauses the program's execution and waits for the user to type something and press Enter. The input received is always of the string data type, regardless of what the user enters.

### Example 1: Simple User Input

```python
# Accepting user input
name = input("Enter your name: ")

# Using the input
print(f"Hello, {name}!")
```

In this example, the program prompts the user to enter their name and then prints a greeting message.

## Handling Different Data Types

Since the `input()` function always returns a string, typecasting is necessary when dealing with numerical inputs. Depending on the context, you might need to convert the input to an integer (`int`) or a floating-point number (`float`).

### Example 2: Typecasting User Input

```python
# Accepting and typecasting user input
age = int(input("Enter your age: "))

# Using the input in arithmetic operations
print(f"You are {age} years old.")
print(f"Next year, you will be {age + 1} years old.")
```

In this example, the user’s age is typecasted to an integer to perform arithmetic operations.

## Exercise 1: Mad Libs Game

Mad Libs is a fun game where the user provides different parts of speech (nouns, verbs, adjectives) to fill in the blanks in a story.

```python
# Mad Libs Game
adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter another adjective: ")
verb = input("Enter a verb ending in -ing: ")
adjective3 = input("Enter one more adjective: ")

# Constructing the story
story = f"Today I went to a {adjective1} zoo. In an exhibit, I saw a {noun}. The {noun} was {adjective2} and {verb}. I was {adjective3}."

# Displaying the story
print(story)
```

## Exercise 2: Calculating Area and Volume

This exercise involves calculating the area of a rectangle and the volume of a rectangular prism.

```python
# Calculating the area of a rectangle
length = float(input("Enter the length of the rectangle (in cm): "))
width = float(input("Enter the width of the rectangle (in cm): "))

area = length * width

print(f"The area of the rectangle is {area} cm².")

# Calculating the volume of a rectangular prism
height = float(input("Enter the height of the rectangle (in cm): "))
volume = length * width * height

print(f"The volume of the rectangular prism is {volume} cm³.")
```

## Exercise 3: Shopping Cart Program

In this exercise, we will create a simple shopping cart program that calculates the total cost based on user input.

```python
# Shopping Cart Program
item = input("What item would you like to buy? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many would you like to buy? "))

total = round(price * quantity, 2)

print(f"You have bought {quantity} {item}(s). Your total is ${total}.")
```

