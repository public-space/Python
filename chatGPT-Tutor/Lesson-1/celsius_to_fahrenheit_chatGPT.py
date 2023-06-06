def celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 9/5) + 32
    return fahrenheit

# Prompt for user input
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit using the function
result = celsius_to_fahrenheit(celsius)

# Print the result
print("The temperature in Fahrenheit is", result)
