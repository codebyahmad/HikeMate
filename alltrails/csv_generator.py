# a web scraping project by Ahmad

# This script takes JSON files containing trail data, extracts relevant information, and generates a CSV file.

# Usage Instructions:
# 1. Ensure the 'alltrails' folder, containing JSON files with trail data, exists.
# 2. Specify the 'json_folder' variable with the path to the folder containing JSON files.
# 3. Specify the 'csv_filename' variable with the desired name for the CSV output file.
# 4. Run the script to convert JSON data to CSV.

# Note:
# - The script looks for JSON files in the specified folder and extracts key trail details.
# - Additional fields can be included in the 'fieldnames' list as needed.
# - The resulting CSV file is created in the same folder as the JSON files.

import os
import json
import csv

def csv_generator(json_folder, csv_filename):
    # Check if the folder exists
    if not os.path.exists(json_folder):
        print(f"\nFolder '{json_folder}' not found.")
        return

    # List all files in the folder
    json_files = [f for f in os.listdir(json_folder) if f.endswith('.json')]

    # Check if there are any JSON files
    if not json_files:
        print(f"\nNo JSON files found in '{json_folder}'.")
        return

    # Create a list to store the extracted trail data
    trail_data_list = []

    # Loop through each JSON file
    for json_file in json_files:
        json_path = os.path.join(json_folder, json_file)

        # Read JSON data
        with open(json_path, 'r', encoding='utf-8-sig') as file:
            json_data = json.load(file)

            # Check if the expected fields exist
            if "trails" in json_data and json_data["trails"]:
                trail = json_data["trails"][0]

                # Helper function to safely extract values or return an empty string
                def safe_get(data, key):
                    return data[key] if key in data else ''

                # Check if the country is Switzerland
                country = safe_get(trail["location"], "country").lower()
                if country not in ["ch"]:
                    continue  # Skip trails that are not in Switzerland

                # Extract duration from defaultActivityStats if duration_minutes is not available
                duration_minutes = safe_get(trail["trailGeoStats"], "durationMinutes")
                if not duration_minutes:
                    duration = safe_get(trail["defaultActivityStats"], "duration")
                    duration_minutes = duration / 3600 if duration else ''

                trail_data_list.append({
                    "trail_id": safe_get(trail, "id"),
                    "name": safe_get(trail, "name"),
                    "city": safe_get(trail["location"], "city"),
                    "region_name": safe_get(trail["location"], "regionName"),
                    "country_name": safe_get(trail["location"], "country_name"),
                    "_geoloc": {'lat': safe_get(trail["location"], "latitude"), 'lng': safe_get(trail["location"], "longitude")},
                    "popularity": safe_get(trail, "popularity"),
                    "length": safe_get(trail["trailGeoStats"], "length"),
                    "elevation_start": safe_get(trail["trailGeoStats"], "elevationStart"),
                    "elevation_gain": safe_get(trail["trailGeoStats"], "elevationGain"),
                    "elevation_max": safe_get(trail["trailGeoStats"], "elevationMax"),
                    "unit": "m",
                    "duration_minutes": duration_minutes,
                    "avg_rating": safe_get(trail, "avgRating"),
                    "difficulty": safe_get(trail["defaultActivityStats"], "difficulty"),
                    "visitor_usage": safe_get(trail["defaultActivityStats"], "visitorUsage"),
                    "season": {'start': safe_get(trail["defaultActivityStats"], "seasonStart"), 'end': safe_get(trail["defaultActivityStats"], "seasonEnd")},
                    "route_type": safe_get(trail, "routeType"),
                    "review_count": safe_get(trail["trailCounts"], "reviewCount"),
                    "photo_count": safe_get(trail["trailCounts"], "photoCount"),
                    "track_count": safe_get(trail["trailCounts"], "trackCount"),
                    "completed_count": safe_get(trail["trailCounts"], "completedCount"),
                    "activities": [activity["uid"] for activity in safe_get(trail["attributes"], "activities")],
                    "features": [feature["uid"] for feature in safe_get(trail["attributes"], "features")],
                    "obstacles": [obstacle["uid"] for obstacle in safe_get(trail["attributes"], "obstacles")],
                    "slug": safe_get(trail, "slug"),
                    "overview": safe_get(trail, "overview")
                    # Add more fields as needed
                })
            else:
                print(f"\nExpected data not found in file '{json_file}'. Skipping.")

    # Check if any trail data is extracted
    if not trail_data_list:
        print(f"\nNo trail data found in JSON files.")
        return

    # Write trail data to CSV
    csv_path = os.path.join(json_folder, csv_filename)
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ["trail_id", "name", "city", "region_name", "country_name", "_geoloc", "popularity", "length", "elevation_start", "elevation_gain", "elevation_max", "unit", "duration_minutes", "avg_rating", "difficulty", "visitor_usage", "season", "route_type", "review_count", "photo_count", "track_count", "completed_count", "activities", "features", "obstacles", "slug", "overview"]
        # Add more field names as needed

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header
        writer.writeheader()

        # Write trail data
        for trail_data in trail_data_list:
            writer.writerow(trail_data)

    print(f"CSV file '{csv_filename}' created in '{json_folder}'.")
    print("My time has come... You must continue your journey without me!")

# Change variable names as desired
json_folder = 'alltrails'
csv_filename = 'alltrails-data.csv'
csv_generator(json_folder, csv_filename)