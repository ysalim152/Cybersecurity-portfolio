# NIST Cybersecurity Framework (CSF) Workflow

**Project:** NIST CSF Incident Response Case Study

**Author:** Salim Younsi

**Role:** Junior Cybersecurity Analyst

**Framework:** NIST Cybersecurity Framework (CSF) 2.0

---

# Purpose

This document illustrates how the five core functions of the NIST Cybersecurity Framework (CSF) were applied during the investigation and response to a simulated Denial-of-Service (DoS) attack.

The workflow provides a structured approach for identifying cybersecurity risks, implementing protective measures, detecting malicious activity, responding to security incidents, and restoring normal business operations.

---

# NIST CSF Workflow Overview

```
                  Cybersecurity Incident

                           │
                           ▼

                ┌────────────────────┐
                │      IDENTIFY       │
                └────────────────────┘
                           │
                           ▼

                ┌────────────────────┐
                │      PROTECT        │
                └────────────────────┘
                           │
                           ▼

                ┌────────────────────┐
                │       DETECT        │
                └────────────────────┘
                           │
                           ▼

                ┌────────────────────┐
                │      RESPOND        │
                └────────────────────┘
                           │
                           ▼

                ┌────────────────────┐
                │      RECOVER        │
                └────────────────────┘
                           │
                           ▼

            Continuous Improvement Cycle
```

---

# Phase 1 — Identify (ID)

## Objective

Develop an understanding of the organization's assets, business environment, risks, and vulnerabilities.

### Activities

- Identify critical assets.
- Inventory network devices.
- Assess business impact.
- Identify vulnerabilities.
- Analyze firewall configuration.
- Determine the root cause.

### Deliverables

- Asset Inventory
- Risk Assessment
- Incident Scope
- Root Cause Analysis

### Outcome

The firewall misconfiguration allowing unrestricted ICMP traffic was identified as the primary cause of the incident.

---

# Phase 2 — Protect (PR)

## Objective

Implement safeguards to reduce cybersecurity risk and protect critical assets.

### Activities

- Harden firewall configurations.
- Configure ICMP rate limiting.
- Apply the Principle of Least Privilege (PoLP).
- Enable Multi-Factor Authentication (MFA).
- Improve security awareness.

### Security Controls

- Firewall Hardening
- Access Control
- Security Policies
- Configuration Management

### Outcome

The organization's attack surface was significantly reduced.

---

# Phase 3 — Detect (DE)

## Objective

Identify cybersecurity events as early as possible.

### Activities

- Monitor firewall logs.
- Analyze network traffic.
- Detect anomalies.
- Collect security logs.
- Generate security alerts.

### Detection Tools

- IDS
- SIEM
- Firewall Logs
- Network Monitoring

### Indicators of Compromise (IoCs)

- ICMP traffic spike
- Increased latency
- High bandwidth usage
- Firewall log anomalies

### Outcome

The attack was detected quickly, allowing rapid containment.

---

# Phase 4 — Respond (RS)

## Objective

Contain the incident and minimize operational impact.

### Activities

- Activate the Incident Response Team.
- Block malicious traffic.
- Update firewall rules.
- Collect forensic evidence.
- Notify stakeholders.

### Response Workflow

```
Detection
     │
     ▼
Analysis
     │
     ▼
Containment
     │
     ▼
Eradication
     │
     ▼
Recovery
```

### Outcome

The incident was successfully contained and business operations resumed.

---

# Phase 5 — Recover (RC)

## Objective

Restore systems and improve organizational resilience.

### Activities

- Restore critical services.
- Validate firewall configuration.
- Verify network availability.
- Monitor for recurring attacks.
- Update documentation.
- Conduct lessons learned review.

### Deliverables

- Incident Report
- Lessons Learned
- Security Recommendations
- Improvement Plan

### Outcome

The organization returned to normal operations with enhanced security controls.

---

# Continuous Improvement

The NIST CSF is not a linear process.

Following every incident, the organization should:

- Review lessons learned.
- Update security policies.
- Improve monitoring capabilities.
- Conduct vulnerability assessments.
- Review firewall rules.
- Test incident response procedures.
- Repeat the Identify phase.

```
Recover
   │
   ▼
Lessons Learned
   │
   ▼
Security Improvements
   │
   ▼
Risk Assessment
   │
   ▼
Identify
```

---

# Workflow Mapping

| NIST Function | Primary Objective | Deliverables |
|---------------|-------------------|--------------|
| Identify | Understand risks and assets | Risk Assessment, Asset Inventory |
| Protect | Reduce attack surface | Firewall Rules, Security Controls |
| Detect | Identify threats | Alerts, Logs, IDS Events |
| Respond | Contain and mitigate | Incident Report, Response Actions |
| Recover | Restore operations | Recovery Report, Improvement Plan |

---

# Key Benefits of the NIST CSF Workflow

- Provides a structured incident response methodology.
- Improves communication across security teams.
- Supports risk-based decision-making.
- Enhances organizational resilience.
- Promotes continuous improvement.
- Aligns cybersecurity activities with business objectives.

---

# Conclusion

Applying the NIST Cybersecurity Framework workflow enabled the organization to effectively manage a simulated DoS attack from initial detection through recovery.

The structured approach ensured that risks were identified, security controls were strengthened, incident response activities were coordinated, and lessons learned were integrated into future security improvements.

This workflow demonstrates how the NIST CSF supports a repeatable, scalable, and business-focused cybersecurity program.

---

# Prepared by

**Salim Younsi**

Junior Cybersecurity Analyst Portfolio

Google Cybersecurity Professional Certificate