# Python Temperature Conversion 

## Steps to Create the Program

1. **Prompt the user for the unit of measurement.**
2. **Prompt the user for the temperature.**
3. **Convert the temperature based on the unit of measurement.**
4. **Handle invalid inputs gracefully.**

## Code Implementation

Here is a step-by-step breakdown of the program:

### Step 1: Prompt for the Unit of Measurement

We will start by asking the user whether the temperature is in Celsius or Fahrenheit.

```python
# Prompt the user to enter the unit of measurement
unit = input("Is the temperature in Celsius or Fahrenheit (C/F)? ").strip().upper()
```

### Step 2: Prompt for the Temperature

Next, we will prompt the user to enter the temperature value. We will store this value in a variable and convert it to a floating-point number for precise calculations.

```python
# Prompt the user to enter the temperature
temp = float(input("Enter the temperature: "))
```

### Step 3: Convert the Temperature

We will use conditional statements to convert the temperature based on the unit of measurement provided by the user. The formulas for conversion are:
- **Celsius to Fahrenheit:** \((temp \times \frac{9}{5}) + 32\)
- **Fahrenheit to Celsius:** \((temp - 32) \times \frac{5}{9}\)

```python
# Convert the temperature based on the unit of measurement
if unit == 'C':
    # Convert Celsius to Fahrenheit
    temp_in_fahrenheit = round((temp * 9/5) + 32, 1)
    print(f"The temperature in Fahrenheit is {temp_in_fahrenheit}°F")
elif unit == 'F':
    # Convert Fahrenheit to Celsius
    temp_in_celsius = round((temp - 32) * 5/9, 1)
    print(f"The temperature in Celsius is {temp_in_celsius}°C")
else:
    # Handle invalid unit input
    print(f"{unit} is an invalid unit of measurement.")
```

### Complete Program

Combining all the steps, the complete program is as follows:

```python
def temperature_conversion():
    # Prompt the user to enter the unit of measurement
    unit = input("Is the temperature in Celsius or Fahrenheit (C/F)? ").strip().upper()

    # Check for valid unit input
    if unit not in ['C', 'F']:
        print(f"{unit} is an invalid unit of measurement.")
        return

    # Prompt the user to enter the temperature
    try:
        temp = float(input("Enter the temperature: "))
    except ValueError:
        print("Invalid temperature value. Please enter a numeric value.")
        return

    # Convert the temperature based on the unit of measurement
    if unit == 'C':
        # Convert Celsius to Fahrenheit
        temp_in_fahrenheit = round((temp * 9/5) + 32, 1)
        print(f"The temperature in Fahrenheit is {temp_in_fahrenheit}°F")
    elif unit == 'F':
        # Convert Fahrenheit to Celsius
        temp_in_celsius = round((temp - 32) * 5/9, 1)
        print(f"The temperature in Celsius is {temp_in_celsius}°C")

# Run the temperature conversion program
if __name__ == "__main__":
    temperature_conversion()
```

### Explanation

1. **Unit Prompt and Validation:**
   - We prompt the user to input the unit of measurement.
   - The input is stripped of leading/trailing spaces and converted to uppercase to ensure uniformity.
   - We check if the unit is either 'C' or 'F'. If not, we display an error message and exit the program.

2. **Temperature Input and Validation:**
   - We prompt the user to input the temperature.
   - We use a try-except block to handle non-numeric input gracefully.

3. **Temperature Conversion:**
   - If the unit is 'C', we convert the temperature from Celsius to Fahrenheit and print the result.
   - If the unit is 'F', we convert the temperature from Fahrenheit to Celsius and print the result.

4. **Main Function:**
   - We define the main function to encapsulate the program logic.
   - We use the `if __name__ == "__main__":` construct to ensure the program runs only when executed directly, not when imported as a module.

