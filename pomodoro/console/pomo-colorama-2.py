# This includes foreground and background color
import time
import colorama
from colorama import Fore, Back, Style

colorama.init()

def pomodoro_timer(task_name, focus_time=25, break_time=5):
    """
    Function to start the Pomodoro timer with specified parameters.

    Args:
        task_name (str): Name of the task.
        focus_time (int): Duration of focus phase in minutes (default is 25).
        break_time (int): Duration of break phase in minutes (default is 5).
    """
    print(Fore.GREEN + Back.MAGENTA + "Pomodoro Timer")
    print(Fore.CYAN + Back.LIGHTBLUE_EX + "--------------")
    print(Fore.GREEN + Back.MAGENTA + f"Task: {task_name}")
    print(f"Focus Time: {focus_time} minutes")
    print(f"Break Time: {break_time} minutes")
    print("Let's get started!" + Style.RESET_ALL)

    while True:
        print(Fore.CYAN + Back.BLACK + "\n[Focus Phase]" + Style.RESET_ALL)
        countdown(focus_time)

        print(Fore.YELLOW + Back.BLACK + "\n[Break Phase]" + Style.RESET_ALL)
        countdown(break_time)

        choice = input(Fore.MAGENTA + "\nDo you want to continue? (y/n): " + Style.RESET_ALL)
        if choice.lower() != 'y':
            break

    print(Fore.GREEN + "\nTask completed! Good job!" + Style.RESET_ALL)

def countdown(minutes):
    """
    Function to count down the time in minutes.

    Args:
        minutes (int): Duration in minutes.
    """
    seconds = minutes * 60
    while seconds > 0:
        mins = seconds // 60  # Calculate the minutes from remaining seconds
        secs = seconds % 60  # Calculate the seconds remaining
        # The '02d' format specifier ensures that the minutes and seconds are displayed with leading zeros if needed
        print(Fore.WHITE + Back.BLACK + f"{mins:02d}:{secs:02d}", end="\r" + Style.RESET_ALL)  # Display the time in MM:SS format
        time.sleep(1)
        seconds -= 1
        
# The 'end="\r"' parameter in the 'print()' statement ensures that subsequent 'print()' statements 
# overwrite the previous line, creating a dynamic output that updates on the same line. 

def main():
    task_name = input(Fore.LIGHTBLUE_EX + Back.BLACK + "Enter the task name: ")
    default_choice = input(Fore.CYAN + Back.BLACK + "Use default times (25 minutes focus and 5 minutes break)? (y/n): ")
    
    if default_choice.lower() == 'n':
        focus_time = int(input(Fore.MAGENTA + Back.BLACK + "Enter the focus time in minutes: "))
        break_time = int(input(Fore.MAGENTA + Back.BLACK + "Enter the break time in minutes: "))
    else:
        focus_time = 25
        break_time = 5
    
    pomodoro_timer(task_name, focus_time, break_time)

if __name__ == '__main__':
    main()
