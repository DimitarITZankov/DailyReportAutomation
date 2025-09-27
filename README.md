# DailyReportAutomation
In this project I am automating the daily reports for my father's company
Libraries used in the project:
-csv - reading the csv files
-pandas - clearing the data
-logging - informative messages about the script as logs
-datetime - using the todays date to create daily report file with the date in the name
This is my first project in GitHub and also first time using it :).
How to use the script?:
1. Prepare your sales in a file namedd 'daily_sales.csv'. The file should include columns like Date,Kg(amount sold),Price
2. In the 'StorageLeft.csv' write the current stock available in your main storage
3. When you run the script , it automatically generates a 'daily_report.log' file which tracks all actions of the script
4. The script subtracts the sold amount from the main storage and updates 'StorageLeft.csv'
5. New CSV daily report file named 'DailyReport_<YYYY-MM-DD>.csv' created and saved in the folder reports:
  Date - The date of sales
  Kg - Total amount sold that day
  Price - Total revenue for the day
