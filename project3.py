""""
Challenge: Minutes alive Calculator

Write a python script that calculates approximately how many minutes old a person is based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too)

2. Convert that age into:
  -Total days
  -Total hours
  -Total minutes

3. Display the result in a readable format.

Assumptions:

- You can 365.25 days / year to account for leap years
- You don't need to handle time zone or exact birthdates in this version.

Example:
Input: 
  - age:23

output:
   You are approximately:
  - 9,131 days
  - 219,144 hours old
  - 13,148,640 minutes old


Bonus:
add comma formatting for large numbers 
let the user try again withot restaring the program


"""

def calculate_minutes(age_years):

    DAY_IN_YEAR = 365.25
    HOURS_IN_DAY = 24
    MINUTES_IN_HOURS = 60

    total_day = age_years * DAY_IN_YEAR
    total_hours = total_day * HOURS_IN_DAY
    total_minutes = total_hours * MINUTES_IN_HOURS

    return round(total_day),round(total_hours),round(total_minutes)

while True:
    try:
        age = float(input("Enter your age in years"))
        days,hours,minutes = calculate_minutes(age)

        print("\n You are approx:")
        print(f"  - {days}  days old")
        print(f"  - {hours}  hours old")
        print(f"  - {minutes}  minutes old \n")

        again = input("would you like to try again (y/n)").strip().lower()

        if again != "y":
            print("Good bye😊!")
            break

    except:
        print("please enter a valid number for age")

