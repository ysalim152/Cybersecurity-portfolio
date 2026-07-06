# NIST Cybersecurity Framework (CSF) Analysis

**Project:** NIST CSF Incident Response Case Study  
**Author:** Salim Younsi  
**Role:** Junior Cybersecurity Analyst  
**Framework:** NIST Cybersecurity Framework (CSF) 2.0  
**Incident Type:** Denial of Service (DoS) – ICMP Flood

---

# 1. Introduction

This document analyzes a simulated cybersecurity incident using the **NIST Cybersecurity Framework (CSF)**.

The organization experienced a **Denial-of-Service (DoS)** attack caused by an ICMP flood that exploited a firewall configuration weakness. The objective of this analysis is to demonstrate how the five NIST CSF functions can be applied to identify risks, protect assets, improve detection capabilities, coordinate incident response, and strengthen recovery processes.

---

# 2. Incident Summary

| Item | Description |
|------|-------------|
| Incident Type | Denial of Service (DoS) |
| Attack Vector | ICMP Flood |
| Severity | High |
| Duration | Approximately 2 Hours |
| Primary Asset | Internal Network |
| Root Cause | Firewall Misconfiguration |

---

# 3. NIST CSF Analysis

---

# Function 1 — Identify (ID)

## Objective

Develop an understanding of the organization's environment, assets, risks, and vulnerabilities.

## Activities Performed

- Identified critical network assets.
- Reviewed firewall configuration.
- Determined the root cause of the attack.
- Assessed business impact.
- Identified vulnerable security controls.

## Assets Identified

- Firewall
- Core Switches
- Internal Network
- Web Services
- Employee Workstations
- Internet Gateway

## Risks Identified

| Risk | Impact |
|------|--------|
| Firewall misconfiguration | High |
| Excessive ICMP traffic | High |
| Service interruption | High |
| Weak monitoring capabilities | Medium |

## Findings

The firewall allowed unrestricted ICMP traffic, enabling an attacker to overwhelm the network.

---

# Function 2 — Protect (PR)

## Objective

Implement safeguards to reduce cybersecurity risk.

## Existing Controls

- Basic firewall
- Antivirus software
- User authentication

## Recommended Security Improvements

### Firewall Hardening

- Enable ICMP rate limiting.
- Block unnecessary inbound ICMP traffic.
- Enable ingress and egress filtering.
- Review firewall rules regularly.

### Access Control

- Apply the Principle of Least Privilege (PoLP).
- Review administrative privileges.
- Implement Multi-Factor Authentication (MFA).

### Security Awareness

- Train employees on cybersecurity best practices.
- Establish change management procedures.
- Maintain secure configuration baselines.

## Expected Outcome

Reduced attack surface and improved resilience against network-based attacks.

---

# Function 3 — Detect (DE)

## Objective

Implement processes to identify cybersecurity events quickly.

## Detection Improvements

- Deploy an Intrusion Detection System (IDS).
- Enable centralized log collection.
- Monitor firewall events.
- Establish network traffic baselines.
- Configure automated security alerts.

## Indicators of Compromise (IoCs)

- Sudden spike in ICMP packets.
- Increased network latency.
- Service timeouts.
- High bandwidth utilization.
- Firewall log anomalies.

## Monitoring Tools

| Tool | Purpose |
|------|---------|
| Firewall Logs | Traffic analysis |
| IDS | Threat detection |
| SIEM | Event correlation |
| Network Monitoring | Performance analysis |

## Expected Outcome

Faster identification of abnormal network activity.

---

# Function 4 — Respond (RS)

## Objective

Contain the incident and minimize operational impact.

## Response Actions

- Activated the Incident Response Team.
- Blocked malicious ICMP traffic.
- Updated firewall rules.
- Restored critical network services.
- Collected forensic evidence.
- Performed root cause analysis.

## Communication

Stakeholders informed:

- IT Management
- Security Team
- Network Administrators

## Documentation

Incident information was documented to support future investigations and continuous improvement.

## Expected Outcome

Rapid containment and reduced recovery time.

---

# Function 5 — Recover (RC)

## Objective

Restore normal business operations while improving resilience.

## Recovery Activities

- Verified firewall configuration.
- Confirmed service availability.
- Monitored the network for recurring attacks.
- Updated security documentation.
- Reviewed incident response procedures.

## Long-Term Improvements

- Conduct periodic firewall audits.
- Perform vulnerability assessments.
- Implement continuous monitoring.
- Schedule incident response exercises.
- Review disaster recovery procedures annually.

## Expected Outcome

Improved organizational resilience and stronger cybersecurity posture.

---

# 4. Risk Assessment Summary

| Threat | Likelihood | Impact | Risk Level |
|---------|------------|--------|------------|
| ICMP Flood | Medium | High | High |
| Firewall Misconfiguration | Medium | High | High |
| Service Downtime | Medium | High | High |
| Lack of Monitoring | Medium | Medium | Medium |

---

# 5. Security Controls Implemented

| Control | Status |
|----------|--------|
| Firewall Hardening | Implemented |
| ICMP Rate Limiting | Implemented |
| Source IP Verification | Implemented |
| IDS/IPS Deployment | Recommended |
| Continuous Monitoring | Implemented |
| Security Awareness Training | Recommended |

---

# 6. Key Lessons Learned

The incident highlighted several important cybersecurity principles:

- Proper firewall configuration is essential.
- Continuous monitoring improves early detection.
- Network traffic baselines help identify anomalies.
- Incident response procedures reduce recovery time.
- Applying the NIST CSF provides a structured and repeatable approach to incident management.

---

# 7. Conclusion

The NIST Cybersecurity Framework provided a comprehensive methodology for managing the simulated DoS incident.

By applying the five core functions—Identify, Protect, Detect, Respond, and Recover—the organization successfully identified the root cause, restored critical services, and implemented security improvements to reduce future risk.

This project demonstrates practical knowledge of incident response, network security, security hardening, and risk management within a structured cybersecurity framework.

---

**Prepared by**

**Salim Younsi**

Junior Cybersecurity Analyst Portfolio

Google Cybersecurity Professional Certificate