const readline = require("readline-sync");
//* npm install readline-sync
const moment = require("moment");
//* npm install moment

//? Ask user for input
while (true) {
  let userInput = readline.question(
    "Enter a specific date (YYYY-MM-DD) or press Enter for today's date: "
  );

  try {
    let daysRemaining = daysLeftInYear(userInput);

    // Output the result
    console.log(`There are ${daysRemaining} days left in the year.`);
    break;
  } catch (error) {
    console.log("Invalid date format. Please enter the date in YYYY-MM-DD format.");
  }
}

function daysLeftInYear(date) {
  let today;
  if (date) {
    today = moment(date, "YYYY-MM-DD");
  } else {
    today = moment();
  }

  let endOfYear = moment(today).endOf("year");
  let daysLeft = endOfYear.diff(today, "days");
  return daysLeft;
}