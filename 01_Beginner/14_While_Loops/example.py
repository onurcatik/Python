num = int(input("Enter a number between 1 and 10:"))

while num < 1 or num > 10:
    print(f"{num} is not valid.")
    num = int(input("Enter a number between 1 and 10:"))
print(f"Your number is {num}.")


#  --------------

age = int(input("Enter your age:"))

while age <= 0:
    print("Age cant be negative or zero:")
    age = int(input("Enter your age:"))
print(f"You are {age}  years old.")