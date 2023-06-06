from termcolor import colored, cprint

#* This is a temperature Conversion script to convert from 
#* Celsius to fahrenheit
#* F = (C * 9/5) + 32

def celsius_to_fahrnheit(temp):
    temp = colored(input("Enter temperature in celsius: "), "green", "on_red")
    fahrenheit = (temp * (9 // 5) + 32)
    cprint(f"The temperature in Fahrenheit is {fahrenheit}")
    
celsius_to_fahrnheit()