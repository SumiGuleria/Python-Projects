'''Scenario:
Write a Python program where:

The user inputs their name (string), age (integer), and height (float).
Print a formatted string like:
"Hello [name], you are [age] years old and [height] meters tall."
Check if the age is greater than 18 and print True or False.'''

name = input("Enter the name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
print(f"Hello {name}, you are {age} years old and {height} meters tall")

if age > 18:
    print("True")
else:
    print("False")
