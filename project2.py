""" Challenge: Simple Bill Splitter

Write a python script that helps split a bill evenly between friends.

Your Program should :
1. Ask how many people are in the group 
2. Ask for each person's name 
3. Ask for the total bill amount 
4. Calculate each person's share of the bill 
5. Display how much each person owes in a clean readable format

Example:
Total Bill:1200
People: Aman, Neha, Ravi

Each person owes:400

Final output:
aman: owes :400
Neha: owes :400
Ravi: owes :400

Bonus:
round to 2 decimal places
print a decorative summary box

"""
def get_float(promt):
    while True:
        try:
            return float(input(promt))
        except ValueError:
            print("❌ please enter a valid number")



num_people = int(input("How many people are there in the group?"))

names = []

for i in range(num_people):
    name = input(f"enter the name of person # {i+1}").strip()
    names.append(name)

toatal_bill = get_float("enter the bill amount in number only:")

share = round(toatal_bill / num_people, 2 )

print("\n" + "*" * 50)
print(f"Total bill:{toatal_bill}")
print(f"Each person owes {share}")

for name in names:
    print(f" {name} owes {share} rupees")
print("\n" + "*" * 50 )
