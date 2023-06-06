from colorama import Fore
from colorama import init as colorama_init

colorama_init(autoreset=True)

colors = [x for x in dir(Fore) if x[0] != '_']

for color in colors: 
    print(color + f"{color}")
    
#* the script below prints a demo of termcolor
print("Enter: 'python3 -m termcolor' to see a demo of termcolor colors")

