def temperature_conversion():
    unit = input("Celsius or Fahrenheit (C/F)? ").strip().upper()
    if unit not in ['C', 'F']:
        print(f"{unit} is an invalid unit of measurement.")
        return
    try:
        temp = float(input("Enter the temperature: "))
    except ValueError:
        print("Invalid temperature value.")
        return
    if unit == "C":
        temp_in_fahrenheit = round((temp * 9/5) + 32, 1)
        print(f"The temperature in Fahrenheit is {temp_in_fahrenheit}°F")
    elif unit == "F":
        temp_in_celsius = round((temp - 32) * 5/9, 1)
        print(f"The temperature in Celsius is {temp_in_celsius}°C")

if __name__ == '__main__':
    temperature_conversion()




