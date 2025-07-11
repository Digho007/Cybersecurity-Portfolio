# Linux Log Analysis for Cybersecurity Monitoring

## Project Overview

This project, completed as part of my GoMyCode cybersecurity training, demonstrates foundational skills in Linux command-line operations and system log analysis for cybersecurity monitoring. By working with Linux commands and regular expressions, I explored how to manage and analyze system logs to identify potential security events, such as unauthorized access attempts. This project highlights my ability to use tools like `grep`, `journalctl`, and `logger` to monitor and secure systems—critical skills for SOC analyst or cybersecurity engineer roles.

## Objectives

- Learn and apply Linux commands (`ls`, `cat`, `head`, `tail`) to navigate and inspect files.
- Use `logger` and `journalctl` to create and monitor system logs, simulating real-world log analysis tasks.
- Apply regular expressions with `grep` to filter log data, including extracting IP addresses from web server logs.
- Understand the role of log analysis in detecting security incidents.

## Tools and Technologies

- **Operating System:** Linux (Ubuntu/Kali, in VMware)
- **Commands:** `ls`, `cat`, `head`, `tail`, `logger`, `journalctl`, `grep`
- **Regex:** Extended regular expressions (`-E`)
- **Environment:** Kali Linux VM (VMware)

## Project Setup

### Environment Configuration

- Set up a Linux environment (e.g., Ubuntu or Kali in VMware).
- Generate sample log files (`access_log.log`, `webserver.log`) to simulate system and web server logs.

### Log Creation

- Use the `logger` command to add custom log entries to the system journal, simulating events like user logins or errors.
  - Example:  
    ```bash
    logger "Suspicious login attempt detected"
    ```

### Log Analysis

- View live logs using `journalctl -f` to monitor real-time system activity.
- Search logs with `journalctl | grep "Suspicious"` to find specific entries.
- Analyze web server logs using `grep` to extract IP addresses and filter patterns.

## Process and Implementation

### Step 1: Exploring Linux Commands

- `ls`: List files and directories in the working directory.
- `cat access_log.log`: Display the full contents of `access_log.log`.
- `cat -n example.log`: Add line numbers to `example.log`.
- `head webserver.log`: View the first 10 lines.
- `tail webserver.log`: View the last 10 lines.
- Redirect outputs using `>` (overwrite) or `>>` (append).

### Step 2: System Log Management

- Create custom log entries with:  
  ```bash
  logger "Test event: System access granted"
  ```
- Monitor live logs:  
  ```bash
  journalctl -f
  ```
- Search for events:  
  ```bash
  journalctl | grep "Test event"
  ```

### Step 3: Advanced Log Analysis with Grep and Regex

- **Case-Insensitive Search:**  
  ```bash
  grep -i [plc] access_log.log
  ```
- **IP Address Filtering (Extended Regex):**  
  ```bash
  grep -E "[^^][0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" webserver.log
  ```
  - `[^^]`: Ensures the line doesn't start with a caret (`^`).
  - `[0-9]{1,3}`: Matches 1–3 digits for each IP octet.
  - `\.`: Matches literal dots.

## Challenges and Solutions

- **Regex syntax complexity:** Overcame by learning extended regex and practicing on regex101.com.
- **Filtering large files:** Used `head`, `tail`, and `grep` to focus on relevant entries.
- **Understanding workflows:** Researched SOC practices on TryHackMe.

## Results and Outcomes

- Navigated and manipulated log files using Linux commands.
- Created and monitored system logs with `journalctl` and `logger`.
- Mastered `grep` and regex for extracting IP addresses.
- Produced visual evidence (screenshots) of command outputs and log analysis results.

## Screenshots of command outputs and log analysis results
 
[View Screenshots on Google Docs](https://docs.google.com/document/d/1y1L1wWgFXU0ujCno7qAmN8bvQcc8gOoccL2AYSdAKhA/edit?usp=sharing)

- **Image 1:** Output of `ls` showing log files.
- **Image 2:** `cat -n access_log.log` displaying numbered log entries.
- **Image 3:** `journalctl -f` showing live system logs.
- **Image 4:** `grep -i [plc] access_log.log` results.
- **Image 5:** Regex output for IP filtering in `webserver.log`.
- **Image 6:** `logger` command adding a custom log entry.
- **Image 7:** `head webserver.log` (first 10 lines).
- **Image 8:** `tail webserver.log` (last 10 lines).

## Lessons Learned

- Gained confidence in Linux command-line navigation.
- Understood logs’ vital role in tracking and detecting security incidents.
- Developed regex skills for parsing complex data.
- Improved technical documentation and communication.

## Relevance to Cybersecurity

This project mirrors real-world tasks in a Security Operations Center (SOC), where analysts use Linux and log analysis to monitor systems, detect anomalies, and investigate incidents. Skills like `grep` for pattern matching and `journalctl` for log monitoring are directly applicable to SOC analyst or cybersecurity engineer roles.

## Future Improvements

- Expand analysis using tools like Splunk or Wireshark.
- Simulate and analyze real-world attacks.
- Automate log parsing with Python for large datasets.

## How to Run

1. Set up a Linux environment (e.g., Ubuntu or Kali VM).
2. Create or copy sample log files (`access_log.log`, `webserver.log`).
3. Run commands like `cat`, `head`, `tail`, `logger`, and `journalctl` as described above.
4. Use `grep -E` to filter IP addresses from `webserver.log`.

---

> Project completed as part of GoMyCode’s cybersecurity training  
> **Author:** Jeremiah Dighomanor (Digho007)
