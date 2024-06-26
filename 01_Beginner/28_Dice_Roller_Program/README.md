# DICE ROLLER Program 

## Introduction

In this tutorial, we will create a dice roller program in Python. The program will use ASCII art to represent the faces of the dice. We will make use of Unicode characters for the dice faces and utilize the `random` module to simulate rolling the dice.

## Importing the Required Module

We begin by importing the `random` module, which will help us generate random numbers between 1 and 6.

```python
import random
```

## Unicode Characters for Dice Faces

To create the ASCII art for the dice faces, we will use Unicode characters. Here are the Unicode codes for the characters we need:

- ⚀: \u2680
- ⚁: \u2681
- ⚂: \u2682
- ⚃: \u2683
- ⚄: \u2684
- ⚅: \u2685

We can test these characters by printing them:

```python
print("\u2680 \u2681 \u2682 \u2683 \u2684 \u2685")
```

## Creating the ASCII Art for Dice Faces

We will create a dictionary to store the ASCII art for each dice face. Each face will be represented as a tuple of strings.

```python
dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    )
}
```

## Generating Random Dice Rolls

We will create a function to roll a specified number of dice and return the results as a list.

```python
def roll_dice(number_of_dice):
    dice = []
    total = 0
    for _ in range(number_of_dice):
        roll = random.randint(1, 6)
        dice.append(roll)
        total += roll
    return dice, total
```

## Displaying the Dice Faces

We will create a function to display the dice faces in a horizontal line.

```python
def display_dice(dice):
    for line in range(5):
        for die in dice:
            print(dice_art[die][line], end=" ")
        print()

# Example Usage
number_of_dice = int(input("How many dice would you like to roll? "))
dice, total = roll_dice(number_of_dice)
display_dice(dice)
print(f"Total: {total}")
```

## Full Program

Here is the complete program combining all the parts discussed above:

```python
import random

dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    )
}

def roll_dice(number_of_dice):
    dice = []
    total = 0
    for _ in range(number_of_dice):
        roll = random.randint(1, 6)
        dice.append(roll)
        total += roll
    return dice, total

def display_dice(dice):
    for line in range(5):
        for die in dice:
            print(dice_art[die][line], end=" ")
        print()

if __name__ == "__main__":
    number_of_dice = int(input("How many dice would you like to roll? "))
    dice, total = roll_dice(number_of_dice)
    display_dice(dice)
    print(f"Total: {total}")
```
