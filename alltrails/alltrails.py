# a web scraping project by ahmad

# This script is designed to scrape trails data and photos from the https://www.alltrails.com based on a list of 
# trail IDs provided in an Excel file. The scraped data is then saved in JSON format in a designated output folder,
# and trail photos are saved in a separate folder.

# Instructions:
# 1. Follow the instructions in headers.py
# 2. Ensure that the required libraries (requests, json, time, os, pandas, openpyxl) are installed.
# 3. Run the script to initiate the scraping process. Adjust the delay value if necessary to comply with API rate limits.
# 4. The scraped trail data will be stored in the "alltrails" folder, and trail photos will be saved in the 
#    "alltrails/images" subfolder.

import requests
import json
import time
import os
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from headers import headers

print("Let's scrape and chill. May the code be ever in your favor! :) Skadoosh! ")

# Base URL and API key for trail data and photos
base_url = "https://www.alltrails.com/api/alltrails/v2/trails/"
api_key = "3p0t5s6b5g4g0e8k3c1j3w7y5c3m4t8i"

# Create a session for making requests
session = requests.Session()

# Read trail IDs from Excel file using pandas
excel_file_path = "trail_ids.xlsx"
df = pd.read_excel(excel_file_path)

# Extract trail IDs as a list
trail_ids = df["trail_id"].tolist()

# Create a folder for the scraped data
output_folder = "alltrails"
os.makedirs(output_folder, exist_ok=True)

# Create a folder for the images
image_folder = os.path.join(output_folder, "images")
os.makedirs(image_folder, exist_ok=True)

# Function to scrape a trail
def scrape_trail(trail_id):
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

            # Save the JSON data to a file in the output folder based on the trail ID for trail data
            filename = os.path.join(output_folder, f"trail_{trail_id}.json")
            with open(filename, 'w') as file:
                json.dump(trail_data, file, indent=2)

            # Introduce a delay between requests for trail data (you can adjust this value)
            time.sleep(10)
        else:
            print(f"\nFailed to retrieve data for trail ID {trail_id}. Status code: {response.status_code}")

        # Construct the complete URL for trail photos
        photo_url = f"{base_url}{trail_id}/photos/0?size=larger_wide&key={api_key}"

        # Send a GET request to the URL for trail photos
        trail_photo = session.get(photo_url, headers=headers)

        # Check if the request was successful (status code 200) for trail photos
        if trail_photo.status_code == 200:
            # Save the image to a file in the images folder based on the trail ID for trail photos
            image_filename = os.path.join(image_folder, f"{trail_id}.webp")
            with open(image_filename, 'wb') as image_file:
                image_file.write(trail_photo.content)

            # Introduce a delay between requests for trail photos (you can adjust this value)
            time.sleep(10)
        else:
            print(f"\nFailed to retrieve photo for trail ID {trail_id}. Status code: {trail_photo.status_code}")

        # Return trail_id to update the progress bar
        return trail_id

    except Exception as e:
        print(f"\nAn error occurred for trail ID {trail_id}: {e}")
        return None

# Wrap the progress bar around the ThreadPoolExecutor
try:
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Use tqdm to create a progress bar
        for _ in tqdm(executor.map(scrape_trail, trail_ids), total=len(trail_ids), desc="Scraping Trails"):
            pass

except Exception as e:
    print(f"\nAn error occurred: {e}")
