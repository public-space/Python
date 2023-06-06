import datetime

def days_left_in_year(date=None):
    if date is None:
        today = datetime.date.today()
    else:
        today = datetime.datetime.strptime(date, '%Y-%m-%d').date()

    end_of_year = datetime.date(today.year, 12, 31)
    days_left = (end_of_year - today).days
    return days_left

# Ask user for input
while True:
    user_input = input("Enter a specific date (YYYY-MM-DD) or press Enter for today's date: ")
    
    try:
        if user_input:
            days_remaining = days_left_in_year(date=user_input)
        else:
            days_remaining = days_left_in_year()

        # Output the result
        print(f"There are {days_remaining} days left in the year.")
        break

    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
