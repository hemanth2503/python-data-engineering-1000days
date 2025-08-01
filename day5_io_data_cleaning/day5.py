import csv

'''Reading CSV (line-by-line):'''
with open("raw_data.csv", "r") as file:
    for line in file:
        print(line.strip())

'''Write Clean Data'''        
with open("cleaned_data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"]) # Header
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])
    writer.writerow(["Charlie", 35, "Chicago"])


'''Basic Cleaning Techniques'''    
cleaned_rows = []

with open("dirty_data.csv", newline='') as infile:
    reader = csv.reader(infile)
    for row in reader:
        # Skip empty rows
        if not row or len(row) < 3 or any(col.strip() == '' for col in row):
            continue
        # Strip spaces and normalize case
        cleaned = [col.strip().title() for col in row]
        cleaned_rows.append(cleaned)

# Write cleaned data
with open("cleaned_data.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(cleaned_rows)    