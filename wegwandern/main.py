# a web scraping project by ahmad

# CSV Generator for Trail Data from https://wegwandern.ch/

# This script extracts information about hiking trails from a set of JSON files,
# including details about the trail, region, difficulty, seasons, route type, activities,
# offers, and themes. It then compiles the extracted data into a CSV file for further analysis.

# The JSON files include:
# - wanderung.json: Trail information
# - wanderregionen.json: Region information
# - anforderung.json: Difficulty levels
# - wander-saison.json: Seasons suitable for hiking
# - routenverlauf.json: Route types
# - aktivitat.json: Activities related to trails
# - angebot.json: Offers related to trails
# - thema.json: Themes associated with trails

# The CSV file includes the following fields for each trail:
# - trail_id, name, city, region_name, length_km, ascent, descent,
# - deepest_point, highest_point, unit, duration_minutes, difficulty,
# - season, route_type, aktivitat, angebot, thema

# Ensure that the JSON files are present in the specified 'json-data' folder before running the script.
# The generated CSV file ('wegwandern-data.csv') will be created in the same directory as the script.

import os
import json
import csv
import re

# Function to extract information using regex
def extract_info(content, regex_pattern):
    match = re.search(regex_pattern, content)
    return match.group(1) if match else None

# Functions to extract specific trail information
def extract_distanz(content):
    return extract_info(content, r'Distanz<\/p><p>([\d.]+)\s*km')

def extract_aufstieg(content):
    return extract_info(content, r'Aufstieg<\/p><p>([\d.]+)\s*m')

def extract_abstieg(content):
    return extract_info(content, r'Abstieg<\/p><p>([\d.]+)\s*m')

def extract_tiefster_punkt(content):
    return extract_info(content, r'Tiefster Punkt<\/p><p>([\d.]+)\s*m')

def extract_hochster_punkt(content):
    return extract_info(content, r'H\u00f6chster Punkt<\/p><p>([\d.]+)\s*m')

def extract_dauer(content):
    dauer_match = re.search(r'Dauer<\/p><p>(?:(\d+):)?(\d+)\s*h', content)
    hours, minutes = map(int, dauer_match.groups()) if dauer_match else (0, 0)
    return hours * 60 + minutes

# Function to read JSON data from a file
def read_json_file(json_path):
    with open(json_path, 'r') as json_file:
        return json.load(json_file)

# Function to find an entry in data based on ID
def find_entry_by_id(data, entry_id):
    return next((entry for entry in data if entry.get("id") == entry_id), None)

# Function to extract information from a list of IDs
def extract_info_list(trail, data, key):
    id_list = sorted(trail.get(key, []))
    info_list = []

    for entry_id in id_list:
        entry = find_entry_by_id(data, entry_id)
        entry_name = entry.get("name", "") if entry else ""
        info_list.append(entry_name)

    return info_list

# Main function to generate CSV
def csv_generator(json_folder, csv_filename):
    # JSON file names
    json_files = [
        'wanderung.json', 'wanderregionen.json', 'anforderung.json',
        'wander-saison.json', 'routenverlauf.json', 'aktivitat.json',
        'angebot.json', 'thema.json'
    ]

    # Check if all JSON files exist
    for json_file in json_files:
        json_path = os.path.join(json_folder, json_file)
        if not os.path.exists(json_path):
            print(f"\nFile '{json_file}' not found in '{json_folder}'.")
            return

    # Create a list to store the extracted trail data
    trail_data_list = []

    # Read JSON data for each file
    thema_data = read_json_file(os.path.join(json_folder, 'thema.json'))
    angebot_data = read_json_file(os.path.join(json_folder, 'angebot.json'))
    aktivitat_data = read_json_file(os.path.join(json_folder, 'aktivitat.json'))
    routenverlauf_data = read_json_file(os.path.join(json_folder, 'routenverlauf.json'))
    wander_saison_data = read_json_file(os.path.join(json_folder, 'wander-saison.json'))
    anforderung_data = read_json_file(os.path.join(json_folder, 'anforderung.json'))
    wanderregionen_data = read_json_file(os.path.join(json_folder, 'wanderregionen.json'))
    wanderung_data = read_json_file(os.path.join(json_folder, 'wanderung.json'))

    # Iterate over each trail in wanderung_data
    for trail in wanderung_data:
        # Extract basic trail information
        trail_id = trail.get("id", "")
        name = trail.get("title", {}).get("rendered", "")
        region_id = trail.get("wanderregionen", [])[0]

        # Find matching entry in wanderregionen_data
        region_entry = find_entry_by_id(wanderregionen_data, region_id)
        city_id = region_entry.get("parent")

        # Extract region_name and city
        if city_id != 0:
            region_name = region_entry.get("name", "") if region_entry else ""
            city_entry = find_entry_by_id(wanderregionen_data, city_id)
            city = city_entry.get("name", "") if city_entry else ""
        else:
            city = region_entry.get("name", "") if region_entry else ""
            region_name = ""

        # Extract anforderung_id from "anforderung" list
        anforderung_list = trail.get("anforderung", [])
        anforderung_id = anforderung_list[0] if anforderung_list else None
        anforderung_entry = find_entry_by_id(anforderung_data, anforderung_id) # Find matching entry in anforderung_data
        anforderung_name = anforderung_entry.get("name", "") if anforderung_entry else ""

        # Check if routenverlauf list is not empty before accessing its elements
        routenverlauf_list = trail.get("routenverlauf", [])
        routenverlauf_id = routenverlauf_list[0] if routenverlauf_list else None
        routenverlauf_entry = find_entry_by_id(routenverlauf_data, routenverlauf_id) # Find matching entry in routenverlauf_data
        routenverlauf_name = routenverlauf_entry.get("name", "") if routenverlauf_entry else ""

        # Extract wander-saison, aktivitat, angebot, thema information
        wander_saison_info_list = extract_info_list(trail, wander_saison_data, "wander-saison")
        aktivitat_info_list = extract_info_list(trail, aktivitat_data, "aktivitat")
        angebot_info_list = extract_info_list(trail, angebot_data, "angebot")
        thema_info_list = extract_info_list(trail, thema_data, "thema")

        # Extract additional trail information
        distanz = extract_distanz(trail.get("content", {}).get("rendered", ""))
        aufstieg = extract_aufstieg(trail.get("content", {}).get("rendered", ""))
        abstieg = extract_abstieg(trail.get("content", {}).get("rendered", ""))
        tiefster_punkt = extract_tiefster_punkt(trail.get("content", {}).get("rendered", ""))
        hochster_punkt = extract_hochster_punkt(trail.get("content", {}).get("rendered", ""))
        dauer = extract_dauer(trail.get("content", {}).get("rendered", ""))

        # Append trail data to the list
        trail_data_list.append({
            "trail_id": trail_id,
            "name": name,
            "city": city,
            "region_name": region_name,
            "length_km": distanz,
            "ascent": aufstieg,
            "descent": abstieg,
            "deepest_point": tiefster_punkt,
            "highest_point": hochster_punkt,
            "unit": "m",
            "duration_minutes": dauer,
            "difficulty": anforderung_name,
            "season": wander_saison_info_list,
            "route_type": routenverlauf_name,
            "aktivitat": aktivitat_info_list,
            "angebot": angebot_info_list,
            "thema": thema_info_list,
            # Add more fields as needed
        })

    # Check if any trail data is extracted
    if not trail_data_list:
        print(f"\nNo trail data found in 'wanderung.json'.")
        return

    # Get the script's directory
    script_directory = os.path.dirname(os.path.realpath(__file__))

    # Write trail data to CSV in the script's directory
    csv_path = os.path.join(script_directory, csv_filename)
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = [
            "trail_id", "name", "city", "region_name", "length_km", "ascent", "descent",
            "deepest_point", "highest_point", "unit", "duration_minutes", "difficulty",
            "season", "route_type", "aktivitat", "angebot", "thema"
            # Add more fields as needed
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write trail data
        for trail_data in trail_data_list:
            writer.writerow(trail_data)

    print(f"CSV file '{csv_filename}' created in '{script_directory}'.")

# Change variable names as desired
json_folder = 'json-data'
csv_filename = 'wegwandern-data.csv'
csv_generator(json_folder, csv_filename)
