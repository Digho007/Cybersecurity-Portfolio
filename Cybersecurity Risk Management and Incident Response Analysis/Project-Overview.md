# Cybersecurity Risk Management and Incident Response Analysis

## Project Overview

This project, completed during my GoMyCode cybersecurity training, analyzes a major cybersecurity incident at a multinational technology organization caused by inadequate risk management and weak Identity and Access Management (IAM) controls. I identified vulnerabilities that enabled an insider threat and a Distributed Denial-of-Service (DDoS) attack, proposing a comprehensive strategy to mitigate risks, enhance incident response, and ensure compliance. This project showcases my skills in risk assessment, incident response, and cybersecurity governance, critical for roles like cybersecurity engineer or SOC analyst in the technology sector.

---

## Objectives

- Identify weaknesses in the organization’s risk management strategy.
- Analyze how weak IAM controls enabled the insider threat and propose improvements.
- Outline steps to strengthen the incident response plan.
- Recommend forensic investigation techniques to understand the attack’s scope.
- Propose a risk assessment strategy to prevent future incidents.
- Suggest controls for insider threats and DDoS protection strategies.
- Address regulatory compliance failures and propose an employee awareness program.
- Detail immediate and long-term actions as a CISO post-incident.

---

## Context

A multinational technology organization suffered a cybersecurity incident due to a poorly maintained IAM system. A disgruntled employee exploited weak access controls to gain unauthorized administrative privileges, exfiltrated sensitive data, and launched a DDoS attack. The lack of an incident response plan and forensic strategy delayed mitigation, leading to financial losses, reputational damage, and regulatory penalties. This case highlights the need for robust risk management and governance.

---

## Analysis

### Primary Weaknesses

The incident was enabled by:

- **Inadequate IAM:** Weak access controls allowed privilege escalation.
- **Lack of Monitoring:** No real-time detection of suspicious behavior.
- **No Incident Response Plan:** Delayed detection and response.
- **Neglected Risk Assessments:** Insider threats were not prioritized.
- **No Forensic Readiness:** Limited ability to investigate the attack.

### IAM and Insider Threats

- **Contribution:** Weak IAM allowed unauthorized privilege escalation and lacked role-based controls.
- **Improvements:**
  - Implement Role-Based Access Control (RBAC) and Least Privilege.
  - Enforce Multi-Factor Authentication (MFA) for administrative access.
  - Conduct regular account audits.
  - Deploy User and Entity Behavior Analytics (UEBA) for anomaly detection.

### Incident Response Plan

Strengthen the plan with:

- Defined roles for an Incident Response Team (IRT).
- Incident classification for prioritization.
- 24/7 monitoring with SIEM tools (e.g., Splunk, Microsoft Sentinel).
- Forensic analysis protocols.
- Regular tabletop exercises.

### Forensic Investigation Techniques

- Log Analysis: Review IAM, firewall, system, and application logs.
- Network Forensics: Analyze packet captures and DDoS traffic with tools like Wireshark.
- Endpoint Forensics: Use FTK or EnCase to examine compromised systems.
- Timeline Analysis: Reconstruct attack events.
- Data Recovery: Retrieve altered or deleted files.

---

## Recommendations

### Risk Assessment Strategy

- Conduct regular risk assessments and threat modeling.
- Maintain a risk register to track vulnerabilities.
- Adopt NIST RMF or ISO/IEC 27005 frameworks.
- Evaluate internal and external threats continuously.
- Include third-party risk assessments.

### Insider Threat Controls

- Implement strict IAM with RBAC and activity monitoring.
- Enforce segregation of duties and regular access reviews.
- Deploy Data Loss Prevention (DLP) tools to block unauthorized data transfers.
- Use UEBA for behavioral monitoring.
- Establish exit protocols for immediate access revocation.

### DDoS Protection Strategies

- Deploy Web Application Firewalls (WAF) and Content Delivery Networks (CDNs) like Cloudflare.
- Use rate-limiting and traffic shaping.
- Partner with DDoS mitigation providers (e.g., Akamai, AWS Shield).
- Implement redundant infrastructure and auto-scaling.
- Monitor with Network Intrusion Detection Systems (NIDS).

### Regulatory Compliance

- Conduct a compliance gap analysis.
- Align with GDPR, HIPAA, or SOX standards.
- Document policies and audit controls.
- Train staff on compliance responsibilities.
- Strengthen the Data Protection Officer (DPO) role.

### Employee Awareness Program

- Monthly training on phishing, social engineering, and secure practices.
- Simulated phishing exercises to test awareness.
- Cybersecurity onboarding for new hires.
- Use posters, videos, and newsletters for reinforcement.
- Offer incentives for reporting suspicious behavior.

### CISO Actions

**Immediate:**
- Isolate affected systems and block malicious access.
- Launch forensic investigation.
- Notify legal, PR, and compliance teams.
- Inform stakeholders and regulators.
- Conduct a post-incident review.

**Long-term:**
- Redesign IAM with RBAC and MFA.
- Develop robust incident response and disaster recovery plans.
- Invest in SIEM, EDR, and DLP technologies.
- Conduct red team/blue team exercises.
- Foster a security culture through training.

---

## Challenges and Solutions

- **Challenge:** Understanding complex IAM configurations for RBAC and UEBA.  
  **Solution:** Studied IAM best practices via GoMyCode and NIST resources.
- **Challenge:** Balancing compliance with operational efficiency.  
  **Solution:** Proposed automated compliance checks and streamlined policies.
- **Challenge:** Designing a practical employee training program.  
  **Solution:** Incorporated gamification and simulations for engagement.

---

## Results and Outcomes

- Identified critical weaknesses in risk management and IAM.
- Proposed a comprehensive strategy for incident response, insider threat mitigation, and DDoS protection.
- Recommended compliance measures to meet industry standards.
- Developed an employee training program to reduce human-related risks.
- Outlined actionable CISO steps for immediate and long-term recovery.

---

## Lessons Learned

- Gained expertise in risk assessment and threat modeling.
- Learned the importance of IAM and continuous monitoring in preventing insider threats.
- Understood DDoS mitigation and compliance requirements.
- Developed skills in designing incident response and training programs.

---

## Relevance to Cybersecurity

This project mirrors real-world risk management and incident response tasks in the technology sector. Skills like IAM implementation, forensic analysis, and compliance are critical for cybersecurity engineers and SOC analysts, ensuring robust protection against insider threats and service disruptions.

---

## Future Improvements

- Simulate the incident in a TryHackMe lab (e.g., IAM or incident response rooms).
- Implement a mock SIEM dashboard using Splunk to visualize alerts.
- Develop a Python script for automated log analysis.
- Conduct a mock compliance audit to test proposed controls.

---

## How to Run

1. Review the incident scenario and weaknesses.
2. Study the proposed strategies for risk management and incident response.
3. Create diagrams using tools like Draw.io to visualize the attack and solutions.
4. Optionally, simulate the scenario in a TryHackMe lab to test recommendations.

---

> Project completed as part of GoMyCode’s cybersecurity training  
> **Author:** Jeremiah Dighomanor (Digho007)
