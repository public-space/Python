Certainly! Here's the first lesson, including the exercise, solution, and explanation, in markdown format:

---

## Lesson 1: Temperature Conversion

In this lesson, we'll learn how to write a Python program that converts temperature from Celsius to Fahrenheit. We'll start with an exercise and then go through the solution and an explanation of the code.

### Exercise

Write a Python program that converts temperature from Celsius to Fahrenheit. The program should prompt the user to enter a temperature in Celsius and display the corresponding temperature in Fahrenheit.

To convert temperature from Celsius to Fahrenheit, you can use the following formula:

```
F = (C * 9/5) + 32
```

Write a function called `celsius_to_fahrenheit` that takes a temperature in Celsius as a parameter and returns the equivalent temperature in Fahrenheit. Test your function by calling it with different temperature values.

### Solution

Here's an implementation of the `celsius_to_fahrenheit` function:

```python
def celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 9/5) + 32
    return fahrenheit

# Prompt for user input
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit using the function
result = celsius_to_fahrenheit(celsius)

# Print the result
print("The temperature in Fahrenheit is", result)
```

### Explanation

In the solution, we define a function called `celsius_to_fahrenheit` that takes a temperature in Celsius as a parameter. Inside the function, we use the provided formula to convert the temperature to Fahrenheit. The result is then returned.

In the main part of the code, we prompt the user to enter a temperature in Celsius using the `input` function. The input is converted to a float using the `float` function to ensure we can perform calculations. We then call the `celsius_to_fahrenheit` function with the user's input as an argument and store the result in the `result` variable.

Finally, we print the result using the `print` function.

### Testing

You can test the program by running it and entering different temperature values in Celsius. The program will calculate and display the corresponding temperature in Fahrenheit.

---

I hope this lesson helps you understand the temperature conversion concept in Python. If you have any questions or need further clarification, please let me know.