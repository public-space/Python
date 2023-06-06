# Web App Idea - Kratom Usage Tracker

## Overview
I am making a web app that tracks Kratom usage for users who are trying to quit. The app focuses on helping users understand the timing of their dosing and provides insights into their usage patterns.

## Functionality

1. Timer: The app will have a timer that users can start once they have dosed.
   - If it is the user's first dose, the timer starts for the first time.
   - If it is not their first dose, the dose is logged in an array, recording the number of doses per session.

2. Session: A session represents the number of times the user doses until they have a final dose and quit the timer.

3. Dose Tracking: Each dose will be recorded as:
   - Actual time of the dose.
   - Time since the first dose.
   - Time since the previous dose.

4. Best Time: The app will keep track of the "best time," which is the longest amount of time between two doses the user takes.

5. Worst Time: The app will track the "worst time," which is the shortest time between doses.

6. Comparison Function: Whenever the user takes a new dose, a function will check and compare the current time between doses to the shortest and longest times.

7. User Feedback: The user will be notified if their time between doses is the longest time.

8. Session Control: A button will allow the user to stop the session and halt dose tracking.

9. Dose Information Form: The form will not only ask when the user doses but also allow them to input the amount taken, with options for grams or teaspoons.

10. Cumulative Amount: The app will keep track of the total amount the user has taken from the beginning of the session to the end.

11. Modular Code: The functionality will be implemented through separate functions to enhance code organization and maintainability.

## User Interface

1. Simple and Clean: The UI will be designed to be extremely simple and clean.

2. Technologies:

   - HTML5: To structure the web app using up-to-date semantic elements.
   - CSS: For basic styling and visual enhancements.
   - JavaScript: To handle the timer and implement all the required functions.

## Data Handling

1. Data Storage: You are unsure whether to use Express or Firebase to handle the data saved for doses, timings, and other relevant information.
