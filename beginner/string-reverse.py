import colorama
from colorama import Fore, Back, Style

fruit = 'banana'


print("Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.")

index = len(fruit)
while index > 0: 
    letter = fruit[index-1]
    print(Fore.GREEN + letter)
    index -=1
    
print(Style.RESET_ALL)

# ? DUDE I FIGURED THIS ONE OUT ALL ON MY OWNNNNNNNNNN!!!!!!!!!!!!!!!!!!!!!!!!!!!!