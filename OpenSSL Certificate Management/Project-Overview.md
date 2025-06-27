# OpenSSL Certificate Management

## Project Overview

This project, completed during my GoMyCode cybersecurity training, focuses on managing OpenSSL certificates on a Kali Linux virtual machine. I generated RSA key pairs, created a Certificate Signing Request (CSR), produced a self-signed certificate, and converted keys to PKCS#12 format. Using OpenSSL commands, I demonstrated proficiency in cryptographic key management and secure system administration. This project showcases my skills in asymmetric cryptography and Linux terminal operations, critical for roles like cybersecurity engineer or SOC analyst.

---

## Objectives

- Verify OpenSSL installation and version on Kali Linux.
- Generate and manage RSA private and public keys.
- Create and verify a Certificate Signing Request (CSR).
- Produce a self-signed certificate valid for 365 days.
- Convert keys and certificates to PKCS#12 format for interoperability.
- Demonstrate Linux terminal proficiency for cryptographic tasks.

---

## Tools and Technologies

- **Operating System:** Kali Linux (GoMyCode-provided VM)
- **Tools:** OpenSSL, Linux terminal commands (`mkdir`, `ls`, `cat`)
- **Environment:** VirtualBox VM
- **Resources:** GoMyCode Learn platform, OpenSSL documentation

---

## Project Setup

### Environment Configuration

- Launched a Kali Linux VM provided by GoMyCode.
- Opened a terminal to execute OpenSSL commands.

### Directory Setup

- Created a `keys` directory to store cryptographic files.

### Tool Verification

- Checked OpenSSL installation with:
  ```sh
  openssl version
  ```

---

## Process and Implementation

### Step 1: Verify OpenSSL Installation

- Ran the following command to confirm OpenSSL version:
  ```sh
  openssl version
  ```
- Ensured OpenSSL was installed and functional.

### Step 2: Create Directory and Generate Private Key

- Created a keys directory:
  ```sh
  mkdir keys
  ```
- Generated a 2048-bit RSA private key:
  ```sh
  openssl genrsa -out keys/corp.gomycode.com.key 2048
  ```
- Verified key creation with:
  ```sh
  ls keys
  ```
- Displayed the private key (PEM format):
  ```sh
  cat keys/corp.gomycode.com.key
  ```

### Step 3: Extract Public Key

- Extracted the public key from the private key:
  ```sh
  openssl rsa -in keys/corp.gomycode.com.key -pubout -out keys/corp.gomycode.com_public.key
  ```
- Confirmed the public key was created in the keys directory.

### Step 4: Generate Certificate Signing Request (CSR)

- Created a CSR with organizational details:
  ```sh
  openssl req -new -key keys/corp.gomycode.com.key -out keys/corp.gomycode.com.csr
  ```
- Filled in fields (e.g., country, organization, common name) as shown in the referenced form.
- Verified the CSR:
  ```sh
  openssl req -text -in keys/corp.gomycode.com.csr -noout -verify
  ```

### Step 5: Generate Self-Signed Certificate

- Created a self-signed certificate valid for 365 days:
  ```sh
  openssl req -newkey rsa:2048 -nodes -keyout keys/corp.gomycode.com.key -x509 -days 365 -out keys/corp.gomycode.com.crt
  ```
- Filled in the same organizational details as the CSR.

### Step 6: Convert to PKCS#12 Format

- Converted the key and certificate to PKCS#12 format:
  ```sh
  openssl pkcs12 -export -name "corp.gomycode.com" -out keys/corp.gomycode.com.pfx -inkey keys/corp.gomycode.com.key -in keys/corp.gomycode.com.crt
  ```
- Set a password for the PKCS#12 file when prompted.

---

## Challenges and Solutions

- **Challenge:** Understanding OpenSSL command syntax and options.  
  **Solution:** Referenced OpenSSL documentation and GoMyCode materials to clarify commands like `genrsa` and `req`.

- **Challenge:** Ensuring correct CSR form inputs (e.g., common name format).  
  **Solution:** Followed the provided form example and practiced with test CSRs.

- **Challenge:** Managing file organization for multiple keys and certificates.  
  **Solution:** Used a dedicated `keys` directory and consistent naming (corp.gomycode.com).

---

## Results and Outcomes

- Successfully verified OpenSSL installation on Kali Linux.
- Generated and managed RSA private and public keys.
- Created and verified a CSR with accurate organizational details.
- Produced a self-signed certificate valid for 365 days.
- Converted keys and certificates to PKCS#12 format for interoperability.
- Captured screenshots of terminal outputs for documentation.

---

## Screenshots of terminal outputs and steps

[OpenSSL Certificate Management – Screenshots](https://docs.google.com/document/d/1u1qOgeSn-ohQCpoA35Y0w0qX1_jWXo-yf7k1Mj9vcbA/edit?usp=sharing)

- Image 1: `openssl version` output.
- Image 2: `ls` output showing corp.gomycode.com.key.
- Image 3: `cat keys/corp.gomycode.com.key` output (private key).
- Image 4: corp.gomycode.com_public.key creation output.
- Image 5: CSR form input during `openssl req`.
- Image 6: CSR verification output (`openssl req -text`).
- Image 7: Self-signed certificate creation output.
- Image 8: PKCS#12 conversion output.

---

## Lessons Learned

- Gained proficiency in OpenSSL for certificate management.
- Learned to generate and manage RSA key pairs and CSRs.
- Understood certificate formats (PEM, PKCS#12) and their use cases.
- Improved Linux terminal skills for cryptographic tasks.
- Developed documentation skills for clear, professional presentation.

---

## Relevance to Cybersecurity

This project mirrors real-world tasks like managing SSL/TLS certificates for web servers, VPNs, or secure applications, critical for cybersecurity engineers and SOC analysts. Secure certificate management ensures data confidentiality and integrity, protecting against man-in-the-middle attacks and unauthorized access.

---

## Future Improvements

- Test the self-signed certificate in a web server (e.g., Apache) to verify functionality.
- Simulate a CA-signed certificate process using a test CA.
- Automate certificate generation with a Bash or Python script.
- Explore TryHackMe’s SSL/TLS labs to deepen certificate management skills.

---

## How to Run

1. Launch a Kali Linux VM and open a terminal.
2. Verify OpenSSL with `openssl version`.
3. Create a `keys` directory and generate RSA keys, CSR, and certificate using the provided commands.
4. Convert to PKCS#12 format and verify outputs with `ls` and `cat`.
5. Optionally, test the certificate in a web server or TryHackMe lab.

---

> Project completed as part of GoMyCode’s cybersecurity training  
> **Author:** Jeremiah Dighomanor (Digho007)
