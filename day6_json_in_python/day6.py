import json

'''1. Load JSON from a string'''

data = '{"name":"Hemanth", "age":28}'
parsed = json.loads(data)
print(parsed["name"])



'''2. Load JSON from a file'''

with open("person.json", "r") as file:
	person = json.load(file)
	print(person["age"])




'''3. Dump data to json'''

data = {
		"name": "Hemanth",
		"skills": ["Python", "SQL"]
		}

with open("output.json", "w") as file:
	json.dump(data, file, indent =4)


'''4.Working with Nested JSON (Very Important)'''
data = {
    "employee": {
        "name": "Priya",
        "contact": {
            "email": "priya@example.com",
            "phone": "1234567890"
        }
    }
}

# Get the whole employee dictionary
emp = data["employee"]

# Get the name of the employee
name = data["employee"]["name"]

# Get contact info
contact = data["employee"]["contact"]

# Get email and phone
email = data["employee"]["contact"]["email"]
phone = data["employee"]["contact"]["phone"]

print("Employee Name:", name)
print("Email:", email)
print("Phone:", phone) 


'''
5.Practice Task – Parse and Extract
Write code to:
Load JSON from file
Print names and email addresses
Print all skills for each user
'''

with open("sample.json", "r") as f:
	data = json.load(f)

for user in data["users"]:
	print("----")
	print(f"Name: {user['name']}, \nEmail: {user['email']}")
	print(f"Skills:", ",".join(user["skills"]) )

python_users = [user for user in data["users"] if "Python" in user["skills"]]
with open("python_users.json", "w") as file:
	data = json.dump(python_users, file, indent = 4)


'''
JSON to Python mapping
object{} 	-->		dict{}
array[]		-->		list[]
string		-->		str
number		-->		int/float
true/false	-->		TRUE/FALSE
null		-->		None
'''

