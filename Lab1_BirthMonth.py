# PART 1: Write a program that asks for your name and the month you were born in.

# getting an input for name
name = input("What is your name? ")
# using the input provided
print(f"Hello, {name}!")
# len() function returns the number of characters in string name
num_letters = len(name)
# using the input from above, where f is used to format string
print(f"Your name has {num_letters} letters.")

"""
--->Bonus question – can you detect if the month entered is the
same as the current month, no matter when you run the
program?
"""

# importing packages
"""this line of code imports the entire ‘datetime’ module 
so you can access all the classes and functions in the module 
by qualifying them with the module name ‘datetime’ ---
source: https://medium.com/@sara.khorram/import-datetime-vs-from-datetime-import-datetime-a30ffa925c9f
"""

import calendar
from datetime import datetime

# getting an input for birth month
birth_month = input("When is your birth month? ")
# current date and time
today = datetime.now()

current_month = calendar.month_name[datetime.today().month]
print("Current Month: ", current_month)

if current_month == birth_month:
    print("Happy birthday month! ")
else:
    print("Not the current month!")

""" 
Note to self: The strftime() method returns a string representing date and time using date, time or datetime object:
example:  current_month = today.strftime("%b")
"""
