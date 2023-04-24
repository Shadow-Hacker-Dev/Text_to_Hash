
import os
try :
	import hashlib
except ImportError :
	print (" Wait a second ")
	os.system("pip install hashlib")
import sys
print ('''

░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
╚█████╗░███████║███████║██║░░██║██║░░██║░╚██╗████╗██╔╝
░╚═══██╗██╔══██║██╔══██║██║░░██║██║░░██║░░████╔═████║░
██████╔╝██║░░██║██║░░██║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░

██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
 

   ''')

print (''''
presents :
	A text to  encrypted hash tool 
	coded by @Shadow_Hackerz
''')

def encrypt_hash(text_to_encrypt, hash_algorithm):
    
    hash_obj = hashlib.new(hash_algorithm)
    hash_obj.update(text_to_encrypt.encode('utf-8'))
    encrypted_hash = hash_obj.hexdigest()
    print(f"Encrypted {hash_algorithm} Hash: {encrypted_hash}")

def decrypt_hash(hash_to_decrypt):
    # MD5 Hash
    md5_hash = hashlib.md5()
    md5_hash.update(hash_to_decrypt.encode('utf-8'))
    print(f"MD5 Hash: {md5_hash.hexdigest()}")

    
    sha1_hash = hashlib.sha1()
    sha1_hash.update(hash_to_decrypt.encode('utf-8'))
    print(f"SHA1 Hash: {sha1_hash.hexdigest()}")

    
    sha256_hash = hashlib.sha256()
    sha256_hash.update(hash_to_decrypt.encode('utf-8'))
    print(f"SHA256 Hash: {sha256_hash.hexdigest()}")

def main():
    
    while True:
        print("Select an option:")
        print("1. Encrypt a hash")
        print("2. Exit")
        choice = input("Enter your choice (1 or  2): ")

        if choice == '1':
            text_to_encrypt = input("Enter the text to encrypt: ")
            hash_algorithm = input("Enter the hash algorithm (e.g., md5, sha1, sha256, custom_hash1, custom_hash2): ")
            encrypt_hash(text_to_encrypt, hash_algorithm)
        elif choice == '2':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
