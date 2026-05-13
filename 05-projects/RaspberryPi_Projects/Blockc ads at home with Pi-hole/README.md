### 🏗️ Network Architecture & DNS Flow

By centralizing DNS resolution through the Pi-hole, the network establishes a single inspection point. This allows for efficient, network-wide filtering of trackers, ads, and malicious domains before they ever reach the end-user devices.

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