# Alert Analysis: Brute-Force SSH Attack

This document details the analysis of an alert triggered by a simulated brute-force SSH attack. The objective is to provide a clear understanding of the incident, its characteristics, and initial assessment.

## Alert Details

*   **What triggered the alert?**
    The alert was triggered by an excessive number of failed SSH login attempts originating from a single source IP address targeting a specific host within a short timeframe. Wazuh's rules (e.g., `5712` for SSH authentication failures and `5720` for multiple failed attempts) detected this anomalous behavior.

*   **Source IP:** `192.168.56.101` (Example IP of the Kali Linux attacker machine)

*   **Destination Host:** `192.168.56.102` (Example IP of the target Linux server)

*   **Number of failed attempts:** Approximately 150-200 failed login attempts were observed within a 5-minute window.

*   **Timeline of attack:**
    *   **Start Time:** `YYYY-MM-DD HH:MM:SS UTC` (e.g., 2026-03-03 10:00:00 UTC)
    *   **End Time:** `YYYY-MM-DD HH:MM:SS UTC` (e.g., 2026-03-03 10:05:00 UTC)
    *   **Duration:** 5 minutes

*   **Was it successful?**
    No, the brute-force attack was not successful. All attempts resulted in authentication failures, indicating that the attacker did not gain unauthorized access to the target system.

*   **Risk level?**
    **Medium to High.** Although the attack was unsuccessful, brute-force attempts represent a significant threat as they can lead to unauthorized access if successful. The high volume of attempts indicates a persistent attacker. Immediate action is required to block the source IP and review security configurations.
