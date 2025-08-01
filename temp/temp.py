import csv

with open("dirty_data.csv", "w", newline = '') as file:
    file.write("""Name,Age,City
        Hemanth , 28 , Hyderabad 
        Priya,, Chennai
        John, 25, New York
        , 30, Delhi
        Raj , Forty , Mumbai""")



cleaned_rows = []        

with open("dirty_data.csv","r") as infile:
    reader = csv.reader(infile)
    header = next(reader)
    for row in reader:
        if not row or len(row) < 3 or any(col.strip() == '' for col in row):
            continue
            
        cleaned = [col.strip().title() for col in row]
        cleaned_rows.append(cleaned)
        
with open("cleaned_data.csv","w", newline = '') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Name", "Age", "City"])
    writer.writerows(cleaned_rows)
    
    
