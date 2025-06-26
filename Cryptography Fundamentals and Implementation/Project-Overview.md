# Cryptography Fundamentals and Implementation

## Project Overview

This project, completed during my GoMyCode cybersecurity training, demonstrates my understanding of cryptography through theoretical exercises and practical Python implementations. I explored symmetric and asymmetric cryptography, performed encryption/decryption with Caesar and Vigenère ciphers, generated RSA key pairs, and implemented Python programs for symmetric encryption and MD5 hashing. Additionally, I analyzed digital signatures for secure communication. This project showcases my skills in cryptographic concepts, secure coding, and system security, critical for roles like cybersecurity engineer or SOC analyst.

---

## Objectives

- Define core cryptography concepts (plaintext, ciphertext, encryption, decryption).
- Compare symmetric and asymmetric cryptography and their goals.
- Apply symmetric ciphers (Caesar, Vigenère) for encryption and decryption.
- Generate and use RSA key pairs for asymmetric encryption/decryption.
- Compare DES and AES algorithms and explain hash functions.
- Implement Python programs for symmetric encryption and MD5 hashing.
- Explain digital signatures and their role in verifying authenticity.

---

## Tools and Technologies

- **Programming Language:** Python
- **Libraries:** cryptography, hashlib
- **Tools:** Calculator for RSA math, text editor (e.g., VS Code)
- **Resources:** GoMyCode Learn platform
- **Environment:** Local Python environment

---

## Project Setup

### Environment Configuration

- Set up a Python environment with cryptography and hashlib libraries installed (`pip install cryptography`).
- Used a text editor to write and test Python code.

### Theoretical Exercises

- Performed manual calculations for Caesar, Vigenère, and RSA tasks.
- Researched cryptographic concepts using GoMyCode resources.

### Coding Tasks

- Developed Python scripts for symmetric encryption and MD5 hashing.
- Tested scripts with sample inputs to verify functionality.

---

## Process and Implementation

### Step 1: Cryptography Concepts

- **Plaintext:** Original, readable data before encryption.
- **Ciphertext:** Unreadable data after encryption.
- **Encryption:** Converting plaintext to ciphertext using a key.
- **Decryption:** Converting ciphertext back to plaintext.
- **Symmetric:** Same key for encryption/decryption (e.g., AES, DES).
- **Asymmetric:** Public key for encryption, private key for decryption (e.g., RSA).
- **Goals:** Confidentiality, integrity, authentication, non-repudiation.

### Step 2: Symmetric Key Cryptography

- **Caesar Cipher (Shift 3):**  
  - Encrypted "HELLO" to "KHOOR": H→K, E→H, L→O, L→O, O→R  
  - Decrypted "VWDQGD" to "STANDA": V→S, W→T, D→A, Q→N, G→D, D→A

- **Vigenère Cipher (Keyword: CRYPTO):**  
  - Encrypted "OPENAI" to "QGCTTW":  
    O (shift 2)→Q, P (shift 17)→G, E (shift 24)→C, N (shift 15)→C, A (shift 19)→T, I (shift 14)→W

### Step 3: Asymmetric Key Cryptography

- **RSA Key Pair Generation:**  
  - Used primes p=17, q=11 to calculate:  
    - Modulus: n = 17 × 11 = 187  
    - Euler’s totient: ϕ(n) = (17-1) × (11-1) = 160  
    - Public exponent: e = 5  
    - Private exponent: d = 129 (since 129 × 5 mod 160 = 1)  
    - Public key: (5, 187)  
    - Private key: (129, 187)

- **RSA Encryption:**  
  - Encrypted "SECRET" with public key (5, 221):  
    S(19)→143, E(5)→31, C(3)→22, R(18)→24, E(5)→31, T(20)→107  
    Ciphertext: [143, 31, 22, 24, 31, 107]

- **RSA Decryption:**  
  - Decrypted ciphertext "196" with private key (53, 221):  
    M = 196^53 mod 221 = 19 (S)  
    Plaintext: "S"

### Step 4: Cryptographic Algorithms

- **DES vs. AES:**  
  - DES: 56-bit key, 64-bit block, weak against brute-force, obsolete.  
  - AES: 128/192/256-bit keys, 128-bit block, highly secure, current standard.

- **Hash Function:**  
  - Defined as deterministic, irreversible, collision-resistant, fast.  
  - Example: SHA-256 hash of "hello" = `2cf24dba5fb0a30e26e83b2ac5b9e29e1b170e8d7f04a2d9e7d2566b1d0f5615`.

- **Hybrid Cryptosystem:**  
  - Combines symmetric (fast data encryption) and asymmetric (secure key exchange).
  - Example: HTTPS uses RSA for key exchange, AES for session encryption.

### Step 5: Practical Application

#### Symmetric Encryption Program

Developed a Python program using the cryptography library to encrypt/decrypt user input with a symmetric key.

```python
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
```

#### MD5 Hash Function

Implemented a Python function to calculate the MD5 hash of a string.

```python
import hashlib

def calculate_md5(input_string):
    # Convert string to bytes and compute MD5 hash
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    return md5_hash

# Example usage
message = input("Enter a string to hash: ")
hash_result = calculate_md5(message)
print(f"MD5 Hash: {hash_result}")
```

#### Digital Signatures

- Explained creation (hash message, encrypt with private key), verification (decrypt with public key, compare hash), and roles (authentication, integrity, non-repudiation).
- Applications: Email, software distribution, contracts, banking.

---

## Challenges and Solutions

- **Challenge:** Calculating RSA private key (d) manually was complex.  
  **Solution:** Used a calculator to solve (d × e) mod ϕ(n) = 1, verifying with modular arithmetic.
- **Challenge:** Understanding Vigenère cipher’s keyword-based shifting.  
  **Solution:** Practiced with smaller examples and referenced GoMyCode materials.
- **Challenge:** Installing cryptography library for Python program.  
  **Solution:** Used `pip install cryptography` and tested in a virtual environment.

---

## Results and Outcomes

- Successfully applied Caesar and Vigenère ciphers for encryption/decryption.
- Generated and used RSA key pairs for secure communication.
- Compared DES and AES, highlighting AES’s superiority.
- Implemented and tested Python programs for symmetric encryption and MD5 hashing.
- Explained digital signatures, demonstrating their role in secure systems.
- Produced screenshots of code and calculations for documentation.

---

## Lessons Learned

- Gained proficiency in symmetric and asymmetric cryptography techniques.
- Learned to implement cryptographic functions in Python using cryptography and hashlib.
- Understood the practical applications of digital signatures in securing communications.
- Developed skills in explaining complex cryptographic concepts clearly.

---

## Relevance to Cybersecurity

This project mirrors real-world cryptography tasks, such as securing data transmission and verifying authenticity, critical for cybersecurity engineers and SOC analysts. Skills like RSA key generation and digital signatures are essential for designing secure systems, while Python implementations demonstrate practical coding abilities.

---

## Future Improvements

- Simulate encryption/decryption in a TryHackMe lab to test real-world applications.
- Implement a digital signature program in Python using cryptography.
- Explore advanced algorithms like elliptic curve cryptography (ECC).
- Test hash functions with larger datasets to analyze performance.

---

## How to Run

1. Install Python and required libraries:  
   `pip install cryptography`
2. Run `symmetric_encryption.py` to encrypt/decrypt a user message.
3. Run `md5_hash.py` to calculate the MD5 hash of a string.
4. Review theoretical exercises (Caesar, Vigenère, RSA) in the README.
5. Optionally, simulate RSA encryption in a calculator or Python.

---

> Project completed as part of GoMyCode’s cybersecurity training  
> **Author:** Jeremiah Dighomanor (Digho007)
