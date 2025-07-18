'''
    Task 1: Write a program that:
    Asks the user for their name, age, and city.
    Prints a message: “Hello <name>, you are <age> years old and live in <city>.”
    Enter your name: Hemanth
    Enter your age: 28
    Enter your city: Hyderabad
    Hello Hemanth, you are 28 years old and live in Hyderabad.
'''    

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

print(f"Hello {name}, you are {age} years old and live in {city}.")



'''
    Write a program that:
    Takes two numbers from user input.
    Prints their sum, difference, product, and division result.
    ✔️ Example Output:
    Enter first number: 20
    Enter second number: 4
    Sum: 24
    Difference: 16
    Product: 80
    Division: 5.0
'''

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
Sum = x + y
diff = abs(x - y)
multi = x * y
div = x / y
print(f"Sum: {Sum}")
print(f"Difference: {diff}")
print(f"Product: {multi}")
print(f"Division: {div}")
