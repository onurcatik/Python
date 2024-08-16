from functools import reduce

prices = [15.5, 20.3, 10.2, 4.7]

total = reduce(lambda x, y: x+y, prices)
print(f"Total: ${total:.2f}")

# ----------------------

total = 0
for price in prices:
    total += price

print(f"Total: ${total:.2f}")