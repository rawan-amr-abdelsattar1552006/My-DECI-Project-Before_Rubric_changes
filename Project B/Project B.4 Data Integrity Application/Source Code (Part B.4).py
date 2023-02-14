# This is the Source Code of Part B.4 Data Integrity App by : Rawan Amr Abdelsattar

# Importing the library used to implement the md5 hashin algorithm
import hashlib

# Setting up some variables
run = True
myHash = ""

# App loop
while run :

	# Prompting the user to select their desired service 
	print("\nPress 'c' for integrity check and 'h' to generate a hash of your file or 'q' to quit")
	service = input("(c/h/q): ")
	
	# Checking if the user wants to quit
	if service == "q":
		run = False

	# Checking if the user wants to check file's integrity
	elif service == "c":
		file_path = input("Type in the path to the file you want to check: ").replace("\\", "/").replace('"', "")
		hash_file_path = input("Type in the path to the file's hash : ").replace("\\", "/").replace('"', "")
		
		# opening the file and the corresponding hash file (checking if the input is valid)
		try:
			global file
			file = open(file_path , "r")
		except:
			print("Please Enter a valid path: ")
			file_path = input("Type in the path to the file you want to check: ").replace("\\", "/").replace('"', "").replace('"', "")
			file = open(file_path , "r")
		
		try:
			global hash_file
			hash_file = open(hash_file_path , "r")
		except:
			print("Please Enter a valid path: ")
			hash_file_path = input("Type in the path to the file's hash : ").replace("\\", "/").replace('"', "")
			hash_file = open(hash_file_path , "r")

		# Reading the files into strings
		file_data = file.read()
		hash_data = hash_file.read()
		
		# Generating our own md5 hash of the file
		myHash = hashlib.md5(file_data.encode()).hexdigest()
		
		# checking if the input hash matches with the generated hash
		if myHash == hash_data:
			print("Integrity Confirmed")
		else:
			print("Integrity Violated")

	# Checking if the user wants to generate the hash value of a file
	elif service == "h":
		file_path = input("Type in the path to the file you want to generate its hash: ").replace("\\", "/").replace('"', "")

		# opening the input file(checking if the input is valid)
		try:
			file = open(file_path , "r")
		except:
			print("Please Enter a valid path: ")
			file_path = input("Type in the path to the file you want to check: ").replace("\\", "/").replace('"', "")
			file = open(file_path , "r")

		# Reading the input file into a string
		file_data = file.read()
		
		# Generating the md5 hash value and saving it into the output file 
		myHash = hashlib.md5(file_data.encode()).hexdigest()
		generatedHashFile = open("Sample Output (hash).txt", "w")
		generatedHashFile.write(myHash)
		generatedHashFile.close()
		print("\nHashing done" + "\nThis file's hash is : " + myHash + " You can also open the file 'Sample Output (hash).txt' to see the generated hash")

	else :
		print("Invalid input ! Try again")
		print("\nPress 'c' for integrity check and 'h' to generate a hash of your file or 'q' to quit")
		service = input("(c/h/q): ")






