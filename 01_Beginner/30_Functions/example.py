def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

result_add = add(1,2)
result_subract = subtract(1,2)
result_multiply = multiply(1,2)
result_divide = divide(1,2)

print(result_add)
print(result_subract)
print(result_multiply)
print(result_divide)

# --------------------------

def create_full_name(first_name , last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return f"{first_name} {last_name}"

full_name = create_full_name("onur" , "çatık")

print(full_name)


# --------------------------


def greeting():
    print("Hello World")
    print("Hello World")
    print("Hello World")
greeting()


# --------------------------

def happy_birthday(name):
    print(f"Happy Birthday {name}")

happy_birthday("Onur")
happy_birthday("Joe")
happy_birthday("Doe")



# --------------------------

def happy_birthday(name, age):
    print(f"Happy Birthday {name}, you are {age} years old.")
    print(f"You are {age}")
    print(f"Your name is {name}")

happy_birthday("Onur", 25)
happy_birthday("Joe", 25)
happy_birthday("Doe", 25)
