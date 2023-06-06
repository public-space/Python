from colorama import just_fix_windows_console
from termcolor import colored

#? this fixes problems on windows
#* use Colorama to make Termcolor work on Windows too

#? use Termcolor for all colored text input
print(colored('Hello, World!', 'green', 'on_red'))