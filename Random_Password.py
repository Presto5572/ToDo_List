# Completed project

import random
import string

print("|------------------------------------------|")
print("| Welcome to the Random Password Generator |")
print("|------------------------------------------|\n")

# Password preferences
while True:
    password_length = int(input("How long do you want your password to be? (4 - 16 characters): "))
    print("------------------------")
    if password_length > 16:
        print("Password is too long. Try again.")
    elif password_length < 4:
        print("Password is too short. Try again.")
    else:
        break
use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
use_numbers = input("Include numbers? (y/n): ").strip().lower() == "y"
use_special_chars = input("Include special characters? (y/n): ").strip().lower() == "y"
print("------------------------")

# Inserting the different char types
characters = string.ascii_lowercase

# Add other character types based on user input
if use_uppercase:
    characters += string.ascii_uppercase
if use_numbers:
    characters += string.digits
if use_special_chars:
    characters += string.punctuation

# Generate the password
if not characters:
    print("Error incurred. No character types selected. Please restart and choose at least one.")
else:
    # Generate a random password by selecting 'password_length' characters
    password = "".join(random.choice(characters) for _ in range(password_length))

    # Display the generated password
    print("Generated Password:", password)
