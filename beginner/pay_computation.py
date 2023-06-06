def get_number(prompt):
    while True: 
        try: 
            number = float(input(prompt))   
            return number
        except ValueError: 
            print("Invalid input. Please enter a valid integer.")
            
def get_pay(): 
    hours = get_number("Enter the number of hours worked: ")
    rate = get_number("Enter the hourly rate: ")
    if hours > 40: 
        pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
    else:
        pay = hours * rate
    return f"Your Pay for this week is ${pay}"

        
print(get_pay())
            
            