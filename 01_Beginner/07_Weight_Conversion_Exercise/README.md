# Python Weight Conversion Exercise 🏋️


## Objective
The objective of this exercise is to create a weight conversion program that:
1. Prompts the user to enter a weight.
2. Prompts the user to specify the unit of the weight (kilograms or pounds).
3. Converts the weight to the desired unit.
4. Displays the converted weight along with the appropriate unit.

## Steps
1. **Create a weight variable and assign it user input.**
2. **Convert the user input into a floating-point number.**
3. **Ask for the unit of the weight (kilograms or pounds).**
4. **Use if statements to determine the conversion direction.**
5. **Reassign the weight variable based on the conversion.**
6. **Display the converted weight.**

## Code Implementation

Here is the detailed code implementation for the weight converter program:

```python
# Weight Converter Program in Python

# Step 1: Prompt the user to enter their weight
weight_input = input("Enter your weight: ")

# Step 2: Convert the user input into a floating-point number
try:
    weight = float(weight_input)
except ValueError:
    print("Invalid weight entered. Please enter a numerical value.")
    exit()

# Step 3: Ask for the unit of the weight (kilograms or pounds)
unit = input("Is this weight in (K)ilograms or (L)bs? ").strip().upper()

# Step 4: Use if statements to determine the conversion direction
if unit == 'K':
    # Convert kilograms to pounds
    converted_weight = weight * 2.205
    new_unit = 'lbs'
elif unit == 'L':
    # Convert pounds to kilograms
    converted_weight = weight / 2.205
    new_unit = 'kgs'
else:
    print(f"Unit '{unit}' was not valid.")
    exit()

# Step 5: Round the converted weight to one decimal place
converted_weight = round(converted_weight, 1)

# Step 6: Display the converted weight
print(f"Your weight is {converted_weight} {new_unit}.")
```

## Explanation

### Step 1: Prompt the User to Enter Their Weight
We start by prompting the user to enter their weight. The input is taken as a string.
```python
weight_input = input("Enter your weight: ")
```

### Step 2: Convert the User Input into a Floating-Point Number
To handle potential errors, we use a try-except block to convert the input to a floating-point number.
```python
try:
    weight = float(weight_input)
except ValueError:
    print("Invalid weight entered. Please enter a numerical value.")
    exit()
```

### Step 3: Ask for the Unit of the Weight
The user is asked to specify the unit of the weight, which is then converted to uppercase and stripped of any leading or trailing whitespace.
```python
unit = input("Is this weight in (K)ilograms or (L)bs? ").strip().upper()
```

### Step 4: Use if Statements to Determine the Conversion Direction
We use if statements to check the unit and perform the appropriate conversion. If the unit is invalid, an error message is displayed and the program exits.
```python
if unit == 'K':
    converted_weight = weight * 2.205
    new_unit = 'lbs'
elif unit == 'L':
    converted_weight = weight / 2.205
    new_unit = 'kgs'
else:
    print(f"Unit '{unit}' was not valid.")
    exit()
```

### Step 5: Round the Converted Weight to One Decimal Place
The converted weight is rounded to one decimal place for a cleaner output.
```python
converted_weight = round(converted_weight, 1)
```

### Step 6: Display the Converted Weight
Finally, we display the converted weight along with the appropriate unit.
```python
print(f"Your weight is {converted_weight} {new_unit}.")
```

## Conclusion
This exercise demonstrates how to create a simple weight conversion program in Python. By using if statements and handling user input carefully, we ensure the program operates correctly and provides accurate results. This approach helps reinforce the concepts of conditional statements and input handling in Python.