'''
Day 3: Working with Lists & Tuples
Why are Lists & Tuples Important in Data Engineering?
They are used to:
	Store collections of values (e.g. prices, IDs, rows from DB)
	Transform, clean, and process data in pipelines
	Pass structured data between functions
'''	

#✔️Creating a list

numbers = [10, 20, 30, 40, 50]

#✔️Accessing elements in a list
print(numbers[0])	# Output: 10
print(numbers[1])	# Output: 20

#✔️ Updating elements
numbers[4] = 100
print(numbers)	# Output: [10, 20, 30, 40, 100]
print(numbers[4])	# Output: 100

#✔️ Adding elements
numbers.append(60)
numbers.insert(4, 50)  # Insert 50 at index 4
print(numbers)	# Output: [10, 20, 30, 40, 100, 60]

# ✔️ removing elements
numbers.remove(100)  # Remove first occurrence of 100
print(numbers)	# Output: [10, 20, 30, 40, 60]
numbers.pop()  # Remove last element
print(numbers)	# Output: [10, 20, 30, 40]

#✔️ Other useful methods
numbers.sort()  # Sort the list
print(numbers)	# Output: [10, 20, 30, 40]	
numbers.reverse()  # Reverse the list
print(numbers)	# Output: [40, 30, 20, 10]


#✔️ Creating a tuple
coordinates = (10.5, 20, 30.6)

#✔️ Accessing elements in a tuple
print(coordinates[0])	# Output: 10.5
#🔒 Immutable: You cannot modify a tuple once created. Useful for fixed data like latitude/longitude.


'''Task 1: List Operations Practice
Write a program that:
Creates a list of 5 integers input by the user.
Prints:
The original list
Maximum and minimum number
Sorted list in ascending and descending order
'''

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))	
number4	= int(input("Enter fourth number: "))
number5 = int(input("Enter fifth number: "))

print("Original List:", [number1, number2, number3, number4, number5])
print("Maximum Number:", max([number1, number2, number3, number4, number5]))
print("Minimum Number:", min([number1, number2, number3, number4, number5]))
print("Sorted List ascending:", sorted([number1, number2, number3, number4, number5]))	
print("Sorted List descending:", sorted([number1, number2, number3, number4, number5], reverse=True))



'''Task 2: Tuple Usage Simulation
You have employee records as a list of tuples:
employees = [
    ("E001", "Hemanth", "Data Engineer"),
    ("E002", "Ajay", "Data Analyst"),
    ("E003", "Priya", "Data Scientist")
]
Write a program to:
Print all employee names.
Print only employee IDs and designations.
'''

employees = [
	("E001", "Hemanth", "Data Engineer"),	
    ("E002", "Ajay", "Data Analyst"),
	("E003", "Priya", "Data Scientist")	
]

print("Employee Names:")
for employee in employees:
    print(employee[1])  # Print employee name
    
print("Employee IDs and Designations:")
for employee in employees:
    print(f"{employee[0]}, - {employee[2]}")  
    
''' Task 3: Mini ETL Simulation with Lists
You have a file raw_sales.txt with the following lines:
100
abc
200
300
xyz
400

Write a program that:
Reads each line from the file.
Converts valid numeric lines to integers, ignores non-numeric lines.
Stores valid numbers in a list.
Prints:
	List of valid sales numbers
	Total sales
✔️ Hint: Use .isdigit() to check if a string is numeric.
✔️ Expected Output:
Valid sales: [100, 200, 300, 400]
Total sales: 1000
'''	

with open("raw_sales.txt", "r") as file:
    sales = file.readlines()

sales_list = []    
for sale in sales:
    sale = sale.strip()
    if sale.isdigit():
        sale = int(sale)
        sales_list.append(sale)
print("Valid sales:", sales_list)
print("Total sales:", sum(sales_list))	


'''Interview Practice (Day 3)
What is the difference between a list and a tuple in Python?
	List: Mutable, can change elements after creation, defined with [].
	Tuple: Immutable, cannot change after creation, defined with ().
    Prefer tuples for fixed data (e.g. coordinates, DB schema field sets).
    Use lists when data needs modification or appending
'''