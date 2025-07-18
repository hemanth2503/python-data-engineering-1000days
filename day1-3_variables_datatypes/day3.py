'''
Task : Write a program that:
    Takes a sentence input from the user.
    Prints:
    The sentence in uppercase
    The sentence in lowercase
    Number of words in the sentence
'''

message = input("Enter a sentence: ")
print(message.upper())
print(message.lower())
words = message.split()
print(len(words))


'''
Task 2: Data Cleaning Simulation
Create a file emails.txt
Reads each email from the file.
Cleans it by:
Removing extra spaces
Converting to lowercase
Saves the cleaned emails to a new file called cleaned_emails.txt
'''

cleaned_emails = []
with open("emails.txt", "r") as file:
    emails = file.readlines()
    for email in emails:
        email = email.strip()
        email = email.lower()
        cleaned_emails.append(email)      
with open("cleaned_emails.txt", "w") as file:
    for cleaned_email in cleaned_emails:
        file.write(cleaned_email + "\n")


'''
Task 3 : You have a string:
log = "2025-07-14 10:35:21,INFO,UserLogin,username=hemanth"
Write a program to extract:
Date: 2025-07-14
Time: 10:35:21
Log Level: INFO
Event: UserLogin
Username: hemanth
✔️ Hint: Use .split(",") and further splits on = for username.
'''

log = "2025-07-14 10:35:21,INFO,UserLogin,username=hemanth"

parts = log.split(",")
datetime = parts[0].split(" ")
date = datetime[0]
time = datetime[1]
log_level = parts[1]
event = parts[2]
username = parts[3].split("=")[1] 

print("Date:", date)
print("Time:", time)
print("Log Level:", log_level)
print("Event:", event)
print("Username:", username)