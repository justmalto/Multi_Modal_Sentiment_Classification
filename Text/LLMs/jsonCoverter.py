import csv
import json

# Define the input and output file paths
csv_file_path = r'C:\Users\omkar\OneDrive\Documents\Internship\SA\IMDB Dataset.csv\IMDB Dataset.csv'
json_file_path = r'C:\Users\omkar\OneDrive\Documents\Internship\SA\LLMs\Data.json'

# Initialize a list to store the rows
data = []

# Open the CSV file and read its contents
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

# Write the list to a JSON file
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)

print(f"CSV data has been successfully converted to {json_file_path}")
