# 🛡️ TP4 - SSH Brute Force Detection (SOC Analysis)

## 🎯 Objective
Detect and analyze a brute force attack targeting an SSH service using network traffic and system logs.

---

## 🎬 Scenario
A Linux server is receiving multiple SSH login attempts from a suspicious internal IP address.

As a SOC Analyst, the goal is to:
- Detect abnormal traffic
- Identify attack patterns
- Analyze authentication logs
- Confirm the intrusion attempt

---

## 🛠️ Tools Used
- Wireshark
- Linux (auth logs)
- SSH client

---

## ⚙️ Environment
- Attacker IP: `192.168.1.80`
- Target IP: `192.168.1.75`
- Service: SSH (port 22)

---

## 🔍 Phase 1 - Traffic Capture

Wireshark was used to monitor network activity.

### Filter:
```bash
tcp.port == 22