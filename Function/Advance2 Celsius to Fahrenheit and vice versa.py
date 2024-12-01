#2. Create a function that converts a given temperature from 
# Celsius to Fahrenheit and vice versa
def convert_temperature(temp, unit):
    if unit.lower() == 'c':
        # Convert from Celsius to Fahrenheit
        return (temp * 9/5) + 32
    elif unit.lower() == 'f':
        # Convert from Fahrenheit to Celsius
        return (temp - 32) * 5/9
    else:
        return "Invalid unit"

# Input from the user
temperature = float(input("Enter the temperature: "))
unit = input("Is this temperature in Celsius (C) or Fahrenheit (F)? ")

# Call the function and print the result
converted_temp = convert_temperature(temperature, unit)
if unit.lower() == 'c':
    print(temperature, "degrees Celsius is equal to", converted_temp, "degrees Fahrenheit.")
elif unit.lower() == 'f':
    print(temperature, "degrees Fahrenheit is equal to", converted_temp, "degrees Celsius.")
else:
    print(converted_temp)

