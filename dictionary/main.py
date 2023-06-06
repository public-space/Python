import pandas as pd
import datetime
import csv
import os

def prompt_dose():
    dose_status = input("Are you taking a Kratom dose today (yes/no)? ")
    if dose_status.lower() == 'yes':
        dose_amount = input("Enter the amount in grams: ")
        return dose_amount
    else:
        return None

def get_todays_date():
    today = datetime.date.today()
    return today

def get_week_range(date):
    start = date - datetime.timedelta(days=date.weekday())
    end = start + datetime.timedelta(days=6)
    return start, end

def save_dose(dose, date, week_range):
    # check if doses.csv exists, if not, create it.
    if not os.path.isfile('./data/doses.csv'):
        with open('./data/doses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Timestamp", "Dose", "Day", "Week_Start", "Week_End"])

    # read doses.csv and get last id, if empty set id to 1
    df = pd.read_csv('./data/doses.csv')
    if df.empty:
        id = 1
    else:
        id = df['ID'].max() + 1

    # save dose to csv file
    with open('./data/doses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, datetime.datetime.now(), dose, date, week_range[0], week_range[1]])

def check_and_save_for_day(dose):
    date = get_todays_date()

    # check if doses.csv exists and if a dose has been saved for the day
    if os.path.isfile('./data/doses.csv'):
        df = pd.read_csv('./data/doses.csv')
        if not df[df['Day'] == str(date)].empty:
            print("A dose for today has already been saved.")
            return

    week_range = get_week_range(date)
    save_dose(dose, date, week_range)

def check_and_save_for_week(dose):
    date = get_todays_date()
    week_range = get_week_range(date)

    # check if doses.csv exists and if a dose has been saved for the week
    if os.path.isfile('./data/doses.csv'):
        df = pd.read_csv('./data/doses.csv')
        if not df[(df['Week_Start'] == str(week_range[0])) & (df['Week_End'] == str(week_range[1]))].empty:
            print("A dose for this week has already been saved.")
            return

    save_dose(dose, date, week_range)

def main():
    dose = prompt_dose()
    if dose:
        check_and_save_for_day(dose)
        check_and_save_for_week(dose)
    else:
        print("No dose information to record for today.")

if __name__ == "__main__":
    main()

