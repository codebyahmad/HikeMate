# Trail Data CSV Generator

## Overview

This Python script automates the extraction of information about hiking trails from JSON files scraped from `https://wegwandern.ch/`. The website's content, including details about trails, regions, difficulty levels, seasons, route types, activities, offers, and themes, is accessible through the WordPress JSON API at `https://wegwandern.ch/wp-json/wp/v2/`. The script compiles this information into a CSV file for further analysis.

## Usage

1. Run the script by executing:

   ```python
   python main.py
   ```

2. Check the generated CSV file:

   The script creates a CSV file named `wegwandern-data.csv` in the same directory.

## Configuration

- Adjust the CSV field names in the script to include additional fields if needed.

## Additional Information

- The script extracts data directly from the provided JSON files and does not perform live scraping from the website's API.
- The website is built using WordPress, and the script automates the process of transforming the available JSON data into a CSV format.
- Refer to the WordPress JSON API documentation at [https://developer.wordpress.org/rest-api/](https://developer.wordpress.org/rest-api/) for any updates or changes in the API structure.

## Acknowledgments

- [OpenAI](https://www.openai.com/) - For providing language models that assist in code generation.
- [WordPress](https://wordpress.org/) - For the WordPress JSON API used in data extraction.

Feel free to contribute or raise issues if you encounter any problems.
