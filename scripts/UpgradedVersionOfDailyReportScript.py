import os
import csv
import logging
import pandas as pd
from datetime import datetime

data_folder= "../data"
logs_folder = "../logs"
reports_folder = "../reports"

os.makedirs(logs_folder, exist_ok=True)
logging.basicConfig(filename=os.path.join(logs_folder, "daily_report.log"),
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

def generate_daily_reports(df_sales):
    report = df_sales.groupby(["Date"]).agg({
        "Kg" : "sum",
        "Price" : "sum"
    }).reset_index()
    total_kg = df_sales["Kg"].sum()
    return report, total_kg

def save_csv(df,folder,filename):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    df.to_csv(path, index=False)
    logging.info(f"Saved the csv file successfully {path}")
    return path

def update_storage(df_storage,total_kg):
    df_storage["Main_Storage"] = df_storage["Main_Storage"] - total_kg
    return df_storage

def main():
    logging.info("Opening the csv file")
    sales_file = os.path.join(data_folder, "daily_sales.csv")
    sales_df = open_csv(sales_file)

    daily_report, total_kg = generate_daily_reports(sales_df)
    today = datetime.today().strftime("%Y-%m-%d")
    save_csv(daily_report,reports_folder,f"daily_report.{today}.csv")
    logging.info("Successfully generated daily report")

    storage_file = os.path.join(data_folder, "StorageLeft.csv")
    df_storage = open_csv(storage_file)
    df_storage = update_storage(df_storage,total_kg)
    save_csv(df_storage,data_folder,f"StorageLeft.csv")
    logging.info("StorageLeft has been successfully refreshed with the new data")

if __name__ == "__main__":
    main()

