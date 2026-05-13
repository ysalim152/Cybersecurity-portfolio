### 🏗️ Network Architecture & DNS Flow

By centralizing DNS resolution through the Pi-hole, the network establishes a single inspection point. 
This allows for efficient, 
network-wide filtering of trackers, 
ads, 
and malicious domains before they ever reach the end-user devices.

### Ce que ce code va générer visuellement :

1.  **Une boîte "Local Home Network"** qui regroupe vos appareils et votre Raspberry Pi.
2.  **Un processus de décision (le losange)** : Montrant exactement l'étape d'inspection (Choke point) où Pi-hole décide si le domaine est sain ou malveillant/publicitaire.
3.  **La sortie vers Internet** : Via votre routeur Ooredoo vers le fournisseur DNS final.


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

### 🛠️ Deployment Log

The deployment was performed on a Raspberry Pi running Raspberry Pi OS (Lite), accessed remotely via SSH.

**1. System Preparation**
Ensuring the operating system and package repositories were fully updated before installation to prevent dependency conflicts:
```bash
sudo apt update
sudo apt full-upgrade -y
sudo reboot