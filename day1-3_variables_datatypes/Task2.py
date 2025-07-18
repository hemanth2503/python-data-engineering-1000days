'''
You received a text file containing prices (one price per line). Create a file named prices.txt with these values:
100
150
200
50
300
✅ Write a Python program that:
Reads each price from the file.
Converts them to integers.
Calculates and prints:
Total sum
Average price
✔️ Expected Output:
Total sum of prices: 800
Average price: 160.0
'''
import os
print("Your CWD is ", os.getcwd())

with open("prices.txt", "r") as file:
    lines = file.readlines()

prices = []
for line in lines:
    price = int(line.strip())
    prices.append(price) 

total_sum = sum(prices)
average = total_sum/len(prices)

print(f"Total sum of prices: {total_sum}")
print(f"Average price: {average}")

'''
🔍 How it works
open() opens the file.
readlines() reads all lines as strings.
strip() removes newline characters.
int() converts string to integer.
sum() adds all numbers in the list.
len() counts total prices for average calculation.
'''    