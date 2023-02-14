# This is the Source Code of Part B.3 Data Confidentiality App by : Rawan Amr Abdelsattar
# I read the docs of the 'cryptography' library from 'https://pypi.org/project/cryptography/'


# Importing the Fernet object from the cryptography library used in encryption and decryption
from cryptography.fernet import Fernet
import os.path

AppEnd = False

#App's loop
while not AppEnd:
	# Prompting the user to choose a service 
	service = input("Type 'e' for encryption service or 'd' for decryption service or 'q' to quit: \n(e/d/q): ")

	# Checking if user selected the encryption serivce
	if service == 'e' :
		file_path = input("Type in the path to the file you want to encrypt :  ").replace("\\" , "/").replace('"', "")
		key_file_path = input("Type in the path to the key to be used to encrypt the file : ").replace("\\" , "/").replace('"', "")

		end = False

		# validating user input through a while loop
		while not end:
			# in case of the two input paths are valid
			if os.path.isfile(file_path) and os.path.isfile(key_file_path):
				
				# splitting path to get extension of yhe file
				name_and_ext_tup = os.path.splitext(file_path)
				
				# opening the data and key files and reading their data
				file = open(file_path, "rb")
				data = file.read()
			
				key_file = open(key_file_path, "rb")
				key = key_file.read()
				
				# defining object used to encrypt the file
				f = Fernet(key)

				# performing encryption if input passes rule tests
				if len(data) > 16 and name_and_ext_tup[1] == '.txt':
					encryptedData = f.encrypt(data)
					
					encrypted_file = open("Encrypted Output Sample.txt.encbyrawan", "wb")
					encrypted_file.write(encryptedData)
					print("\nEncryption Done")
					end = True
					# closing files to save changes
					file.close()
					key_file.close()
					encrypted_file.close()

				# checking the length of input to apply rule #2 in encryption rules
				elif len(data) < 16:
					print("Too short input cannot be encrypted !")
					end = True

				# checking the extension of input file to apply rule #3 in encryption rules
				elif name_and_ext_tup[1] != '.txt':
					print("Invalid input file extension, only txt files can be encrypted !")
					end = True

			# in case of the data file path is invalid
			elif not os.path.isfile(file_path):
				print("Invalid file path , Try again...")
				file_path = input("Type in the path to the file you want to encrypt : ").replace("\\" , "/").replace('"', "")
			

			# in case of the key file path is invalid
			elif not os.path.isfile(file_path):
				print("Invalid path , Try again...")
				key_file_path = input("Type in the path to the key to be used to encrypt the file :").replace("\\" , "/").replace('"', "")

	# Checking if user selected the decryption serivce
	elif service == 'd':
		file_path = input("Type in the path to the file you want to decrypt :  ").replace("\\" , "/").replace('"', "")
		key_file_path = input("Type in the path to the key to be used to decrypt the file : ").replace("\\" , "/").replace('"', "")

		end = False

		# validating user input through a while loop
		while not end:
			# in case of the two input paths are valid
			if os.path.isfile(file_path) and os.path.isfile(key_file_path):
				
				# splitting path to get extension of yhe file
				name_and_ext_tup = os.path.splitext(file_path)
	

				# opening the data and key files and reading their data
				file = open(file_path, "rb")
				data = file.read()
			
				key_file = open(key_file_path, "rb")
				key = key_file.read()
				
				# defining object used to encrypt the file
				f = Fernet(key)

				# performing decryption if input passes rule tests
				if len(data) > 16 and name_and_ext_tup[1] == '.encbyrawan':
					decryptedData = f.decrypt(data)
					
					decrypted_file = open("Decrypted Output Sample.txt", "wb")
					decrypted_file.write(decryptedData)
					print("\nDecryption Done")
					end = True

					# closing files to save changes
					file.close()
					key_file.close()
					decrypted_file.close()


				# checking the length of input to apply rule #2 in decryption rules
				elif len(data) < 16:
					print("Too short input cannot be decrypted !")
					end = True

				# checking the extension of input file to apply rule #3 in decryption rules
				elif name_and_ext_tup[1] != '.encbyrawan':
					print("Invalid input file extension, only '.encbyrawan' files can be decrypted !")
					end = True
					

			# in case of the data file path is invalid
			elif not os.path.isfile(file_path):
				print("Invalid file path , Try again...")
				file_path = input("Type in the path to the file you want to decrypt : ").replace("\\" , "/").replace('"', "")
			

			# in case of the key file path is invalid
			elif not os.path.isfile(file_path):
				print("Invalid path , Try again...")
				key_file_path = input("Type in the path to the key to be used to decrypt the file :").replace("\\" , "/").replace('"', "")

	# Checking if user wanted to quit the application
	elif service == 'q':
		AppEnd = True

	# checking if user input is an invalid service, and re-prompting input
	else:
		print("Invalid Service, Please try again..")
		service = input("Type 'e' for encryption service or 'd' for decryption service : \n(e/d/q): ")
