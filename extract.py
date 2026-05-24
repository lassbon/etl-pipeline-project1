import logging
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def extract_data():
    # Extract
    logging.info("Fetching data from API...")
    url = os.getenv("API_URL")
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
