def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1, 2))        
print(add(1, 2, 3))     
print(add(1, 2, 3, 4))   


# ----------------

def print_addres(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_addres(street="123 Fake Steet",  state="MI", city="New York")



# ----------------

def shipping_label(*args , **kwargs):
    for arg in args:
        print(arg, end=' ')
    print()

    if 'street' in kwargs:
        print(kwargs.get("street"), end = " ")
        if 'apartment' in kwargs:
            print(f", Apartment {kwargs.get('apartment')}")
        elif 'po_box' in kwargs:
            print(f", PO Box {kwargs.get('po_box')}")
        else:
            print()
        if 'city' in kwargs and 'state' in kwargs and 'zip_code' in kwargs:
            print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip_code')}")

shipping_label("Dr. John Doe", street="123 Fake Street", city="Detroit", state="MI", zip_code="54321")
shipping_label("Dr. John Doe", "III", street="123 Fake Street", apartment="100", city="Detroit", state="MI", zip_code="54321")
shipping_label("Dr. John Doe", "III", street="123 Fake Street", po_box="1001", city="Detroit", state="MI", zip_code="54321")



