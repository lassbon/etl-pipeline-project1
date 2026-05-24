import requests
import pandas as pd
import logging
from transfrom import transform_data
from extract import extract_data
from load import load_data

logging.basicConfig(
    filename="./logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s , %(name)s - %(levelname)s - %(message)s"
)

#Extract
data = extract_data()
if not data:
    logging.info("No data found ...")
    exit()
logging.info("Starting my ETL pipeline...")

#Transform
df = transform_data(data)

#Load
df = load_data(df)
logging.info("Saving Completed ...")
logging.info("ETL pipeline completed successfully ...")
