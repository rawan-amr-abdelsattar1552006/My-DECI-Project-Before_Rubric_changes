# importing Fernet from cryptography library to use it in key generation
from cryptography.fernet import Fernet

# generating the key
key = Fernet.generate_key()

# saving the key to key.txt file  
key_file = open("key.txt", "w+")
key_file.write(key.decode('utf-8'))

# closing the file to save changes
key_file.close()