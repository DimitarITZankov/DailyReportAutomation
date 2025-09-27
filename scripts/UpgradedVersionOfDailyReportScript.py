import os
import csv
import logging
import pandas as pd
from datetime import datetime

data_folder= "../data"
logs_folder = "../logs"
reports_folder = "../reports"

os.makedirs(logs_folder, exist_ok=True)
logging.basicConfig(filename=os.path.join(logs_folder, "upgrade_daily_report.log"),
                    format='%(asctime)s %(levelname)s %(message)s',level=logging.INFO)

def open_csv(csv_file):
    try:
        df_sales = pd.read_csv(csv_file)
        logging.info("Opened the csv file successfully")
        return df_sales
    except FileNotFoundError as e:
        logging.error(e)
        print("File not found")
        quit()

