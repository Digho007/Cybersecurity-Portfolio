# Active Directory Hardening for IT Security

## Project Overview

This project, completed during my GoMyCode cybersecurity training, focuses on hardening administrator accounts and workstations in a Windows Server environment using Active Directory and Group Policy. I created a fine-grained password policy for IT staff accounts and configured a Group Policy Object (GPO) to secure IT workstations, implementing settings like disabling Guest Accounts and renaming Administrator Accounts. This project showcases my skills in Windows system administration and defensive cybersecurity, critical for roles like SOC analyst or cybersecurity engineer in industries such as oil and gas.

---

## Objectives

- Create a global security group for IT staff in Active Directory.
- Implement a fine-grained password policy with strict security settings for IT staff accounts.
- Configure a GPO to harden IT workstations by disabling Guest Accounts, renaming Administrator Accounts, and hiding last user names during logon.
- Link the GPO to an Organizational Unit (OU) containing IT computer accounts.
- Demonstrate proficiency in Active Directory and Group Policy for system security.

---

## Tools and Technologies

- **Operating System:** Windows Server (GoMyCode-provided VM)
- **Tools:** Active Directory Users and Computers, Active Directory Administrative Center, Group Policy Management (gpmc.msc)
- **Resources:** GoMyCode Learn platform, YouTube tutorials
- **Environment:** VirtualBox VM

---

## Project Setup

### Environment Configuration

- Set up a Windows Server VM provided by GoMyCode.
- Ensured Active Directory Domain Services were installed and configured.

### Access Tools

- Launched Server Manager to access Active Directory Users and Computers, Active Directory Administrative Center, and Group Policy Management.

### Test Environment

- Created a test OU for IT computer accounts to apply the GPO.
- Used a global security group (GOMYCODEstaff) for password policy application.

---

## Process and Implementation

### Step 1: Creating the IT Staff Group

- Opened Active Directory Users and Computers from Server Manager > Tools.
- Navigated to the Users container, right-clicked, and selected New > Group.
- Named the group **GOMYCODEstaff**, set Group scope to Global, and Group type to Security.
- Confirmed creation, ensuring the group was ready for password policy application.

### Step 2: Configuring Fine-Grained Password Policy

- Launched Active Directory Administrative Center and navigated to gomycode (local) > System > Password Settings.
- Right-clicked in the Password Settings area and selected New > Password Settings.
- Configured the policy with:
  - Minimum password length: 20 characters
  - Password complexity: Enabled
  - Password history: 24 passwords remembered
  - Minimum password age: 1 day
  - Maximum password age: 30 days
  - Account lockout threshold: 3 failed login attempts
  - Account lockout duration: 20 minutes
  - Reset failed attempts after: 10 minutes
- Added **GOMYCODEstaff** to the policy by clicking Add, entering the group name, and confirming.
- Verified the policy was applied under gomycode (local).

### Step 3: Hardening Workstations with Group Policy

- Opened Group Policy Management (gpmc.msc) from Server Manager.
- Navigated to Group Policy Objects, right-clicked, and created a new GPO named **SecureAdminWorkstation**.
- Right-clicked SecureAdminWorkstation and selected Edit.
- In the Group Policy Management Editor, navigated to:  
  `Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options`
- Applied the following settings:
  - Disabled the Guest Account.
  - Renamed the Administrator Account to a custom name.
  - Enabled the policy "Interactive logon: Do not display last user name".
- Closed the editor and linked the GPO to the IT OU by right-clicking the OU, selecting Link an Existing GPO, and choosing SecureAdminWorkstation.

---

## Challenges and Solutions

- **Challenge:** Navigating Active Directory interfaces was initially complex due to unfamiliarity.  
  **Solution:** Watched YouTube tutorials and referenced GoMyCode’s Learn platform to understand tool navigation.
- **Challenge:** Ensuring the GPO applied correctly to the IT OU without affecting other systems.  
  **Solution:** Tested the GPO on a single test computer in the OU and verified settings via `gpresult /r`.
- **Challenge:** Understanding fine-grained password policy precedence over Default Domain Policy.  
  **Solution:** Researched Microsoft documentation to confirm policy application to specific groups.

---

## Results and Outcomes

- Successfully created and configured the **GOMYCODEstaff** global security group.
- Implemented a fine-grained password policy, enforcing strict security for IT staff accounts.
- Configured and linked the **SecureAdminWorkstation** GPO, hardening IT workstations against unauthorized access.
- Verified policy application using Active Directory tools, ensuring compliance with security requirements.
- Produced screenshots of each step, documenting the process for transparency.

---

## Screenshots of each step

[Active Directory Hardening for IT Security - Screenshots](https://docs.google.com/document/d/1yRdx3ws-AeSnZ-tIisQkl72ywGzmFamo5DfTSD5R8yc/edit?usp=sharing)

- Image 1: Active Directory Users and Computers showing GOMYCODEstaff group creation.
- Image 2: Group properties for GOMYCODEstaff (Global, Security).
- Image 3: Active Directory Administrative Center navigation to Password Settings.
- Image 4: New Password Settings creation interface.
- Image 5: Password policy settings (20 characters, complexity enabled, etc.).
- Image 6: Adding GOMYCODEstaff to the password policy.
- Image 7: Confirmation of password policy in gomycode (local).
- Image 8: Group Policy Management showing SecureAdminWorkstation creation.
- Image 9: GPO Editor with Security Options settings.
- Image 10: Guest Account disabled in GPO settings.
- Image 11: Renamed Administrator Account in GPO settings.
- Image 12: Enabled “Do not display last user name” policy.

---

## Lessons Learned

- Gained proficiency in Active Directory for group and policy management.
- Mastered fine-grained password policies to enhance account security.
- Learned Group Policy configuration to harden workstations, reducing attack surfaces.
- Improved understanding of Windows Server administration for cybersecurity.
- Developed documentation skills for clear, professional presentation.

---

## Relevance to Cybersecurity

This project mirrors real-world defensive cybersecurity tasks, such as securing user accounts and systems in a corporate environment. Hardening administrator accounts and workstations is critical for preventing unauthorized access and mitigating risks like brute-force attacks. These skills are essential for SOC analysts and cybersecurity engineers, particularly in industries like oil and gas, where secure IT infrastructure is vital.

---

## Future Improvements

- Test policy enforcement by simulating login attempts to verify lockout settings.
- Integrate with a SIEM tool like Splunk to monitor policy violations.
- Expand to include additional GPO settings, such as firewall rules or software restrictions.
- Practice on TryHackMe’s Active Directory rooms to deepen expertise.

---

## How to Run

1. Set up a Windows Server VM with Active Directory Domain Services.
2. Access Active Directory Users and Computers to create the **GOMYCODEstaff** group.
3. Use Active Directory Administrative Center to configure the fine-grained password policy.
4. Create and link the **SecureAdminWorkstation** GPO using Group Policy Management.
5. Verify settings with `gpresult /r` on a test workstation in the IT OU.

---

> Project completed as part of GoMyCode’s cybersecurity training  
> **Author:** Jeremiah Dighomanor (Digho007)
