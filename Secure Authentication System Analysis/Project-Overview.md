# Secure Authentication System Analysis

## Project Overview

This project, completed during my GoMyCode cybersecurity training, analyzes a security breach at SecureBank, a fictional financial organization, caused by vulnerabilities in its password-based authentication system. I identified the flaws that enabled phishing, brute force, credential stuffing, and session hijacking attacks, and proposed a multi-layered cybersecurity strategy to mitigate future risks. This project showcases my skills in threat analysis, secure system design, and incident response, critical for roles like SOC analyst or cybersecurity engineer in the financial sector.

---

## Objectives

- Identify security flaws in SecureBank’s authentication system that enabled the breach.
- Analyze the attack methods used (phishing, brute force, credential stuffing, session hijacking) and propose prevention strategies.
- Explain the critical role of two-factor authentication (2FA) in preventing the compromise.
- Develop a cybersecurity resilience strategy to limit attack impact.
- Recommend secure authentication mechanisms and employee training to reduce risks.
- Outline compliance measures to align with industry standards post-breach.

---

## Context

SecureBank, operating in the financial sector, relied on a password-based authentication system for internal services and customer accounts. A hacker exploited vulnerabilities through:

- A phishing campaign tricking employees into entering credentials on a fake login page.
- Brute force and credential-stuffing attacks to access accounts.
- Poor session management, allowing prolonged unauthorized access.

The breach resulted in significant data loss (customer information) and fraudulent transactions, highlighting the need for improved security controls.

---

## Analysis

### Security Flaws

The breach was enabled by:

- **Weak Authentication Controls:** Lack of 2FA meant stolen passwords were sufficient for access.
- **Phishing Susceptibility:** No phishing-resistant authentication (e.g., FIDO2) or employee training.
- **Poor Credential Security:** No protections against brute force or credential stuffing, such as account lockouts or rate limiting.
- **Inadequate Session Management:** Long-lived sessions allowed attackers to maintain access.
- **Lack of Threat Detection:** No monitoring or alerting for suspicious login attempts.

### Attack Methods and Prevention

**Phishing:**  
- *Method:* Employees entered credentials on a fake website mimicking SecureBank’s login page.  
- *Prevention:* Deploy email security (SPF, DKIM, DMARC), train employees on phishing awareness, and use phishing-resistant authentication (FIDO2, passkeys).

**Brute Force Attack:**  
- *Method:* Repeated password guesses to gain access.  
- *Prevention:* Implement account lockouts (e.g., after 3 failed attempts), enforce complex passwords, and use rate limiting.

**Credential Stuffing:**  
- *Method:* Used stolen credentials from other breaches.  
- *Prevention:* Enable 2FA, monitor for logins from unusual locations, and check credentials against leaked databases (e.g., Have I Been Pwned).

**Session Hijacking:**  
- *Method:* Exploited poor session management for prolonged access.  
- *Prevention:* Use short-lived tokens, auto-logout inactive sessions, and require re-authentication for sensitive actions.

---

## Impact of Lacking 2FA

Without 2FA:

- Stolen passwords provided immediate access, bypassing additional verification.
- Reused passwords from other breaches were exploitable without a second factor (e.g., OTP, biometrics).
- Attackers maintained persistent access due to the absence of session re-authentication.

2FA would have required a second verification step, significantly reducing the risk of unauthorized access.

---

## Recommendations

### Cybersecurity Resilience Strategy

To minimize future attack impact, SecureBank should:

- **Enable Multi-Factor Authentication (MFA):** Require 2FA (e.g., OTPs, security keys) for all logins.
- **Improve Phishing Defenses:** Deploy email filtering and conduct regular phishing awareness training.
- **Implement Zero Trust Security:** Use continuous authentication and restrict access based on user behavior and device trust.
- **Enhance Monitoring & Detection:** Deploy SIEM tools (e.g., Splunk, Microsoft Sentinel) to detect anomalies like unusual logins.
- **Enforce Strong Password Policies:** Require unique, complex passwords and promote password managers.
- **Deploy Endpoint Detection & Response (EDR):** Monitor for malware and credential theft tools.

### Secure Authentication Mechanisms

- **FIDO2/WebAuthn:** Uses hardware security keys or biometrics for phishing-resistant authentication.
- **Passkeys:** Implements passwordless authentication tied to user devices.
- **Adaptive Authentication:** Analyzes login risk (e.g., IP, device, behavior) and blocks suspicious attempts.

### Employee Training & Awareness

- Train employees to recognize phishing emails and fake login pages.
- Emphasize the importance of unique passwords and password managers.
- Teach how to report suspicious emails promptly.
- Conduct regular simulated phishing exercises to reinforce training.

### Compliance with Cybersecurity Standards

Post-breach, SecureBank should align with:

- **NIST Cybersecurity Framework:** Follow Identify, Protect, Detect, Respond, Recover phases.
- **ISO 27001:** Implement information security management best practices.
- **PCI-DSS:** Ensure encryption and authentication controls for payment data.
- **GDPR/CCPA:** Notify affected customers and regulators as required.

---

## Challenges and Solutions

- **Challenge:** Limited employee awareness of phishing risks.  
  **Solution:** Developed a training plan with simulated phishing exercises, referencing GoMyCode’s Learn platform.
- **Challenge:** Balancing security with usability (e.g., 2FA complexity).  
  **Solution:** Recommended user-friendly 2FA options like passkeys and biometrics.
- **Challenge:** Understanding compliance requirements (e.g., GDPR, PCI-DSS).  
  **Solution:** Researched standards via NIST and PCI Security Standards Council resources.

---

## Results and Outcomes

- Identified critical flaws in SecureBank’s authentication system, explaining their role in the breach.
- Proposed a comprehensive cybersecurity strategy, including 2FA, Zero Trust, and SIEM.
- Recommended advanced authentication mechanisms (FIDO2, passkeys) to prevent future compromises.
- Developed an employee training plan to reduce phishing risks.
- Outlined compliance measures to meet industry standards, ensuring regulatory alignment.

---

## Lessons Learned

- Gained expertise in analyzing authentication vulnerabilities and attack vectors.
- Learned the importance of 2FA and Zero Trust in securing systems.
- Understood the role of employee training in mitigating phishing risks.
- Developed knowledge of cybersecurity standards (NIST, ISO 27001, PCI-DSS) for compliance.

---

## Relevance to Cybersecurity

This project mirrors real-world incident response and secure system design tasks in the financial sector. Analyzing breaches and designing mitigation strategies are critical for SOC analysts and cybersecurity engineers, ensuring robust protection of sensitive data and compliance with regulations.

---

## Future Improvements

- Simulate the breach in a lab (e.g., TryHackMe phishing rooms) to test proposed solutions.
- Implement a mock SIEM dashboard using Splunk to visualize anomaly detection.
- Develop a phishing simulation tool in Python to train employees.
- Explore advanced authentication protocols (e.g., OAuth 2.0) for deeper understanding.

---

> Project completed as part of GoMyCode’s cybersecurity training  
> **Author:** Jeremiah Dighomanor (Digho007)
