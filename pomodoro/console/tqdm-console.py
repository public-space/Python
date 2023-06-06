# this works but it updates to the screen every new line and I don't feel like 
#fucking around with it to get it to stop rn
import time
from tqdm import tqdm

def pomodoro_timer(task_name, focus_time=25, break_time=5):
    """
    Function to start the Pomodoro timer with specified parameters.

    Args:
        task_name (str): Name of the task.
        focus_time (int): Duration of focus phase in minutes (default is 25).
        break_time (int): Duration of break phase in minutes (default is 5).
    """
    print("Pomodoro Timer")
    print("--------------")
    print(f"Task: {task_name}")
    print(f"Focus Time: {focus_time} minutes")
    print(f"Break Time: {break_time} minutes")
    print("Let's get started!")

    while True:
        print("\n[Focus Phase]")
        countdown(focus_time)

        print("\n[Break Phase]")
        countdown(break_time)

        choice = input("\nDo you want to continue? (y/n): ")
        if choice.lower() != 'y':
            break

    print("\nTask completed! Good job!")

def countdown(minutes):
    """
    Function to count down the time in minutes.

    Args:
        minutes (int): Duration in minutes.
    """
    seconds = minutes * 60
    for remaining in tqdm(range(seconds), desc="Time Remaining", unit="s", dynamic_ncols=True):
        mins = remaining // 60  # Calculate the minutes from remaining seconds
        secs = remaining % 60  # Calculate the seconds remaining
        # The '02d' format specifier ensures that the minutes and seconds are displayed with leading zeros if needed
        print(f"{mins:02d}:{secs:02d}", end="\r")  # Display the time in MM:SS format
        time.sleep(1)
        
# The 'end="\r"' parameter in the 'print()' statement ensures that subsequent 'print()' statements 
# overwrite the previous line, creating a dynamic output that updates on the same line. 

def main():
    task_name = input("Enter the task name: ")
    default_choice = input("Use default times (25 minutes focus and 5 minutes break)? (y/n): ")
    
    if default_choice.lower() == 'n':
        focus_time = int(input("Enter the focus time in minutes: "))
        break_time = int(input("Enter the break time in minutes: "))
    else:
        focus_time = 25
        break_time = 5
    
    pomodoro_timer(task_name, focus_time, break_time)

if __name__ == '__main__':
    main()
