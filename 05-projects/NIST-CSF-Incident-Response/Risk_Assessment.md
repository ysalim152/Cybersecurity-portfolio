# Risk Assessment Report

**Project:** NIST CSF Incident Response Case Study  
**Author:** Salim Younsi  
**Role:** Junior Cybersecurity Analyst  
**Assessment Methodology:** NIST SP 800-30 & NIST Cybersecurity Framework (CSF)  
**Date:** July 2026

---

# 1. Purpose

The purpose of this risk assessment is to identify, evaluate, and prioritize cybersecurity risks associated with the Denial-of-Service (DoS) incident affecting the organization's internal network.

The assessment supports decision-making by identifying appropriate security controls to reduce the likelihood and impact of future incidents.

---

# 2. Scope

This assessment covers the following assets:

- Perimeter Firewall
- Internal Network Infrastructure
- Core Network Switches
- Web Services
- Employee Workstations
- Network Monitoring Systems

---

# 3. Risk Assessment Methodology

The risk level is calculated using two factors:

- **Likelihood** (Probability that the threat will occur)
- **Impact** (Business consequences if the threat occurs)

| Likelihood | Description |
|------------|-------------|
| Low | Unlikely to occur |
| Medium | Possible |
| High | Very likely |

| Impact | Description |
|--------|-------------|
| Low | Minimal disruption |
| Medium | Noticeable operational impact |
| High | Significant business disruption |

Risk Level = Likelihood × Impact

---

# 4. Risk Register

| ID | Threat | Vulnerability | Asset | Likelihood | Impact | Risk |
|----|---------|--------------|-------|------------|--------|------|
| R-01 | ICMP Flood | Firewall Misconfiguration | Firewall | High | High | Critical |
| R-02 | Denial of Service | No Rate Limiting | Internal Network | High | High | Critical |
| R-03 | Network Congestion | Weak Monitoring | Network Infrastructure | Medium | High | High |
| R-04 | Delayed Detection | Lack of IDS | Security Monitoring | Medium | Medium | Medium |
| R-05 | Configuration Errors | Weak Change Management | Firewall | Medium | Medium | Medium |

---

# 5. Risk Matrix

|                | **Low Impact** | **Medium Impact** | **High Impact** |
|----------------|----------------|-------------------|-----------------|
| **High Likelihood** | Medium | High | **Critical** |
| **Medium Likelihood** | Low | Medium | High |
| **Low Likelihood** | Low | Low | Medium |

Current Overall Risk Level:

**HIGH**

---

# 6. Risk Analysis

## Risk R-01

### Threat

ICMP Flood Attack

### Vulnerability

Improper firewall configuration allowing unrestricted ICMP traffic.

### Business Impact

- Network outage
- Loss of productivity
- Business interruption

### Existing Controls

- Standard firewall

### Recommended Controls

- ICMP Rate Limiting
- Firewall Hardening
- Source IP Verification
- Continuous Monitoring

Residual Risk

Medium

---

## Risk R-02

### Threat

Denial of Service

### Vulnerability

Absence of ICMP traffic filtering.

### Recommended Controls

- IDS
- IPS
- Traffic Analysis
- Automated Alerting

Residual Risk

Low

---

## Risk R-03

### Threat

Network Congestion

### Cause

Excessive traffic volume.

### Recommended Controls

- Baseline Network Traffic
- Performance Monitoring
- Bandwidth Monitoring

Residual Risk

Low

---

## Risk R-04

### Threat

Delayed Incident Detection

### Cause

No dedicated intrusion detection capability.

### Recommended Controls

- IDS Deployment
- SIEM Integration
- Log Correlation

Residual Risk

Low

---

## Risk R-05

### Threat

Firewall Configuration Errors

### Cause

Insufficient configuration review process.

### Recommended Controls

- Monthly Firewall Audits
- Change Management Process
- Configuration Backups
- Peer Review

Residual Risk

Low

---

# 7. Recommended Mitigation Plan

## Immediate Actions (0–30 Days)

- Configure ICMP rate limiting.
- Review firewall rules.
- Enable centralized logging.
- Deploy IDS monitoring.

---

## Short-Term Actions (1–3 Months)

- Conduct vulnerability assessments.
- Establish security baselines.
- Perform firewall audits.
- Implement change management procedures.

---

## Long-Term Actions (3–12 Months)

- Deploy SIEM platform.
- Conduct incident response exercises.
- Improve disaster recovery planning.
- Implement continuous security monitoring.

---

# 8. Risk Prioritization

| Priority | Action |
|----------|--------|
| Critical | Firewall Hardening |
| Critical | ICMP Rate Limiting |
| High | IDS Deployment |
| High | Continuous Monitoring |
| Medium | Security Awareness Training |
| Medium | Periodic Firewall Reviews |

---

# 9. Residual Risk Evaluation

Following implementation of the recommended security controls:

| Risk | Initial | Residual |
|------|----------|----------|
| ICMP Flood | Critical | Medium |
| DoS Attack | Critical | Low |
| Weak Monitoring | High | Low |
| Firewall Errors | Medium | Low |

Overall Residual Risk:

**LOW**

---

# 10. Conclusion

The assessment identified firewall misconfiguration and insufficient traffic controls as the primary contributors to the DoS incident.

Implementing the recommended controls—including firewall hardening, ICMP rate limiting, IDS deployment, and continuous monitoring—will significantly reduce the organization's exposure to similar attacks.

This assessment demonstrates a structured, risk-based approach to cybersecurity aligned with the NIST Cybersecurity Framework and industry best practices.

---

# Approval

Prepared by:

**Salim Younsi**

Junior Cybersecurity Analyst Portfolio

Google Cybersecurity Professional Certificate