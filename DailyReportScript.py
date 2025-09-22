import os
import csv
import pandas as pd
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
try:
    df = pd.read_csv("daily_sales.csv")
    logging.debug("Opened the  csv file successfully")
except FileNotFoundError as e:
    logging.error("Unable to open the csv file",e)
    print("The file doesnt exist")
