''' 
    Day 9: Working with Files + Lists Togethe
    Read data from a file into a list
    Process that list (filter, transform, search, etc.)
    Write the processed result back to another file
'''

# Example 1: Reading numbers from a file into a list, from numbers.txt
with open ("numbers.txt", "r") as f:
    lines = f.readlines()
print("Raw lines:", lines)    

numbers = []
for line in lines:
    try:
        numbers.append(int(line.strip()))
    except ValueError:
        print(f"Skipping invalid value: {line.strip()}")
print("Valid numbers", numbers)        

squared = [n**2 for n in numbers]
print("Squared Numbers:", squared)

with open("squared_numbers.txt", "w") as f:
    for n in squared:
        f.write(str(n) + "\n")



# Example 2: Example 2: Names processing
with open("names.txt", "r") as f:
    rawlines = f.readlines()
print("Raw names", rawlines)    

# Filter names startsing with 'D'
name = [x for x in rawlines if x.startswith("D")]
print("Names starting with D:", name)

# Save to file
with open("d_names.txt", "w") as f:
    for x in name:
        f.write(x + "\n")


# Example 3: Numbers processing using nums.txt, ignore invalid values and find sum, avg of valid numbers. save results to file
with open("nums.txt", "r") as f:
    rawdata = f.readlines()
numbers = []
for r in rawdata:
    try:
        numbers.append(int(r.strip()))
    except ValueError:
        print(f"Skipping the invalid value, {r.strip()}")
total = sum(numbers)
if len(numbers) > 0:
    avg = total / len(numbers)
with open ("results.txt", "w") as f:
    f.write("Sum = "+ str(total) + "\n")
    f.write("Average = "+ str(avg) + "\n")


# Example 4: Student Names, read data from students.txt, extract the name start with "S", write to s_names.txt
with open("students.txt", "r") as f:
    all_students = f.readlines()
s_names = [x.strip() for x in all_students if x.startswith("S")]
with open("s_names.txt", "w") as f:
    for x in s_names:
        f.write(x + "\n")

# Example 5: Word counter, read data from story.txt, count how many words in there in total, write to word_count.txt    
with open("story.txt", "r") as f:
    story_lines = f.readlines()
word_count = 0
for l in story_lines:
    word_count += len(l.split())
with open("word_count.txt", "w") as f:
    f.write(str(word_count))