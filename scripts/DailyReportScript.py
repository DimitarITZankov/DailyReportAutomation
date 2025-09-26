import os
import csv
import pandas as pd
import logging
from datetime import datetime

data_folder = "../data"
reports_folder = "../reports"
logs_folder = "../logs"

os.makedirs(logs_folder, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(logs_folder, "daily_report.log"),
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO)
try:
    sales_df = pd.read_csv(os.path.join(data_folder, "daily_sales.csv"))
    logging.info("Opened the  csv file successfully")
except FileNotFoundError as e:
    logging.error("Unable to open the csv file: %s",e)
    print("The file doesnt exist")
    quit()
logging.info("Fetching the data for daily report")
daily_report = sales_df.groupby("Date").agg({
    "Kg": "sum",
    "Price": "sum"
}).reset_index()
all_kg = sales_df["Kg"].sum()
today = datetime.today().strftime("%Y-%m-%d")
daily_report.to_csv(os.path.join(reports_folder, f"DailyReport_{today}.csv"), index=False)
logging.info("Daily report has been successfully generated")
logging.info(f"Searching for file...")
try:
    storage_df = pd.read_csv(os.path.join(data_folder, "StorageLeft.csv"))
    logging.info("Opened the csv file successfully")
except FileNotFoundError as e:
    logging.error("Unable to open the csv file: %s",e)
    print("The file doesnt exist")
    quit()
storage_df["Main_Storage"] = storage_df["Main_Storage"] - all_kg
storage_df.to_csv(os.path.join(data_folder, "StorageLeft.csv"), index=False)
logging.info("StorageLeft has been successfully refreshed with the new data")