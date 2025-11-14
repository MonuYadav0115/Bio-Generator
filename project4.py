"""
Challenge: Emoji enhancer for Messages

Create a python script that takes a message and adds emoji is after specific keywords to make it more expressive 

Your program should:

1. Ask the user to input a message.
2. add emojis after certain keywords (like "happy","love","code","tea",etc.).
3. Print the update message with emojis 

Example:
input:
I love to code and drink tea when I'm happy.

output:
I love ❤️ to code 📺 and drink tea ☕ when i'm happy

Bonus :
- make it case- insensitive (match "happy" or "Hppay")
- Handle punctuation (loke commas or periods right after keawords)

"""

# get dictionary 
emoji_map_fun = {
    "love":"❤️",
    "happy":"😊",
    "code":"📺",
    "tea":"☕",
    "music":"🎶",
    "food":"🍉"

}

# get usermessage 
message = input("enter your message:")
updated_words = []


# process each word 
for word in message.split():
    cleaned = word.lower().strip(".,!?")
    emoji = emoji_map_fun.get(cleaned,"")
    if emoji:
        updated_words.append(f"{word} {emoji}")
    else:
        updated_words.append(word)

updated_message = " ".join(updated_words)
print("\n Enhanced message:\n")
print(updated_message)
