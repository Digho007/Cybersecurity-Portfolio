# Malicious Script Analysis for Incident Response

## Project Overview

This project, completed during my GoMyCode cybersecurity training, focuses on analyzing two suspicious scripts (**Defeat.bat** and **rev.py**) to support incident response. I examined a batch script that downloads and executes malware and a Python reverse shell that grants attackers remote access. Using tools like Windows Defender, Notepad, and theoretical applications of Wireshark and netstat, I identified malicious behaviors and recommended detection methods. This project showcases my skills in threat detection, script analysis, and incident response, critical for roles like SOC analyst or cybersecurity engineer.

---

## Objectives

- Analyze Defeat.bat to identify its malicious actions and assess Windows Defender’s detection capabilities.
- Examine rev.py to determine its functionality, attacker’s IP, and communication port.
- Recommend detection and mitigation strategies for both scripts.
- Decide whether the scripts warrant escalation to senior incident response analysts.
- Demonstrate proficiency in incident response and threat analysis.

---

## Tools and Technologies

- **Operating System:** Windows Server (username: Administrator, password: Gomycode01*)
- **Tools:** Windows Defender, Notepad, Wireshark (theoretical), netstat, Sysinternals Process Explorer (theoretical), Endpoint Detection and Response (EDR, theoretical)
- **Environment:** VirtualBox VM provided by GoMyCode
- **Resources:** GoMyCode Learn platform

---

## Project Setup

### Environment Configuration

- Set up a Windows Server VM provided by GoMyCode.
- Ensured Windows Defender was active with real-time protection enabled.

### Script Acquisition

- Copied Defeat.bat and a folder containing rev.py to the Windows Server.
- Opened scripts in Notepad for manual analysis.

### Analysis Tools

- Used Windows Defender to scan Defeat.bat.
- Prepared to monitor network traffic and processes with Wireshark and netstat for rev.py.

---

## Process and Implementation

### Step 1: Analyzing Defeat.bat

#### Script Review

- Opened Defeat.bat in Notepad to examine its code.
- Identified that it:
  - Prompts for a malware download link.
  - Uses BITSAdmin to retrieve a malicious file (e.g., Winupdate.exe).
  - Saves the file to the Startup folder for persistence.
  - Executes the file using PowerShell.

#### Windows Defender Scan

- Scanned Defeat.bat with Windows Defender.
- Noted that Defender may not detect it due to its use of legitimate tools (BITSAdmin, PowerShell), which can bypass signature-based detection.
- Recognized the risk of fileless malware in the second folder, potentially using obfuscated or memory-based scripts.

#### Recommendations

- Enable advanced logging in Microsoft Defender for Endpoint.
- Use Sysinternals Process Explorer to monitor suspicious processes.
- Deploy EDR solutions for behavior-based detection.

---

### Step 2: Analyzing rev.py

#### Script Review

- Identified rev.py as a Python script implementing a reverse shell.
- Determined its functionality:
  - Connects to an attacker’s IP (**192.168.2.192**) on port **4444**.
  - Redirects system input, output, and error streams to the attacker.
  - Launches a bash shell, granting full remote control.

#### Detection Strategies

- Monitor outgoing connections with:
  ```sh
  netstat -antp
  ```
  to identify connections to 192.168.2.192:4444.
- Use Wireshark to capture suspicious network traffic.
- Configure a firewall to block unknown outbound traffic.
- Scan running processes to detect unauthorized shells.
- Deploy EDR to identify malicious behavior.

---

### Step 3: Escalation Decision

- **Assessment:**
  - **Defeat.bat:** High risk due to malware download, persistence, and potential evasion of antivirus. Warrants escalation to senior analysts for further investigation.
  - **rev.py:** Critical threat due to remote access capabilities, requiring immediate escalation to isolate the system and analyze network traffic.
- **Rationale:** Both scripts exhibit malicious intent (malware delivery and remote control), posing significant risks to system integrity and network security.

---

## Challenges and Solutions

- **Challenge:** Windows Defender failed to detect Defeat.bat due to its use of legitimate tools.  
  **Solution:** Researched evasion techniques and recommended behavior-based detection tools like EDR.
- **Challenge:** Limited access to Wireshark and netstat in the VM environment for real-time analysis.  
  **Solution:** Studied theoretical usage of these tools via TryHackMe and online resources.
- **Challenge:** Understanding complex script behaviors (e.g., fileless malware, reverse shells).  
  **Solution:** Analyzed scripts in Notepad and referenced Python/Batch scripting guides.

---

## Results and Outcomes

- Identified Defeat.bat as a malware delivery script with persistence mechanisms, recommending advanced detection methods.
- Confirmed rev.py as a reverse shell connecting to **192.168.2.192:4444**, with actionable detection strategies.
- Escalated both scripts to senior analysts due to their high-risk nature.
- Produced screenshots of script analysis and tool outputs for documentation.
- Gained expertise in incident response and threat analysis.

---

## Screenshots of script analysis and tool outputs

[Malicious Script Analysis for Incident Response – Screenshots](https://docs.google.com/document/d/1elQZk3eFbiTFhubtPBefFobviHu4EiHGFil6umpkToc/edit?usp=sharing)

- Image 1: Defeat.bat script opened in Notepad.
- Image 2: Windows Defender scan results for Defeat.bat.
- Image 3: rev.py script contents in Notepad or Python editor.

---

## Lessons Learned

- Gained proficiency in analyzing batch and Python scripts for malicious behavior.
- Learned about malware evasion techniques, including fileless attacks and legitimate tool misuse.
- Understood the importance of behavior-based detection tools like EDR.
- Developed skills in incident response decision-making and escalation processes.

---

## Relevance to Cybersecurity

This project mirrors real-world incident response tasks, such as analyzing suspicious scripts and determining escalation needs. These skills are critical for SOC analysts and cybersecurity engineers, particularly in industries like oil and gas, where rapid threat detection is essential to protect critical infrastructure.

---

## Future Improvements

- Implement real-time traffic analysis with Wireshark to detect rev.py connections.
- Test EDR tools like Microsoft Defender for Endpoint in a lab environment.
- Practice analyzing more complex scripts (e.g., obfuscated PowerShell) on TryHackMe.
- Develop automated script analysis tools using Python.

---

## How to Run

1. Set up a Windows Server VM with Windows Defender enabled.
2. Copy Defeat.bat and rev.py to the server.
3. Analyze Defeat.bat using Notepad and Windows Defender.
4. Review rev.py in a text editor and simulate detection with netstat or Wireshark.
5. Document findings and escalate as needed.

---

> Project completed as part of GoMyCode’s cybersecurity training  
> **Author:** Jeremiah Dighomanor (Digho007)
