

def create_folders():
    num_folders = int(input("How many folders would you like to create? "))
    
    folder_name = input("Enter the name of the folders: ")
    
    #* Iterates and prints folder names out
    for number in range(1, num_folders + 1):
        folder = f"{folder_name}-{number}"
        print (folder)
        
if __name__ == '__main__': 
    create_folders()

    