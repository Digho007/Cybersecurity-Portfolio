# Network Reconnaissance and Traffic Analysis

## Project Overview

This project, completed during my GoMyCode cybersecurity training, focuses on network reconnaissance and traffic analysis across Kali Linux, Windows, and Debian virtual machines. I used tools like Nmap, Wireshark, and tcpdump to identify IP addresses, scan for open ports, resolve domain names, and analyze network traffic. The project also involved configuring a Windows Server’s IIS web server and sniffing authentication attempts, simulating real-world tasks for a cybersecurity engineer. This work showcases my skills in network security, system administration, and ethical hacking, relevant to roles like SOC analyst or cybersecurity engineer.

---

## Objectives

- Identify IP addresses of Kali Linux, Windows, and Debian VMs using command-line tools.
- Perform port scanning with Nmap to discover services running on target machines.
- Resolve Fully Qualified Domain Names (FQDNs) using `nslookup` and `dig`.
- Verify network connectivity with `ping` and analyze web server responses with `curl`.
- Configure IIS on Windows Server to enable Basic Authentication.
- Sniff and analyze network traffic using `tcpdump` and Wireshark to inspect authentication attempts.

---

## Tools and Technologies

- **Operating Systems:** Kali Linux (username: kali, password: kali), Windows Server (password: Gomycode01*), Debian (password: Gomycode01*)
- **Tools:** `ipconfig`, `ifconfig`, `ip addr`, Nmap, nslookup, dig, ping, curl, tcpdump, Wireshark, Firefox, IIS
- **Environment:** VirtualBox VMs provided by GoMyCode
- **Other:** Sample network traffic and web server setup

---

## Project Setup

### Environment Configuration

- Set up three VMs: Kali Linux, Windows Server, and Debian, using GoMyCode-provided images.
- Configured network settings to ensure connectivity between VMs.

### Tool Installation

- Verified Nmap, tcpdump, and Wireshark were pre-installed on Kali Linux.
- Ensured IIS was running on Windows Server for web server tasks.

### Test Environment

- Used IP `172.16.103.134` and domain `windowsServer.gomycode.com` for testing.
- Created sample traffic for analysis, including authentication attempts.

---

## Process and Implementation

### Step 1: IP Address Identification

- On Windows Server, ran `ipconfig` to retrieve the IP address.
- On Debian, used `ifconfig` or `ip addr` to identify the IP address.
- On Kali Linux, executed `ip addr` to confirm the IP address.
- Documented IPs for use in scanning and connectivity tests.

### Step 2: Port Scanning with Nmap

- Ran Nmap on Kali Linux to scan the Windows and Debian VMs:  
  ```sh
  nmap -sV 172.16.103.134
  ```
- Identified open ports and services (e.g., HTTP on port 80 for Windows Server).
- Noted potential vulnerabilities based on service versions.

### Step 3: DNS Resolution

- Used `nslookup` to find the FQDN of `3.33.130.190`:
  ```sh
  nslookup 3.33.130.190
  ```
- Attempted to resolve the FQDN of `172.16.103.134` using `dig`:
  ```sh
  dig 172.16.103.134
  ```
- Noted that `windowsServer.gomycode.com` was not a registered subdomain, indicating a DNS configuration issue.

### Step 4: Connectivity Verification

- Pinged `172.16.103.134` from Kali Linux to confirm reachability:
  ```sh
  ping 172.16.103.134
  ```
- Attempted to ping `debianGomycode.gomycode.com` to verify DNS resolution.
- Used `curl -I windowsServer.gomycode.com` to check the web server, expecting Microsoft IIS/10.0.

### Step 5: IIS Configuration

- On Windows Server, accessed IIS Manager via Tools > Internet Information Services (IIS).
- Navigated to the FTP section, disabled Anonymous Authentication, and enabled Basic Authentication.
- Refreshed `windowsServer.gomycode.com` in Firefox on Kali Linux, noting access issues due to the unregistered subdomain.

### Step 6: Network Traffic Analysis

- On Kali Linux, sniffed traffic to `windowsServer.gomycode.com` using:
  ```sh
  sudo tcpdump -vv dst windowsServer.gomycode.com and port www -w auth.txt
  ```
- Reloaded the website in Firefox, attempting login with incorrect credentials (admin/password).
- Stopped tcpdump with Ctrl+C.
- Attempted to analyze `auth.txt` in Wireshark but encountered a “file not found” error, likely due to incorrect file path or capture failure.
- Inspected GET requests in Wireshark (when successful) to identify credentials.

---

## Challenges and Solutions

- **Challenge:** `auth.txt` file not found when loading in Wireshark.  
  **Solution:** Verified tcpdump output path and re-ran the capture, ensuring the file was saved correctly. Researched correct syntax for tcpdump filters.

- **Challenge:** `windowsServer.gomycode.com` was not accessible due to unregistered subdomain.  
  **Solution:** Used IP address (`172.16.103.134`) directly for testing and noted DNS configuration as a learning point.

- **Challenge:** Interpreting Nmap results to identify vulnerabilities.  
  **Solution:** Referenced Nmap documentation and TryHackMe’s network scanning rooms to understand service versions and potential risks.

---

## Results and Outcomes

- Successfully identified IP addresses of Kali Linux, Windows, and Debian VMs.
- Discovered open ports and services using Nmap, confirming IIS on Windows Server.
- Attempted FQDN resolution, learning about DNS limitations when subdomains are unregistered.
- Configured IIS authentication settings, demonstrating system administration skills.
- Captured network traffic with tcpdump, though faced issues with `auth.txt` analysis in Wireshark.
- Gained hands-on experience with network reconnaissance and traffic analysis, critical for cybersecurity roles.

---

## Screenshots of tool outputs and interfaces

[Network Reconnaissance and Traffic Analysis Screenshots](https://docs.google.com/document/d/1TLfSUleLsSJj_wgJZfZ6kbn7wPigsr8i_qgvfXp-ThY/edit?usp=sharing)

- Image 1: `ipconfig` output on Windows Server showing IP address.
- Image 2: `ifconfig` or `ip addr` output on Debian.
- Image 3: `ip addr` output on Kali Linux.
- Image 4: Nmap scan results for `172.16.103.134`.
- Image 5: `nslookup 3.33.130.190` output.
- Image 6: `dig 172.16.103.134` output.
- Image 7: `ping 172.16.103.134` results.
- Image 8: `curl -I windowsServer.gomycode.com` output showing IIS/10.0.
- Image 9: Firefox attempt to access `windowsServer.gomycode.com`.
- Image 10: IIS Manager interface on Windows Server.
- Image 11: IIS FTP authentication settings (disabling Anonymous, enabling Basic).
- Image 12: `tcpdump` command execution on Kali Linux.
- Image 13: Wireshark interface showing:
- Attempt to open `auth.txt`
- GET request with credential analysis
- Error message for `auth.txt` not found in Wireshark

---

## Lessons Learned

- Mastered IP address identification across multiple OS, essential for network mapping.
- Gained proficiency in Nmap for port scanning and service enumeration.
- Understood DNS resolution challenges with unregistered subdomains.
- Learned to configure IIS for secure authentication, a key system administration skill.
- Developed skills in network traffic analysis with tcpdump and Wireshark, despite file access issues.
- Improved troubleshooting abilities by resolving tool errors and researching documentation.

---

## Relevance to Cybersecurity

This project mirrors real-world network reconnaissance tasks performed by cybersecurity engineers, such as mapping network infrastructure, identifying vulnerabilities, and analyzing traffic for security incidents. These skills are critical for defensive roles (e.g., SOC analyst) and offensive roles (e.g., penetration tester), aligning with my goal of becoming a cybersecurity engineer in industries like oil and gas, where network security is vital.

---

## Future Improvements

- Resolve `auth.txt` issue by automating tcpdump captures with a script.
- Simulate a full penetration test using Metasploit to exploit identified open ports.
- Integrate with a SIEM tool like Splunk to analyze captured traffic.
- Practice on TryHackMe’s network security rooms to deepen reconnaissance skills.

---

## How to Run

1. Set up Kali Linux, Windows Server, and Debian VMs in VirtualBox.
2. Identify IP addresses using `ipconfig`, `ifconfig`, or `ip addr`.
3. Run `nmap -sV <IP>` to scan for open ports.
4. Use `nslookup` and `dig` for FQDN resolution.
5. Configure IIS on Windows Server to enable Basic Authentication.
6. Capture traffic with tcpdump and analyze in Wireshark.

---

> Project completed as part of GoMyCode’s cybersecurity training  
> **Author:** Jeremiah Dighomanor (Digho007)
