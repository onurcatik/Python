# Python Shopping Cart Program

In this tutorial, we will develop a shopping cart program in Python. This exercise will reinforce the concepts of lists, sets, and tuples, with a particular focus on lists due to their mutability and ordered nature. Our program will allow users to add food items and their prices to a shopping cart, display the cart, and calculate the total cost. 

## Program Overview

1. Initialize empty lists for foods and prices.
2. Use a `while` loop to continuously ask the user for food items and prices.
3. Break out of the loop when the user decides to quit.
4. Display the contents of the shopping cart.
5. Calculate and display the total cost of the items in the cart.

## Step-by-Step Implementation

### Step 1: Initialize Lists and Total

We start by initializing two empty lists, one for storing food items and another for storing their respective prices. We also initialize a variable `total` to keep track of the total cost.

```python
foods = []
prices = []
total = 0.0
```

### Step 2: Main Loop for User Input

We use a `while` loop to repeatedly prompt the user to enter food items and their prices. The loop will continue until the user decides to quit by entering 'q' or 'Q'.

```python
while True:
    food = input("Enter a food to buy (press 'q' to quit): ").lower()
    if food == 'q':
        break
    price = float(input(f"Enter the price of {food} in dollars: "))
    foods.append(food)
    prices.append(price)
```

### Step 3: Display Shopping Cart

After the user quits the input loop, we display the contents of the shopping cart. We use a simple `for` loop to iterate over the `foods` list and print each item.

```python
print("\n----- Your Cart -----")
for food in foods:
    print(food, end=' ')
print()
```

### Step 4: Calculate Total Cost

We then calculate the total cost by summing up the values in the `prices` list.

```python
for price in prices:
    total += price
print(f"Your total is: ${total:.2f}")
```

### Full Program

Below is the complete implementation of the shopping cart program:

```python
# Initialize lists and total
foods = []
prices = []
total = 0.0

# Main loop for user input
while True:
    food = input("Enter a food to buy (press 'q' to quit): ").lower()
    if food == 'q':
        break
    price = float(input(f"Enter the price of {food} in dollars: "))
    foods.append(food)
    prices.append(price)

# Display shopping cart
print("\n----- Your Cart -----")
for food in foods:
    print(food, end=' ')
print()

# Calculate total cost
for price in prices:
    total += price
print(f"Your total is: ${total:.2f}")
```

### Additional Considerations

1. **Data Validation:** In a more robust application, you would include error handling to ensure valid inputs (e.g., checking if the entered price is a valid number).
2. **Refactoring:** The program can be refactored into functions to improve readability and maintainability.
3. **Advanced Features:** Additional features could include removing items, updating quantities, and more.

By following this structured approach, we ensure our program is not only functional but also easy to understand and maintain. This exercise solidifies the understanding of lists and their applications in real-world scenarios.