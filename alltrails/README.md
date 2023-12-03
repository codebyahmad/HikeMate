# AllTrails Web Scraping Project

## Overview

This GitHub repository contains a comprehensive web scraping project for collecting trail data and photos from [AllTrails](https://www.alltrails.com). The project is designed to scrape trail information based on a list of trail IDs provided in an Excel file. The scraped data is then stored in JSON format in a designated output folder, and trail photos are saved in a separate folder.

## Project Structure

### 1. Scripts

- **alltrails.py:** Scrapes trail data and photos based on the provided trail IDs.
- **csv_generator.py:** Converts JSON files containing trail data into a CSV file.
- **headers.py:** Provides necessary headers and cookie values for web scraping AllTrails data.
- **main.py:** Automates the execution of the three main scripts for a seamless workflow.
- **trail_ids_generator.py:** Collects trail IDs by merging XLSX files in the trail_ids_grabber folder.

### 2. Instructions

- **headers.py:** Contains instructions on how to obtain and update necessary cookie values for authentication and consent.
- **README.md:** Detailed instructions for running the entire scraping project, including manual steps and automation.

### 3. Data Handling

- **trail_ids_grabber:** Folder for collecting trail IDs manually using the `trail_ids_generator.py` script.
- **alltrails:** Folder for storing scraped JSON files and trail photos.
- **trail_ids.xlsx:** Excel file containing unique trail IDs.

## Instructions for Usage

### Initial Setup

1. Clone the repository to your local machine.
2. Install the required libraries: `requests`, `json`, `time`, `os`, `pandas`, `openpyxl`.
   ```bash
   pip install requests json time os pandas openpyxl
   ```

### Web Scraping Process

1. **Collect Trail IDs:**

- Navigate to the **trail_ids_grabber** folder.
- Execute the **trail_ids_grabber.py** script multiple times to gather a satisfactory number of trail IDs.
  ```bash
  python trail_ids_grabber.py
  ```
- **NOTE:** Due to certain technical restrictions, the complete process cannot be fully automated in one go. You must rename old **`trail_ids.xlsx`** as `trail_ids-*.xlsx` and rename newly generated **`trail_ids-new.xlsx`** as `trail_ids.xlsx`. You must perform these action after each iteration.

2. **Scrape Trail Data:**

- Run the **main.py** script to automate the entire process or execute each script individually:
  ```bash
  python main.py
  ```
- Follow the prompts to generate trail IDs, start scraping, and generate a CSV file

3. **Check Results:**

- The scraped trail data is stored in the **`alltrails`** folder, and trail photos are saved in the **`alltrails/images`** subfolder.
- The CSV file with extracted trail information is saved as **`alltrails-data.csv`**.

## Important Notes

- Update cookie values in **`headers.py`** by following the instructions provided.
- Make sure to adjust delay values in the scripts to comply with API rate limits.

## Folder Structure

```
├── AllTrails
|     |
|     └── trail_ids_grabber
|           |
|           ├── trail_ids_grabber.py
|           └── trail_ids.xlsx
|
├── alltrails
|
├── header.py
├── trail_ids_generator.py
├── alltrails.py
├── csv_generator.py
├── main.py
|
└── README.md
```

## Contributions

Contributions to improve and enhance this project are welcome. If you encounter any issues or have suggestions, please create an issue or submit a pull request.

Happy scraping! Skadoosh! 🚀
