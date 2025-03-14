# This is day 2 program of the python basics that will generate a tip calculator
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?\n$"))
tip = int(input("what percentage of tip would you like to give? 10, 12, or 15?\n  "))
no_of_people =float( input("How many people to split the bill? \n"))
total_tip = total_bill * (tip/100)
bill = (total_bill + total_tip )/no_of_people
print(bill)