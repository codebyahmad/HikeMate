# a web scraping project by ahmad

# This script automates a multi-step workflow involving the execution of three Python scripts:
# 1. trail_ids_generator.py - Generates an Excel file containing unique trail IDs.
# 2. alltrails.py - Performs scraping based on the generated unique trail IDs.
# 3. csv_generator.py - Generates a CSV file for the scraped trails.

# Due to certain technical restrictions, the complete process cannot be fully automated in one go.

# To ensure a sufficient amount of data, please follow the manual steps below before executing this script.
# 1. Navigate to the 'trail_ids_grabber' folder and execute 'trail_ids_grabber.py' multiple times 
#    until you have gathered a satisfactory number of trail IDs.
# 2. Once you have collected a good amount of trail IDs, you can now proceed to execute this script 
#    python main.py

import subprocess

def execute_script(script_name):
    try:
        subprocess.run(['python', script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"\nError executing {script_name}: {e}")
        exit()

def main():
    # Step 1: Execute trail_ids_generator.py
    generate_ids = input("\nDo you want to generate Trail IDs? (Press 'y' or 'Y' to generate): ")
    if generate_ids.lower() == 'y':
        execute_script('trail_ids_generator.py')

    # Step 2: Execute alltrails.py
    start_scraping = input("\nDo you want to start scraping? (Press 'y' or 'Y' to start): ")
    if start_scraping.lower() == 'y':
        execute_script('alltrails.py')

    # Step 3: Execute csv_generator.py
    generate_csv = input("\nDo you want to generate a CSV for scraped trails? (Press 'y' or 'Y' to generate): ")
    if generate_csv.lower() == 'y':
        execute_script('csv_generator.py')

if __name__ == "__main__":
    main()
