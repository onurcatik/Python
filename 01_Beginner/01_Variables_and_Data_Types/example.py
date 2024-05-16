# Declaring variables
age = 21
players = 2
quantity = 5
gpa = 3.2
distance = 2.5
price = 10.99
name = "John"
food = "Pizza"
email = "example@gmail.com"
online = True
for_sale = False
running = True

# Printing variables
print("Age:", age)
print("Number of players online:", players)
print("Quantity to buy:", quantity)
print("GPA:", gpa)
print("Distance run:", distance, "kilometers")
print("Price:", "$" + str(price))
print("Name:", name)
print("Favorite food:", food)
print("Email:", email)
print("Online status:", online)
print("Item for sale:", for_sale)
print("Game running:", running)

# Using F-strings for cleaner syntax
print(f"I am {age} years old and my name is {name}.")
print(f"My favorite food is {food} and my GPA is {gpa}.")

# Multiple assignment
x, y, z = 1, 2, 3
print("x:", x, "y:", y, "z:", z)

# Setting multiple variables to the same value
x = y = z = 0
print("x:", x, "y:", y, "z:", z)
