import hashlib

def calculate_md5(input_string):
    # Convert string to bytes and compute MD5 hash
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    return md5_hash

if __name__ == "__main__":
    message = input("Enter a string to hash: ")
    hash_result = calculate_md5(message)
    print(f"MD5 Hash: {hash_result}")