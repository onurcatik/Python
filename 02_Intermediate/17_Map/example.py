def celsius_to_fahrenheit(temp):
    return ( temp *  9/5) + 32

celsius_temps = [0, 20, 37, 100]

# Apply the celsius_to_fahrenheit function to each item in the list
fahrenheit_temps = map(celsius_to_fahrenheit, celsius_temps)

# Convert the map object to a list
fahrenheit_temps = list(fahrenheit_temps)

# Print the result
print(fahrenheit_temps)

#  --------------

fahrenheit_temps = list(map(lambda temp: (temp * 9/5)+ 32, celsius_temps))

print(fahrenheit_temps)

# ------------------------

def celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))
print("Using defined function:", fahrenheit_temps)

fahrenheit_temps = list(map( lambda temp : (temp* 9/5)+32 ,celsius_temps))
print("Using lambda function:", fahrenheit_temps)