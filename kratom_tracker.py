from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from datetime import datetime
import json
import hashlib


class KratomTracker:
    def __init__(self):
        self.doses = []

    def start(self):
        self.doses = []  # Reset doses list
        self.record_dose()  # Start recording doses

    def record_dose(self):
        while True:
            dose_amount = input("Enter the dose amount:", type=FLOAT)
            dose_unit = select("Select dose unit:", ['grams', 'teaspoons', 'capsules'])

            dose_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            dose = {
                'amount': dose_amount,
                'unit': dose_unit,
                'time': dose_time
            }
            self.doses.append(dose)

            if not actions(buttons=['Record Next Dose']):
                break  # Exit the loop if the user doesn't want to record another dose

    def save_doses(self, username):
        with open(f'{username}_doses.json', 'w') as file:
            json.dump(self.doses, file)

    def load_doses(self, username):
        try:
            with open(f'{username}_doses.json', 'r') as file:
                self.doses = json.load(file)
        except FileNotFoundError:
            pass  # If the file doesn't exist, continue with an empty doses list

    def compare_dose_times(self):
        if len(self.doses) < 2:
            return "Insufficient data to compare dose times"

        comparisons = []
        for i in range(1, len(self.doses)):
            prev_time = datetime.strptime(self.doses[i-1]['time'], '%Y-%m-%d %H:%M:%S')
            curr_time = datetime.strptime(self.doses[i]['time'], '%Y-%m-%d %H:%M:%S')
            time_diff = curr_time - prev_time
            comparisons.append(f"Time difference between dose {i-1} and {i}: {time_diff}")

        return comparisons


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._hash_password(password)  # Store the hashed password
        self.tracker = KratomTracker()

    def _hash_password(self, password):
        # Hash the password using SHA-256 algorithm
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self, password):
        if self._hash_password(password) == self.password:
            return True
        return False

    def logout(self):
        # Implement your logout logic here
        pass

    def save_data(self):
        self.tracker.save_doses(self.username)

    def load_data(self):
        self.tracker.load_doses(self.username)


users = []  # List to store user instances
tracker = None  # Global variable for the tracker instance

def create_user():
    username = input("Enter a username:", required=True)
    password = input("Enter a password:", type=PASSWORD, required=True)

    user = User(username, password)
    users.append(user)

    put_text("User created successfully!")

def login():
    username = input("Enter your username:", required=True)
    password = input("Enter your password:", type=PASSWORD, required=True)

    for user in users:
        if user.username == username:
            if user.login(password):
                put_text(f"Logged in as {username}")
                return user
            else:
                put_text("Invalid password.")
                return None

    put_text("User not found.")
    return None

@use_scope('kratom_tracker', clear=True)
def main():
    global tracker

    put_markdown(readme)  # Display the README contents

    if not tracker:
        # User is not logged in
        put_buttons(['Create User'], onclick=[create_user])
        user = login()
        if not user:
            return

        user.load_data()
        tracker = user.tracker

    if not tracker.doses:
        put_buttons(['Start Tracking'], onclick=[tracker.start])
    else:
        put_text('Doses Recorded:')
        for dose in tracker.doses:
            put_text(f"Amount: {dose['amount']} {dose['unit']}, Time: {dose['time']}")

        put_buttons(['Record Next Dose'], onclick=[tracker.record_dose])
        put_buttons(['Save Doses'], onclick=[tracker.save_doses, tracker.username])

        comparisons = tracker.compare_dose_times()
        if comparisons:
            put_text('Comparisons:')
            for comparison in comparisons:
                put_text(comparison)

    put_buttons(['Logout'], onclick=[user.logout])

tracker = None
readme = """
# Kratom Consumption Tracker

This is a program to track kratom consumption. It allows users to record their doses and view the dose history.

## Instructions
1. Create a new user account by clicking the **Create User** button.
2. Log in with your username and password.
3. Start tracking your kratom consumption by clicking the **Start Tracking** button.
4. Enter the dose amount, select the unit, and click **Record Next Dose** to record a dose.
5. View your dose history and compare dose times.
6. Click **Save Doses** to save your dose data.
7. Click **Logout** to log out of your account.

"""

start_server(main, port=8080)
