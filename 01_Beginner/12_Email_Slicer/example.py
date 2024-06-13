email = input("Enter your email:")

at_index = email.index('@')

username=email[:at_index]
domain = email[at_index + 1:]

print(f"Your username is : {username}")
print(f"Your domain is: {domain}")