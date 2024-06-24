# Python Concession Stand Program 🍿

## Creating the Menu

We begin by creating a dictionary named `menu`, which will contain the items available at the concession stand and their prices.

```python
menu = {
    "pizza": 5.50,
    "nachos": 3.25,
    "popcorn": 4.00,
    "fries": 2.50,
    "chips": 1.75,
    "soft pretzel": 2.00,
    "soda": 1.50,
    "lemonade": 2.00
}
```

## Displaying the Menu

To display the menu to the user, we will use the `items()` method of the dictionary to iterate through the key-value pairs and format them for readability.

```python
print("Menu")
print("-" * 20)
for item, price in menu.items():
    print(f"{item:12}: ${price:.2f}")
print("-" * 20)
```

## User Selection

We will prompt the user to select items from the menu. The user can continue selecting items until they decide to quit by entering 'q'.

```python
cart = []
total = 0.0

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item not on the menu. Please select a valid item.")
```

## Calculating the Total

After the user has finished selecting items, we will calculate the total cost of the items in their cart.

```python
for food in cart:
    total += menu[food]
```

## Displaying the Cart and Total

Finally, we will display the items in the user's cart and the total cost.

```python
print("\nYour Cart:")
print("-" * 20)
for food in cart:
    print(food)
print("-" * 20)
print(f"Total: ${total:.2f}")
```

## Complete Program

Here is the complete program:

```python
# Concession Stand Program

# Create the menu dictionary
menu = {
    "pizza": 5.50,
    "nachos": 3.25,
    "popcorn": 4.00,
    "fries": 2.50,
    "chips": 1.75,
    "soft pretzel": 2.00,
    "soda": 1.50,
    "lemonade": 2.00
}

# Display the menu
print("Menu")
print("-" * 20)
for item, price in menu.items():
    print(f"{item:12}: ${price:.2f}")
print("-" * 20)

# Initialize the cart and total
cart = []
total = 0.0

# User selection loop
while True:
    food = input("Select an item (q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item not on the menu. Please select a valid item.")

# Calculate the total
for food in cart:
    total += menu[food]

# Display the cart and total
print("\nYour Cart:")
print("-" * 20)
for food in cart:
    print(food)
print("-" * 20)
print(f"Total: ${total:.2f}")
```

