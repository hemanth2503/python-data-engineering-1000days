my_string = "Data Engineering"

print(my_string)
print(len(my_string))
print(my_string[0]) # First character
print(my_string[-1]) # Last character)

# String methods
print(my_string.lower())  # Convert to lowercase
print(my_string.upper())  # Convert to uppercase
print(my_string.strip())  # Remove whitespace
print(my_string.replace("Data", "Big Data"))  # Replace substring
print(my_string.split())  # Split into a list of words
separator = " "
print(my_string.split(separator))


words = ["I", "love", "Python"] 
sentense = " ".join(words)  # Join list into a string
print(sentense)  # Output: I love Python

print(my_string.startswith("Big"))  # Check if string starts with "Data"
print(my_string.startswith("Data"))  # Check if string starts with "Data"
print(my_string.endswith("Engineering"))  # Check if string ends with "Engineering"