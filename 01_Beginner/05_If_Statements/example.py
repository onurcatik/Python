name = input("Enter your name:")

if name == "":
    print("Not have Name.")
else:
    print(f"Hello, {name}")

#  ---


age = int(input("Enter your age:"))

if age >= 18:
    print("You are now signed up")
else:
    print("Sorry, you are too young to sign up")

# ---


age = int(input("Enter your age:"))

if age >= 30:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("Sorry")



