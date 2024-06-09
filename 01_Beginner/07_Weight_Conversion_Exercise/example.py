
temperature = float(input("Temperature:"))
unit = input("Is this temperature in (C)elsius or (F)ahrenheit? ").strip().upper()

if unit == "C":
    converted_temperature = (temperature * 9/5) + 32
    new_unit = "F"
elif unit == "F":
    converted_temperature = (temperature - 32) * 5/9
    new_unit = "C"
else:
    print(f"Unit {unit} was not valid.")
    exit()
print(f"The temperature is {round(converted_temperature,5), {new_unit}}")