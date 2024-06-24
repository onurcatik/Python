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

print("Menu")
print("*" * 20)
for item , price in menu.items():
    print(f"{item:12}: ${price:.2f}")
print("-" * 20)

cart = []
total = 0.0

while True:
    food = input("Select item (q to quit):".lower())
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item not on the menu")


for food in cart:
    total += menu[food]


print("\nYour Cart:")
print("-" * 20)
for food in cart:
    print(food)
print("-" * 20)
print(f"Total: ${total:.2f}")
