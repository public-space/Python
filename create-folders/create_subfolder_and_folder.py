import os
from datetime import datetime, timedelta

def get_valid_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def create_folders_with_readme():
    num_folders = get_valid_integer_input("How many folders would you like to create? ")
    folder_name = input("Enter the name of the folders: ")

    start_date = input("Enter the start date (YYYY-MM-DD), or press Enter to use today's date: ")
    if not start_date:
        start_date = datetime.today().strftime("%Y-%m-%d")

    user_name = input("Enter your name: ")

    subfolder_names = []  # List to store subfolder names

    populate_subfolders = input("Do you want to populate the folders with subfolders? (yes/no): ")
    if populate_subfolders.lower() == "yes":
        num_subfolders = get_valid_integer_input("How many subfolders would you like to create? ")

        for i in range(num_subfolders):
            subfolder_name = input(f"Enter the name of subfolder {i + 1}: ")
            subfolder_names.append(subfolder_name)

    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        for number in range(1, num_folders + 1):
            folder = f"{number}-{folder_name}"
            folder_path = os.path.join(os.getcwd(), folder)  # Get the absolute path of the folder

            try:
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                    print(f"Folder '{folder}' created successfully!")

                    readme_text = f"# Name: {user_name}\n# Date: {start_date.strftime('%B %d, %Y')}"
                    readme_path = os.path.join(folder_path, "readme.md")
                    with open(readme_path, "w") as readme_file:
                        readme_file.write(readme_text)
                        print(f"Readme file created for '{folder}' with name and date")

                    for subfolder_name in subfolder_names:
                        subfolder_path = os.path.join(folder_path, subfolder_name)
                        if not os.path.exists(subfolder_path):
                            os.makedirs(subfolder_path)
                            print(f"Subfolder '{subfolder_name}' created successfully!")
                        else:
                            print(f"Subfolder '{subfolder_name}' already exists!")

                else:
                    print(f"Folder '{folder}' already exists!")
            except OSError as e:
                print(f"Error creating folder '{folder}': {str(e)}")
            except IOError as e:
                print(f"Error creating readme file for '{folder}': {str(e)}")
            finally:
                start_date += timedelta(days=1)  # Increment the start date by one day for the next folder
    except ValueError:
        print("Invalid start date format. Please provide the date in YYYY-MM-DD format.")

create_folders_with_readme()
