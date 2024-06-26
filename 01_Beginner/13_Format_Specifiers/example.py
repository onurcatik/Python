price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is {price1}")
print(f"Price 2 is {price2}") 
print(f"Price 3 is {price3}")

# -----------

print(f"Price 1 is {price1:.2f}")
print(f"Price 2 is {price2:.2f}")
print(f"Price 3 is {price3:.2f}")
# -----------

print(f"Price 1 is ${price1:.1f}")
print(f"Price 2 is ${price2:.1f}")
print(f"Price 3 is ${price3:.1f}")

# -----------

print(f"Price 1 is ${price1:<10.2f}")
print(f"Price 2 is ${price2:<10.2f}")
print(f"Price 3 is ${price3:<10.2f}")

# -----------

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")