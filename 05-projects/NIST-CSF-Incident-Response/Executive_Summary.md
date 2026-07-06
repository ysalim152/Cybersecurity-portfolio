# Executive Summary

**Project:** Incident Response Using the NIST Cybersecurity Framework (CSF)  
**Author:** Salim Younsi  
**Role:** Junior Cybersecurity Analyst (Portfolio Project)  
**Date:** July 2026

---

# Purpose

This report provides a high-level summary of a simulated cybersecurity incident involving a **Denial-of-Service (DoS)** attack against a multimedia company's internal network. The analysis follows the **NIST Cybersecurity Framework (CSF)** to assess the incident, evaluate its business impact, and recommend security improvements.

---

# Incident Overview

The organization experienced a network outage caused by an **ICMP Flood DoS attack**. A threat actor exploited a misconfigured firewall, allowing excessive ICMP traffic to overwhelm network resources.

As a result, employees temporarily lost access to internal services, affecting business operations for approximately **two hours**.

The incident response team successfully contained the attack by blocking malicious ICMP traffic, restoring critical services, and initiating a post-incident investigation.

---

# Business Impact

The attack primarily affected the **availability** of the organization's services.

### Operational Impact

- Internal network services became unavailable.
- Employees were unable to access business resources.
- Business productivity decreased during the outage.
- Incident response resources were required to restore operations.

### Security Impact

The investigation found **no evidence of data theft or unauthorized access**. The incident was limited to a disruption of service availability.

---

# Root Cause Analysis

The primary cause of the incident was an improperly configured firewall that allowed unrestricted ICMP traffic from external sources.

Contributing factors included:

- Missing ICMP rate limiting
- Insufficient firewall hardening
- Limited network traffic monitoring
- Absence of automated anomaly detection

---

# Actions Taken

The cybersecurity team implemented immediate containment measures to restore normal operations.

Key actions included:

- Blocking incoming ICMP traffic
- Applying ICMP rate limiting
- Updating firewall security rules
- Deploying continuous network monitoring
- Implementing IDS/IPS capabilities

These actions successfully restored network availability and reduced the likelihood of similar attacks.

---

# NIST Cybersecurity Framework Assessment

The incident was analyzed using the five functions of the NIST Cybersecurity Framework.

| Function | Summary |
|----------|---------|
| Identify | Determined affected assets, vulnerabilities, and business impact |
| Protect | Improved firewall configuration and network hardening |
| Detect | Enhanced monitoring and intrusion detection capabilities |
| Respond | Contained the attack and restored critical services |
| Recover | Returned systems to normal operation and documented lessons learned |

---

# Recommendations

To further improve the organization's cybersecurity posture, the following actions are recommended:

- Perform regular firewall configuration reviews.
- Implement continuous vulnerability management.
- Deploy centralized log collection and analysis.
- Establish baseline network traffic monitoring.
- Conduct periodic incident response exercises.
- Provide cybersecurity awareness training to employees.
- Review and update incident response procedures regularly.

---

# Conclusion

This project demonstrates the practical application of the **NIST Cybersecurity Framework** to a simulated Denial-of-Service incident.

The structured analysis highlights the importance of proactive security controls, effective incident response, and continuous monitoring in protecting organizational assets.

Applying the NIST CSF enabled the organization to identify weaknesses, implement corrective actions, and improve its overall cybersecurity resilience.

---

**Prepared by**

**Salim Younsi**

Junior Cybersecurity Analyst Portfolio

Google Cybersecurity Professional Certificate