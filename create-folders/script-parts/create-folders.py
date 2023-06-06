import os

def create_folders():
    num_folders = int(input("How many folders would you like to create? "))
    folder_name = input("Enter the name of the folders: ")
    
    for number in range(1, num_folders + 1):
        folder = f"{folder_name}-{number}"
        
        folder_path = os.path.join(os.getcwd(), folder)  #? Get the absolute path of the folder
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
            print(f"Folder '{folder}' create successfully!")
            
        else: 
            print(f"Folder {folder}' already exists!")
            
if __name__ == '__main__':
    create_folders()