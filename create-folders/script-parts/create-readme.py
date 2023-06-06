import datetime

def create_folders_and_readme():
    num_folders = int(input("How many folders would you like to create? "))
    folder_name = input("Enter the name of the folders: ")
    
    start_date_input = input("Enter the start date (leave blank for today's date): ")
    
    if start_date_input: 
        start_date = datetime.datetime.strptime(start_date_input, "%Y-%m-%d").date()
    else: 
        start_date = datetime.date.today()
        
    for number in range(1, num_folders + 1):
        folder = f"{folder_name}-{number}"
        folder_date = start_date + datetime.timedelta(days=number - 1)
        
        readme_content = folder_date.strftime("%B %d, %Y")
        
        print(f"Creating folder: {folder}")
        print(f"Readme content: {readme_content}")
        
        #TODO:  Create the folder
        #? Your code to create the folder goes here
        
        #* Create the readme.md file
        readme_file_path = f"{folder}/readme.md"
        with open(readme_file_path, "w") as readme_file:
            readme_file.write(readme_content)
