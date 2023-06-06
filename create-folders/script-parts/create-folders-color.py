from colorama import just_fix_windows_console, Fore, Back

def create_folders():
    num_folders = int(input(Fore.LIGHTCYAN_EX + Back.RED + "How many folders would you like to create? "))
    
    folder_name = input("Enter the name of the folders: ")
    
    for number in range(1, num_folders + 1):
        folder = f"{folder_name}-{number}"
        print (Fore.RED + Back.LIGHTBLUE_EX+ folder)
        
if __name__ == '__main__': 
    create_folders()

    