# Incident Report: Brute-Force SSH Attack

**Incident ID:** IR-20260303-001
**Date of Report:** March 3, 2026
**Author:** Manus AI

## 1. Executive Summary

On March 3, 2026, a brute-force SSH attack was detected targeting a Linux server within the simulated SOC environment. The attack involved multiple failed login attempts originating from a single external IP address. The Security Information and Event Management (SIEM) system, Wazuh, successfully identified the anomalous activity and generated an alert. Investigation confirmed that the attack was unsuccessful, and no unauthorized access was gained. Immediate mitigation steps included blocking the source IP address and reviewing existing security controls.

## 2. Timeline of Events

| Timestamp (UTC)       | Event Description                                                                 | Source IP         | Destination Host      |
| :-------------------- | :-------------------------------------------------------------------------------- | :---------------- | :-------------------- |
| 2026-03-03 10:00:00   | Start of brute-force SSH attempts detected.                                       | 192.168.56.101    | 192.168.56.102        |
| 2026-03-03 10:01:30   | Wazuh SIEM triggers alert for multiple failed SSH logins (Rule 5720).             | 192.168.56.101    | 192.168.56.102        |
| 2026-03-03 10:02:00   | SOC Analyst begins initial triage and alert analysis.                             | N/A               | N/A                   |
| 2026-03-03 10:05:00   | Brute-force attempts cease.                                                       | 192.168.56.101    | 192.168.56.102        |
| 2026-03-03 10:15:00   | Confirmation of unsuccessful attack; no compromise identified.                    | N/A               | N/A                   |
| 2026-03-03 10:30:00   | Source IP (192.168.56.101) blocked at firewall level.                             | N/A               | N/A                   |

## 3. Technical Analysis

The attack originated from IP address `192.168.56.101` (simulated Kali Linux machine) targeting the SSH service on `192.168.56.102` (simulated Linux server). The attacker utilized a brute-force methodology, attempting numerous username and password combinations. Logs from the target server (e.g., `/var/log/auth.log`) showed a high volume of `Authentication failure` entries. Wazuh successfully correlated these events, exceeding the predefined threshold for failed login attempts and generating a critical alert. Further analysis of the logs confirmed that despite the persistent attempts, no valid credentials were found, and therefore, no unauthorized access was achieved.

## 4. MITRE Mapping

This incident aligns with the following MITRE ATT&CK techniques and tactics:

*   **Tactic:** Credential Access (TA0006)
    *   **Technique:** Brute Force (T1110)
        *   **Description:** The adversary attempted to gain access to accounts by systematically guessing passwords. This was evidenced by the high volume of failed SSH login attempts.

## 5. Impact Assessment

*   **Confidentiality:** No impact. No sensitive data was accessed or exfiltrated as the attack was unsuccessful.
*   **Integrity:** No impact. System configurations or data integrity were not compromised.
*   **Availability:** Minimal impact. The SSH service remained available, although the high volume of failed login attempts could potentially cause minor performance degradation or log flooding. No denial of service was observed.

## 6. Recommendations

Based on the analysis of this incident, the following recommendations are proposed to enhance the security posture:

1.  **Implement Account Lockout Policies:** Configure the target server to temporarily lock user accounts after a specified number of failed login attempts.
2.  **Enforce Strong Password Policies:** Ensure all user accounts have strong, unique passwords that meet complexity requirements.
3.  **Deploy Multi-Factor Authentication (MFA):** Implement MFA for all remote access services, including SSH, to add an additional layer of security.
4.  **Geographic IP Restrictions:** Consider restricting SSH access to only necessary geographic locations.
5.  **Advanced Threat Detection:** Enhance SIEM rules to detect more sophisticated brute-force variants or other credential access techniques.
6.  **Regular Security Audits:** Conduct periodic security audits and penetration testing to identify and remediate vulnerabilities.
7.  **Review Network Segmentation:** Ensure proper network segmentation is in place to limit the blast radius of potential compromises.
