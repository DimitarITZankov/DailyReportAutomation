# DailyReportAutomation
In this project I am automating the daily reports for my father's company
Libraries used in the project:
-csv - reading the csv files
-pandas - clearing the data
-logging - informative messages about the script as logs
-datetime - using the todays date to create daily report file with the date in the name
The script works by taking the daily sales, summing all the amount sold in the day and price, then saving them into variable.Next we open the file with the storage left and subtract from it.
This is my first project in GitHub and also first time using it :).
How this script is working ?
1. You write your sales in the 'daily_sales.csv'
2. Then you start the script and it automatically :
Generates logs in the .log file
Subtract the sold amount from the main storage file
Makes a 'daily_report.csv' file with Columns: Date,Amount,Price
