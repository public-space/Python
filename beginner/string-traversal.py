import colorama
from colorama import Fore, Back, Style

fruit = 'banana'
letter = fruit[1]
print(Fore.LIGHTCYAN_EX + f"the second letter is {letter}")
# * A string is a sequence. 

length = len(fruit)

print(f"the length of the string is {length}")

last = fruit[length-1]

print(f"the last letter is {last}")

print(Back.LIGHTMAGENTA_EX + Fore.GREEN + "looping through a string using a 'while' loop")

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index +=1
    

print(Back.GREEN + Fore.LIGHTCYAN_EX + "looping through a string using a 'for' loop")

for char in fruit: 
    print(f"the letter is {char}")
    


