
# Network-Wide Ad Blocking & Security Sinkhole

## Project Overview

This project involves the deployment of a **Pi-hole** server on a Raspberry Pi
to act as a private DNS sinkhole for a home network.

By centralizing DNS resolution, this implementation provides network-wide
protection against advertisements, trackers, and malicious domains,
enhancing both privacy and security for all connected devices
(PCs, smartphones, IoT, Smart TVs).

---

## 🏗️ Network Architecture & DNS Flow

By centralizing DNS resolution through the Pi-hole,
the network establishes a single inspection point.

This allows for efficient, network-wide filtering
of trackers, ads, and malicious domains before
they ever reach the end-user devices.

### What this code will visually generate:

A "Local Home Network" box grouping your devices and your Raspberry Pi.
A decision process (the diamond shape): showing the exact inspection step (choke point) where Pi-hole determines whether a domain is safe or malicious/advertising-related.
The Internet outbound connection: through your Ooredoo router to the final DNS provider.


```mermaid
graph LR
    subgraph Home_Network [Local Home Network]
        A[📱 Clients<br>PC, Phone, IoT] -->|1. DNS Request| B(🍓 Pi-hole<br>DNS Sinkhole)
        B -->|2. Check Blocklists| C{Is Domain<br>Blocked?}
    end

    C -- Yes --> D[🛑 Sinkholed<br>Returns 0.0.0.0]
    C -- No --> E[🌐 Ooredoo Router<br>Gateway]
    E -->|3. Forward Query| F((☁️ Upstream DNS<br>e.g. Cloudflare))
    F -.->|4. Resolves IP| A
