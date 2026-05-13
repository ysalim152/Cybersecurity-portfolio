from weasyprint import HTML
import markdown

# README Markdown content
readme_content = """
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
"""

# Save README.md
with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme_content)

print("README.md generated successfully.")

# Convert Markdown to HTML
html_content = markdown.markdown(readme_content)

# Generate PDF
HTML(string=html_content).write_pdf("PiHole_Project_Report.pdf")

print("PDF report generated successfully.")
