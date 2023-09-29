import csv

# Specify the CSV file path
csv_file_path = "nested_columns.csv"

# Define your data with nested columns
nested_columns_data = [
    {"group": "Group1", "details": {"type": "Type1", "date": "Date1"}},
    {"group": "Group2", "details": {"type": "Type2", "date": "Date2"}},
    # Add more data as needed
]

# Create a flattened data list
flattened_data = []

for item in nested_columns_data:
    row = {
        "group": item["group"],
        "details.type": item["details"]["type"],
        "details.date": item["details"]["date"]
    }
    flattened_data.append(row)

# Open the CSV file for writing
with open(csv_file_path, "w", newline="") as csvfile:
    columns = ["group", "details.type", "details.date"]

    # Create a DictWriter to handle writing data
    writer = csv.DictWriter(csvfile, fieldnames=columns)

    # Write the header row
    writer.writeheader()

    # Write the data rows
    for row in flattened_data:
        writer.writerow(row)
