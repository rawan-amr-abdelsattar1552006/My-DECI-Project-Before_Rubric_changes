#This is the Source Code of Part B.2 Password Security Strength Evaluator App by : Rawan Amr Abdelsattar

# importing the library used to get all alphabet letters
import string

# intializing our characters list in each type 
lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)
symbols = ["@", "?","=", "<",">",":","{", "}","!", "#", "%", "$", "*", "&", "^", "~", "'", ";", "/", "-", "_", "(", ")"]
numbers = [0,1,2,3,4,5,6,7,8,9]


# the running of our application depends on this variable , it's true until the user types in 'q'
run = True

# app's loop
while run :

	# prompting user to type in a password
	print("\nThis is the password security strength evaluator app")
	password = input("\nType in your password or type 'q' to quit: ").replace(" ", "")
	
	# checking if the user wants to quit
	if password == "q":
		run = False

	# categorizing the password according to its length and content
	elif len(password) < 4:
		print("\nThis cannot be a password ! please type in a password to be evaluated..")
		password = input("\nType in your password or type 'q' to quit: ").replace(" ", "")

	elif len(password) >= 12 and any(str(i) in password for i in numbers) and any(i in password for i in lowercase_alphabet) and any(i in password for i in uppercase_alphabet) and any(i in password for i in symbols):
		print("\nCategory: Strong Password \nDescrption: Your password is 12 or more characters long and includes all of the following characters types : lowercase letters, uppercase letters, numbers and symbols \nMeets minimum requirement: Yes")

	elif (len(password) > 8) and ((any(str(i) in password for i in numbers) and any(i in password for i in lowercase_alphabet)) or (any(str(i) in password for i in numbers) and any(i in password for i in uppercase_alphabet)) or (any(str(i) in password for i in numbers) and any(i in password for i in symbols)) or (any(i in password for i in symbols) and any(i in password for i in lowercase_alphabet)) or (any(i in password for i in symbols) and any(i in password for i in uppercase_alphabet)) or (any(i in password for i in symbols) and any(str(i) in password for i in numbers)) or (any(i in password for i in uppercase_alphabet) and any(i in password for i in lowercase_alphabet)) or (any(i in password for i in uppercase_alphabet) and any(i in password for i in symbols)) or (any(i in password for i in uppercase_alphabet) and any(str(i) in password for i in numbers)) or (any(i in password for i in lowercase_alphabet) and any(i in password for i in symbols)) or (any(i in password for i in lowercase_alphabet) and any(i in password for i in uppercase_alphabet)) or (any(i in password for i in lowercase_alphabet) and any(str(i) in password for i in numbers))):
		print("\nCategory: Fair Password \nDescrption: Your password is 12 or more characters long and includes at least two of the following characters types : lowercase letters, uppercase letters, numbers and symbols \nMeets minimum requirement: Yes")

	else :
		print("\nCategory: Weak Password \nDescrption: Your password is 8 or less characters long or at any length but includes only one of the following characters type : lowercase letters, uppercase letters, numbers and symbols \nMeets minimum requirement: No \n\nWarning: Your Password needs to be re-chosen or re-generated to be secure")

