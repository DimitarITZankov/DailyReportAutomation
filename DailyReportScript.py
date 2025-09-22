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
    level=logging.INFO
try:
    df = pd.read_csv("daily_sales.csv")
    logging.debug("Opened the  csv file successfully")
except FileNotFoundError as e:
    logging.error("Unable to open the csv file",e)
    print("The file doesnt exist")
    quit()
logging.debug("Fetching the data for daily report")
calculate_kg_per_day = df.groupby("Date")["Kg"].sum()
calculate_price_per_day = df.groupby("Date")["Price"].sum()
all_kg = df["Kg"].sum()
today = datetime.today().strftime("%Y-%m-%d")
calculate_kg_per_day.to_csv(f"DailyReport_{today}.csv")
logging.info("Daily report has been successfully generated")
logging.info(f"Searching for file...")
try:
    df = pd.read_csv(f"StorageLeft.csv")
    logging.debug("Opened the csv file successfully")
except FileNotFoundError as e:
    logging.error("Unable to open the csv file: %s",e)
    print("The file doesnt exist")
df["Main_Storage"] = df["Main_Storage"] - all_kg
df.to_csv(f"StorageLeft.csv",index=False)
logging.info("StorageLeft has been successfully refreshed with the new data")