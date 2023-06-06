def get_float(): 
    while True: 
        try: 
            number = float(input("Enter a number between 0.0 and 1.0: "))
            if number >= 0.9 and number <= 1.0:
               return "A"
            elif number >= 0.8 and number < 0.9:
                return "B"
            elif number 

            else:
                print("Invalid input. Please enter a number between 0.0 and 1.0.")
        except ValueError:  
            print("Invalid input. Please enter a valid number.")    
            
            
print(get_float())