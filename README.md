# Python Network Port Scanner

### 🛡️ Project Overview
This tool is a custom Network Reconnaissance script built to demonstrate **Active Scanning** concepts from CompTIA Security+ (Domain 3). It utilizes Python's `socket` library to perform a TCP Connect Scan on a target to identify open service ports.

### 🎯 Objective
Port scanning is the first step in the "Cyber Kill Chain" (Reconnaissance). This tool allows security analysts to map out the attack surface of a system by identifying which doors (ports) are unlocked.

### 🔧 Tech Stack
* **Language:** Python 3
* **Networking Concepts:** TCP/IP, Socket Programming, IPv4
* **Ports Scanned:** 21 (FTP), 22 (SSH), 80 (HTTP), 443 (HTTPS), and others.

### 🚀 How to Use
1.  Clone the repository:
    ```bash
    git clone [https://github.com/17032003-pb/Network-Port-Scanner.git](https://github.com/17032003-pb/Network-Port-Scanner.git)
    ```
2.  Run the scanner:
    ```bash
    python port_scanner.py
    ```
3.  Enter a valid IP or Hostname (e.g., `scanme.nmap.org`).

### ⚠️ Ethical Warning
This tool is for educational purposes and authorized testing only. Scanning networks without permission is illegal.
