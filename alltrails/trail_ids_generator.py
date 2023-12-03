# a web scraping project by ahmad

# This script reads all XLSX files in a specified folder, concatenates their data into a single DataFrame, removes
# duplicate IDs, and saves the unique IDs to a new Excel file.

# Usage:
# 1. Place all XLSX files containing ID data in the 'trail_ids_grabber' folder.
# 2. Run this script to merge the files, remove duplicate IDs, and save the result.

import os
import pandas as pd
from tqdm import tqdm

def trail_ids_generator(folder_path, output_file="trail_ids.xlsx"):
    # Get the absolute path of the current script
    script_path = os.path.dirname(os.path.abspath(__file__))

    # Get a list of all XLSX files in the specified folder
    file_list = [file for file in os.listdir(folder_path) if file.endswith(".xlsx")]

    if not file_list:
        print("\nNo XLSX files found in the specified folder.")
        return

    # Initialize an empty DataFrame to store the concatenated data
    combined_data = pd.DataFrame()

    # Use tqdm to add a progress bar
    for file_name in tqdm(file_list, desc="Processing files", unit="file"):
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_excel(file_path)
        combined_data = pd.concat([combined_data, df], ignore_index=True)

    # Remove duplicate IDs
    combined_data.drop_duplicates(subset="trail_id", inplace=True)

    # Sort the unique IDs
    combined_data.sort_values(by="trail_id", inplace=True)

    # Save the combined data to a new Excel file in the same folder as the script
    output_path = os.path.join(script_path, output_file)
    combined_data.to_excel(output_path, index=False)

    print(f"\nMerged and unique IDs saved to {output_path}.")

# Replace 'trail_ids_grabber' with the actual folder path
folder_path = "trail_ids_grabber"

trail_ids_generator(folder_path)
