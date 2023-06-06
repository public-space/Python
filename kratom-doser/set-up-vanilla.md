Certainly! Here's a guide on how to implement your web app using HTML, CSS, and JavaScript without Firebase:

1. **HTML Structure:**
   - Create an HTML file and define the basic structure of your web app using HTML5 semantic elements.
   - Include necessary elements like buttons, forms, containers, and placeholders for displaying data.

2. **CSS Styling:**
   - Write CSS rules to style your web app according to your design preferences.
   - Apply styles to elements, containers, buttons, forms, and other components to create a clean and appealing UI.

3. **JavaScript Functionality:**
   - Begin by creating a JavaScript file and linking it to your HTML file.
   - Implement functions to handle various functionalities of your app.

4. **Timer Functionality:**
   - Write JavaScript code to handle the timer functionality.
   - Implement a timer that starts and stops based on user actions.
   - Calculate the time elapsed since the first dose and the previous dose.

5. **Dose Tracking:**
   - Create an array or data structure to store dose information.
   - Implement functions to log each dose, including the actual time, time since the first dose, and time since the previous dose.

6. **Best and Worst Time Calculation:**
   - Write functions to calculate the best and worst times between doses.
   - Compare the current time between doses with the shortest and longest times and update them accordingly.

7. **User Interface Updates:**
   - Use JavaScript to update the UI dynamically with relevant information.
   - Display the best and worst times, the current session's dose count, and any other relevant data.

8. **User Interaction:**
   - Implement event listeners for buttons and form submissions to capture user interactions.
   - Allow users to start and stop the timer, log doses, and input dose amounts.

9. **Session Control:**
   - Create a function to stop the session and prevent further dose tracking.
   - Disable relevant buttons or provide an option to reset the session.

10. **Data Storage and Retrieval:**
   - Since you're not using Firebase, you can consider using local storage or browser cookies to store dose information, session data, and any other required data.
   - Implement functions to store and retrieve data from local storage or cookies.

11. **Testing and Debugging:**
   - Thoroughly test your web app to ensure all functionalities work as expected.
   - Debug any issues or unexpected behaviors you encounter during testing.

12. **Deployment:**
   - To deploy your web app, you can use a web server or hosting service of your choice.
   - Upload your HTML, CSS, and JavaScript files to the server/hosting platform.

Remember, without a backend service like Firebase, you won't have centralized data storage or real-time updates. The data will be stored locally on the user's browser. Keep in mind that local storage has limitations on the amount of data it can store (usually around 5 MB).

Additionally, consider incorporating code organization and modularity practices, such as using separate JavaScript functions for different functionalities, to make your code easier to maintain and enhance in the future.

I hope this helps you in creating your web app using HTML, CSS, and JavaScript! Let me know if you have any further questions.