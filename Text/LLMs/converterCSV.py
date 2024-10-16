import json
import csv

# File paths
json_file_path = r'C:\Users\omkar\OneDrive\Documents\Internship\SA\LLMs\data (6).json'
csv_file_path = r'C:\Users\omkar\OneDrive\Documents\Internship\SA\LLMs\data1.csv'

# Read the JSON data
with open(json_file_path, mode='r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Write to the CSV file
with open(csv_file_path, mode='w', encoding='utf-8', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the header
    header = data[0].keys()
    csv_writer.writerow(header)
    
    # Write the data rows
    for row in data:
        csv_writer.writerow(row.values())

print(f"JSON data has been successfully converted to {csv_file_path}")
