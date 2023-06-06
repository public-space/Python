def comparison (x,y):
    if x < y: 
        print(f"x: {x} is less than y: {y}")
    elif x > y: 
        print(f"x: {x} is greater than y: {y}")
    else: 
        print(f"x: {x} is equal to y: {y}")
     
     
def get_number(prompt):
    while True: 
        try: 
            number = int(input(prompt))   
            return number
        except ValueError: 
            print("Invalid input. Please enter a valid integer.")
            
x_input = get_number("Enter a number for x: ")
y_input = get_number("Enter a number for y: ")

comparison(x_input, y_input)

