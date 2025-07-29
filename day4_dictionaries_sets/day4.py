'''
Part1: Python Dictionaries
mutable collection of key-value pairs
keys must be unique and immutable
'''
person = {"name": "Bob", "city": "New York", "age": 30}
print(person["name"])  # Access
person["age"] = 31  # Update
del person["city"]  # Delete

#Iterating through keys and values
for key, value in person.items():
    print(f"{key}: {value}")





'''Part2: Python Sets
unordered collection of unique elements
'''    
my_set = {"apple", "banana", "cherry"} # Create
my_set.add("orange")  # Add
my_set.remove("banana")  # Remove
if "apple" in my_set:
    print("Apple is in the set")  # Check membership

# iterating through a set
for fruit in my_set:
    print(fruit)





'''
Set logic = Venn diagram in Python
Intersection (∩): a & b → only shared items
Union (∪): a | b → everything, no duplicates
Difference (−): a - b → items in a not in b
Symmetric Difference (∆): a ^ b → items not in both
'''
set1 = {"apple", "banana"}
set2 = {"banana", "cherry"}        
print(set1.union(set2))  # Union: {'apple', 'banana', 'cherry'}
print(set1.intersection(set2))  # Intersection: {'banana'}
print(set1.difference(set2))  # Difference: {'apple'}
print(set1.symmetric_difference(set2))  # Symmetric Difference: {'apple', 'cherry'}

cities = ["Delhi", "Mumbai", "Bangalore", "Chennai", "Delhi"]
unique_cities = set(cities)  # Convert list to set for uniqueness
print(unique_cities)  # Output unique cities


