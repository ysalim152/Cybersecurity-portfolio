# Incident Report

**Project:** NIST CSF Incident Response Case Study  
**Author:** Salim Younsi  
**Role:** Junior Cybersecurity Analyst  
**Date:** July 2026  
**Classification:** Internal Use Only

---

# 1. Executive Overview

On the morning of the incident, the organization experienced a **Denial-of-Service (DoS)** attack that disrupted internal network operations. The attack exploited a firewall configuration weakness, allowing a high volume of **ICMP packets** to flood the network.

The excessive traffic exhausted available network resources, causing a loss of availability for approximately **two hours**.

The Security Operations Center (SOC) identified the attack, initiated containment procedures, restored critical services, and performed a post-incident analysis using the **NIST Cybersecurity Framework (CSF).**

---

# 2. Incident Information

| Field | Value |
|--------|-------|
| Incident ID | IR-2026-001 |
| Incident Type | Denial of Service (DoS) |
| Attack Method | ICMP Flood |
| Severity | High |
| Status | Resolved |
| Duration | Approximately 2 Hours |
| Detection Method | Network Monitoring |
| Framework Used | NIST Cybersecurity Framework |

---

# 3. Environment

The organization provides:

- Website Design Services
- Graphic Design
- Social Media Marketing

Critical assets include:

- Internal Network
- Firewall
- Web Services
- File Servers
- Employee Workstations
- Network Infrastructure

---

# 4. Incident Description

The monitoring system detected an abnormal increase in incoming ICMP traffic originating from multiple external IP addresses.

Within minutes, internal users reported that network services had become unavailable.

Further investigation determined that the firewall was accepting unrestricted ICMP traffic from external networks.

The attacker exploited this weakness to generate a large volume of ICMP Echo Requests, overwhelming network resources and causing service disruption.

---

# 5. Attack Analysis

## Attack Type

Denial of Service (DoS)

### Technique

ICMP Flood

### MITRE ATT&CK Technique

- T1498 – Network Denial of Service

---

# 6. Root Cause Analysis

The investigation identified several contributing factors.

### Primary Cause

Improper firewall configuration.

### Contributing Factors

- No ICMP rate limiting
- Missing ingress filtering
- Insufficient monitoring
- Lack of anomaly detection
- Weak firewall hardening

---

# 7. Indicators of Compromise (IoCs)

The following indicators were observed:

- Extremely high ICMP traffic
- Significant increase in network latency
- Service timeouts
- High CPU utilization on network devices
- Network congestion

No evidence of malware or unauthorized authentication attempts was identified.

---

# 8. Impact Assessment

## Confidentiality

No impact identified.

---

## Integrity

No evidence of data modification.

---

## Availability

High impact.

Critical services were unavailable for approximately two hours.

---

# 9. Immediate Response Actions

The Incident Response Team performed the following actions:

- Blocked incoming ICMP traffic
- Applied ICMP rate limiting
- Updated firewall rules
- Disabled non-essential services
- Restored critical services
- Increased network monitoring

---

# 10. Containment

Short-term containment:

- Block malicious traffic
- Limit ICMP requests
- Isolate affected network segments

Long-term containment:

- Harden firewall configuration
- Deploy IDS/IPS
- Continuous monitoring

---

# 11. Eradication

Security engineers removed the firewall configuration weakness.

Additional controls included:

- Source IP verification
- ICMP rate limiting
- Traffic filtering
- Firewall policy review

---

# 12. Recovery

Recovery activities included:

- Restoring network services
- Verifying firewall configuration
- Testing network availability
- Monitoring for recurring attacks
- Validating business applications

Normal operations resumed after approximately two hours.

---

# 13. Lessons Learned

The incident demonstrated the importance of:

- Proper firewall configuration
- Continuous network monitoring
- Security hardening
- Network traffic baselining
- Incident response planning

---

# 14. Recommendations

The following improvements are recommended.

## Firewall Security

- Review firewall rules monthly
- Enable ingress filtering
- Configure ICMP rate limiting
- Remove unnecessary open ports

---

## Monitoring

- Deploy centralized logging
- Implement SIEM monitoring
- Configure IDS/IPS alerts
- Establish traffic baselines

---

## Security Governance

- Perform regular vulnerability assessments
- Conduct firewall audits
- Improve incident response procedures
- Train employees on cybersecurity awareness

---

# 15. NIST CSF Mapping

| Function | Actions |
|----------|---------|
| Identify | Asset inventory, risk analysis, root cause investigation |
| Protect | Firewall hardening, rate limiting, security policies |
| Detect | Network monitoring, IDS, traffic analysis |
| Respond | Incident containment, mitigation, communication |
| Recover | Service restoration, validation, documentation |

---

# 16. Conclusion

The DoS attack successfully exploited a firewall configuration weakness and temporarily affected the organization's availability.

Although no data breach occurred, the incident highlighted weaknesses in perimeter security and monitoring capabilities.

Applying the NIST Cybersecurity Framework provided a structured methodology for identifying the root cause, improving defensive controls, and strengthening the organization's overall security posture.

The recommendations presented in this report will reduce the likelihood of similar attacks and improve future incident response capabilities.

---

**Prepared by**

Salim Younsi

Junior Cybersecurity Analyst Portfolio

Google Cybersecurity Professional Certificate