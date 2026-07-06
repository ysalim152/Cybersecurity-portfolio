# Incident Timeline Report

**Project:** NIST CSF Incident Response Case Study  
**Author:** Salim Younsi  
**Role:** Junior Cybersecurity Analyst  
**Incident ID:** IR-2026-001  
**Classification:** Internal Use Only  
**Framework:** NIST Cybersecurity Framework (CSF)

---

# 1. Purpose

The purpose of this report is to reconstruct the sequence of events that occurred during the Denial-of-Service (DoS) attack. A detailed timeline supports incident investigation, identifies response gaps, and contributes to improving future incident response procedures.

---

# 2. Incident Overview

On the day of the incident, the organization experienced an ICMP Flood attack targeting its internal network. The attack exploited a firewall configuration weakness, resulting in a temporary disruption of network services.

The Security Operations Center (SOC) responded by containing the attack, restoring business operations, and documenting the incident.

---

# 3. Chronological Timeline

| Time | Event | Category |
|------|-------|----------|
| 09:55 | Normal network operations | Baseline |
| 10:00 | Large increase in inbound ICMP traffic detected | Detection |
| 10:05 | Firewall logs record abnormal traffic volume | Detection |
| 10:10 | Users begin reporting network slowness | User Report |
| 10:15 | Network latency increases significantly | Impact |
| 10:20 | Critical internal services become unavailable | Service Disruption |
| 10:25 | SOC analysts begin investigation | Investigation |
| 10:30 | Firewall identified as the attack entry point | Root Cause Analysis |
| 10:35 | Incident classified as High Severity | Incident Management |
| 10:40 | Incident Response Team activated | Response |
| 10:45 | Malicious ICMP traffic blocked | Containment |
| 10:50 | ICMP rate limiting configured | Mitigation |
| 11:00 | Firewall rules reviewed and updated | Hardening |
| 11:10 | Network monitoring intensified | Monitoring |
| 11:20 | IDS confirms traffic returning to normal | Detection |
| 11:40 | Critical services restored | Recovery |
| 11:50 | Validation testing completed | Verification |
| 12:00 | Incident officially closed | Closure |

---

# 4. Timeline Visualization

```
09:55  Normal Operations
   │
10:00  ICMP Flood Begins
   │
10:10  Performance Degradation
   │
10:20  Service Outage
   │
10:30  Investigation Starts
   │
10:40  Incident Response Activated
   │
10:45  ICMP Blocked
   │
10:50  Firewall Hardened
   │
11:20  Traffic Returns to Normal
   │
11:40  Services Restored
   │
12:00  Incident Closed
```

---

# 5. Key Decisions

### Decision 1

**Action**

Block inbound ICMP traffic.

**Reason**

Immediately stop malicious traffic and restore network availability.

---

### Decision 2

**Action**

Apply ICMP rate limiting.

**Reason**

Prevent future ICMP Flood attacks while allowing legitimate diagnostic traffic.

---

### Decision 3

**Action**

Review firewall configuration.

**Reason**

Identify the configuration weakness exploited during the attack.

---

### Decision 4

**Action**

Increase network monitoring.

**Reason**

Detect any recurrence of malicious activity.

---

# 6. Incident Response Performance

| Activity | Result |
|----------|--------|
| Detection | Successful |
| Analysis | Successful |
| Containment | Successful |
| Eradication | Successful |
| Recovery | Successful |
| Documentation | Completed |

---

# 7. Response Metrics

| Metric | Value |
|---------|-------|
| Time to Detect (TTD) | 5 minutes |
| Time to Analyze | 20 minutes |
| Time to Contain | 45 minutes |
| Time to Recover (TTR) | 1 hour 40 minutes |
| Total Incident Duration | Approximately 2 hours |

---

# 8. Lessons Identified During the Timeline

The incident timeline revealed several opportunities for improvement:

- Firewall configurations should be reviewed regularly.
- Network baselines help identify abnormal traffic earlier.
- Automated alerts reduce detection time.
- Incident response playbooks improve coordination.
- Continuous monitoring shortens recovery time.

---

# 9. Recommendations

To improve future response capabilities, the following actions are recommended:

### Short-Term

- Enable real-time firewall alerts.
- Deploy centralized log collection.
- Improve network traffic visualization.

### Long-Term

- Conduct quarterly incident response exercises.
- Implement Security Information and Event Management (SIEM).
- Automate incident notifications.
- Review firewall rules every quarter.
- Update the Incident Response Plan annually.

---

# 10. Conclusion

The timeline demonstrates that the organization successfully detected, contained, and recovered from a Denial-of-Service attack within approximately two hours.

While the response was effective, earlier detection and stronger preventive controls could have reduced operational impact.

Maintaining detailed timelines for future incidents will improve investigations, support post-incident reviews, and strengthen the organization's overall incident response maturity.

---

# Approval

Prepared by:

**Salim Younsi**

Junior Cybersecurity Analyst Portfolio

Google Cybersecurity Professional Certificate