import sys
from colorama import just_fix_windows_console
from termcolor import colored, cprint

text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
#! doesn't blink on windows

print(text)

cprint("Hello, world!", "green", "on_red")

print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")

print_red_on_cyan("Hello World!")
print_red_on_cyan("Hello, Universe!")

for i in range(10):
    cprint(i, "magenta", end="")
    
cprint("Attention!", "red", attrs=["bold"], file=sys.stderr)