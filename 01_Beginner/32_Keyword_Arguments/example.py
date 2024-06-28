def hello(greeting , title , first_name, last_name):
    print(f"{greeting}, {title}  {first_name}  {last_name}")

hello("Hello", "Mr." , "Sünger" , "Square")


hello(greeting="Hello", title="Mr.", first_name="Sünger", last_name="Square")

hello( last_name="SquarePants" , first_name="Sünger" , greeting="Hello" , title="Mr.")

hello(title="Mr." , first_name="Sponge" , last_name="Square" , greeting="Hello")


# --------------------

for i in range(1,6):
    print(i, end=" ")

print("1" , "2", "3", "4" , "5" ,sep="-") 


# --------------------

def get_phone_number(country_code, area_code , first_digits, last_digits):
    return f"{country_code}-{area_code}-{first_digits}-{last_digits}"

phone_num=get_phone_number(country_code="1", area_code="123", first_digits="456" , last_digits="7890")

print(phone_num)
