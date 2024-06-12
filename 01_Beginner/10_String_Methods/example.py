name = input("Enter your full name:")
result= len(name)
print(f"The length of your name is {result}")
result = name.find("B")
print(f"The first occurence of 'B' is at index: {result}")
result = name.rfind("o")
print(f"The last occurence of 'o' is at index: {result}")

# ------

name_upper = name.upper()
print(f"Uppercase name: {name_upper}")

name_lower = name.lower()
print(f"Lowercase name: {name_lower}")

# ---------

numeric_string = "12345"
result = numeric_string.isdigit()
print(f"Is the string '12345' all digits? {result}")


#  --------------

phone_number = input("Enter your phone number:")
dash_count = phone_number.count("-")
print(f"Number dashes: {dash_count}")

phone_number = phone_number.replace("-", "")
print(f"Spaces: {phone_number}")

# ------

username = input("Enter a username:")

if len(username) > 12:
    print("Your username cant be more than 12 characters")
else:
    if username.find(" ") != -1:
        print("Your username can't contain spaces.")
    else:
        if not username.isalpha():
            print("Your user name cant numbers.")
        else:
            print(f"Welcome, {username}!")