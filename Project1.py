""" 
Challenge: Stylish Bio Generator for Instagram/ Twitter

Create a python utility that asks the user for a few key details and generates a short stylish bio that could be used for social media profilies like instagram or twitter.abs

Your  Program should:

1. Prompt the user to enter thair:
-Name 
- Profession 
-One-liner passion or goal
-Favorite emoji (optional)
-website or handle(optional)

2- generate a stylish 2-3 line bio using the inputs.it should feel modern concise and catchy

3- add optional hashtag or emojis for flair

Example:
Name: Monu
Profession: Student 
Passion: Coding 
Emoji:😊
Website:@monu.design

Output:
  😊Monu | Student
  📺Coding
  🎶@monu.designer

  Bonus :
  let the user pick from 2-3 different layout styles.
  ask the user if they want to save the result into a `txt` file.

""" 
import textwrap

name = input("Enter you name: ").strip()
profession = input("Enter you profession: ").strip()
passion = input("Enter you passion: ").strip()
emoji = input("Enter you emoji: ").strip()
website = input("Enter you website: ").strip()

print("\n choose your style:")
print("1-simple lines: ")
print("2-vertical flair: ")
print("3-Emoji smile: ")

style = input("Enter 1,2 and 3:").strip()

def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession} \n {website}"
    elif style == "2":
        return f"{emoji} {name} \n {profession}🤖 \n {passion} \n {website}🤖"
    elif style =="3":
        return f"{emoji*3} \n {name} - {profession} \n {passion} \n {website} \n {emoji*3} "


bio = generate_bio(style)
print("\nYour styleish bio: \n")
print("*" * 80 )
print(textwrap.dedent(bio))
print("*" * 80 )

