foods = []
prices = []
total = 0.0

while True:
    food = input("Enter the food item (or 'done' to finish): ")
    if food.lower() == "done":
        break
    price = float(input(f"Enter the price of {food} in dollars: "))
    foods.append(food)
    prices.append(price)

print("\n----- Your Cart -----")

for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]:.2f}")
    total += prices[i]

print(f"\nYour total is: ${total:.2f}")
