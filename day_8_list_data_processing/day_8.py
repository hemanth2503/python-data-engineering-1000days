'''
List are the most used data structure in python
You'll deal with datasets, logs, API responses, and CSV rows - all often in the form of lists.
Create                      - [], indexing, slicing, and methods
Looping through this        - for, enumerate()
Common operations           - append, insert, remove, pop, sort, reverse
list comprehensions         - Pythonic way to filter and transform lists
Real-world tasks            - Data cleaning, transformation, and analysis
'''

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(cities[0])    # Accessing the first element
print(cities[-1])   # Accessing the last element
print(len(cities))  # Length of the list  

# loop through the list
for city in cities:
    print("City:", city)

for i, city in enumerate(cities):
    print(f"{i+1}. {city}")

# enumerate(cities) is a special function in Python: It returns both the index (i) and the value (city) of each element, Indexing starts at 0 by default
# f"..." is an f-string, which allows you to insert variables directly inside {}.
# {i+1} → Since Python indexes start at 0, we add +1 to make it more human-friendly (1-based numbering), {city} → inserts the name of the city.  

for i, city in enumerate(cities, start=1):
    print(f"{i}. {city}")
# The start=1 argument makes the enumeration start at 1 instead of the default 0.

# Common operations
cities.append('San Diego')  # Add a new city to the end
cities.insert(2, 'San Francisco')  # Insert a city at index 2
cities.remove('Houston')  # Remove a city by name
removed_city = cities.pop()  # Remove and return the last city
print("Removed city:", removed_city)  # Display the removed city
cities.sort()  # Sort the list alphabetically
print(cities)

# list comprehension example
nums = [1, 2, 3, 4, 5]
squared = [x**2 for x in nums]
print(squared)

even_squared = [x**2 for x in nums if x % 2 == 0]
print(even_squared)


#Practice Task 1
raw_values = [" 100", "200 ", "abc", "", "300", "N/A", "500 "]

'''
Remove empty or invalid values ("", "abc", "N/A") 
Strip whitespace
Convert to integers
'''
# Method 1: Using a Loop
cleaned_values = []
for value in raw_values:
    stripped_value = value.strip()
    if stripped_value.isdigit():
        cleaned_values.append(int(stripped_value))
print(cleaned_values)  # Output: [100, 200, 300, 500]

# Method 2: Using List Comprehension
def clean_values(raw_values):
    return [int(x.strip()) for x in raw_values if x.strip().isdigit()]
# Example usage
cleaned_values = clean_values(raw_values) 
print(cleaned_values)  # Output: [100, 200, 300, 500]



# Practice Task 2: Multiply Each Item by 10
input_list = [1, 5, 10]
output_list = [x*10 for x in input_list]
print(output_list)

# Real-World Mini Project: Log Cleaner
logs = [
    "ERROR: Disk full",
    "INFO: Backup complete",
    "WARNING: Low memory",
    "ERROR: CPU overheating",
    "INFO: Update installed"
]

'''
Tasks:
Filter only lines starting with "ERROR"
Count how many errors occurred
'''

# Filter only lines starting with "ERROR"
error_logs = [x for x in logs if x.startswith("ERROR")]
print("Filtered Error Logs:", error_logs)
print("Number of Errors:", len(error_logs))


#Tip of the Day: What is the difference between list and tuple? 
# A list is mutable, meaning you can change its content (add, remove, or modify elements).
# A tuple is immutable, meaning once it is created, its content cannot be changed.



