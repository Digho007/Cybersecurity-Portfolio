from cryptography.fernet import Fernet

# Generate a symmetric key
key = Fernet.generate_key()
cipher = Fernet(key)

# Get user input
message = input("Enter a message to encrypt: ")

# Encrypt the message
encrypted = cipher.encrypt(message.encode())
print(f"Encrypted: {encrypted}")

# Decrypt the message
decrypted = cipher.decrypt(encrypted).decode()
print(f"Decrypted: {decrypted}")

# Optionally, print the key for future use
print(f"Key (save this securely if you want to decrypt later): {key.decode()}")