'''Basic Function Definition'''
def greet():
    print("Hello, welcome to the function demonstration!")
greet()

'''Function with Parameters'''
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 3)
print(f"The sum of 5 and 3 is: {result}")

'''Function with Return'''
def double_value(x):
    return x * 2
result = double_value(25)
print(f"The double of 25 is : {result}")


'''Default Parameters'''
def power(base, exponent=2):
    return base ** exponent
print(power(3))  # Uses default exponent of 2
print(power(3, 3))  # Uses provided exponent of 3


def add_numbers(a,b):
    return a + b
print(add_numbers(10, 20))  # Output: 30

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(celsius_to_fahrenheit(25))  # Output: 77.0

raw_data = ["100", "200", "300", "abc", "N/A", "400"]
def clean_and_sum(data_list):
    total = 0
    for item in data_list:
        try:
            total += int(item)
        except ValueError:
            print(f"Skipping invalid value: {item}")
    return total
total_sum = clean_and_sum(raw_data)
print(f"The total sum of valid numbers is: {total_sum}")

