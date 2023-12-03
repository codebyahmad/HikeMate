# a web scraping project by ahmad

# This script is designed to scrape trail ids from the https://www.alltrails.com based on a list of trail IDs
# provided in an Excel file. 

# Instructions:
# 1. Follow the instructions in headers.py
# 2. Ensure that the required libraries (requests, json, time, os, pandas, openpyxl) are installed.
# 3. Run the script to initiate the scraping process. Adjust the delay value if necessary to comply with API rate limits.

import os
import sys
import requests
import time
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

sys.path.append(os.path.abspath('..'))
from headers import headers # ../headers.py

# Base URL and API key for alltrails.com
base_url = "https://www.alltrails.com/api/alltrails/v2/trails/"
api_key = "3p0t5s6b5g4g0e8k3c1j3w7y5c3m4t8i"

# Create a session for making requests
session = requests.Session()

# Read trail IDs from Excel file using pandas
excel_file_path = "trail_ids.xlsx"
df = pd.read_excel(excel_file_path)

# Extract trail IDs as a list
trail_ids = df["trail_id"].tolist()

# List to store new trail IDs
new_trail_ids = set()

# Function to scrape trail ids
def trail_ids_grabber(trail_id):
    try:
        # Construct the dynamic part of the URL for trail data
        dynamic_url = f"{trail_id}?key={api_key}"

        # Construct the complete URL for trail data
        url = base_url + dynamic_url

        # Send a GET request to the URL with headers for trail data
        response = session.get(url, headers=headers)

        # Check if the request was successful (status code 200) for trail data
        if response.status_code == 200:
            # Parse the JSON data for trail data
            trail_data = response.json()

            # Extract trailIds from defaultPhoto and add them to the set
            default_photo = trail_data.get("trails", [])[0].get("defaultPhoto", {})
            trail_ids_in_photo = default_photo.get("trailIds", [])

            new_trail_ids.update(trail_ids_in_photo)

            # Introduce a delay between requests for trail data (you can adjust this value)
            time.sleep(10)

        else:
            print(f"\nFailed to retrieve data for trail ID {trail_id}. Status code: {response.status_code}")

        # Update the progress bar
        pbar.update(1)

    except Exception as e:
        print(f"\nAn error occurred for trail ID {trail_id}: {e}")
        # Update the progress bar in case of an error
        pbar.update(1)

# Create a progress bar with the total number of trails
total_trails = len(trail_ids)
with tqdm(total=total_trails, desc="Scraping Trail Ids") as pbar:
    try:
        # Use ThreadPoolExecutor to parallelize the requests
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(trail_ids_grabber, trail_ids)

        # Create a DataFrame with trail IDs
        unique_df = pd.DataFrame({"trail_id": list(new_trail_ids)})

        # Write the DataFrame to a new Excel file
        new_excel_file = "trail_ids-new.xlsx"  # Replace with the desired file name
        unique_df.to_excel(new_excel_file, index=False)

        print(f"\nScraping done! Trail IDs saved to {new_excel_file}.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
