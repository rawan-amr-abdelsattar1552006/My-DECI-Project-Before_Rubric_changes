#This is the Source Code of Part B.1 Secure Password Generator App by : Rawan Amr Abdelsattar
# I read the docs of the "random" library from 'https://www.geeksforgeeks.org/python-random-module/'

# Importing the library used to make random choices
import random

#Importing the library to get the alphabet in both upper and lower case
import string

lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)
symbols = ["@", "!", "#", "%", "$", "*", "&", "^", "~", "'", ";", "/", "-", "_", "(", ")"]
numbers = [0,1,2,3,4,5,6,7,8,9]

password_characters = []
password = ""

for i in range(0,3):
	password_characters.append(random.choice(lowercase_alphabet))
	password_characters.append(random.choice(uppercase_alphabet))
	password_characters.append(random.choice(symbols))
	password_characters.append(random.choice(numbers))

print(password_characters)
random.shuffle(password_characters)

for i in range(0,len(password_characters)):
	password += str(password_characters[i])


print("Your Secure Password is : " + password)