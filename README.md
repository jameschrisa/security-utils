![secutils](./secutil.png "security utilities")

# Open-Source Security Tools

This repository contains a list of widely available open-source security tools for both Mac and Linux systems. These tools cover various aspects of cybersecurity, including network security, vulnerability assessment, penetration testing, encryption, privacy, and system hardening.

## Table of Contents

1. [Network Security](#network-security)
2. [Vulnerability Assessment](#vulnerability-assessment)
3. [Penetration Testing](#penetration-testing)
4. [Encryption and Privacy](#encryption-and-privacy)
5. [System Hardening](#system-hardening)
6. [Other](#other)

## Network Security

### 1. Nmap (Mac, Linux)
- **Description**: Network scanning and exploration tool
- **Example**: `nmap -sS 192.168.1.1` (scan a single IP address)

### 2. Wireshark (Mac, Linux)
- **Description**: Network protocol analyzer and packet sniffer
- **Example**: `wireshark -i en0` (capture packets on interface en0)

## Vulnerability Assessment

### 1. OpenVAS (Mac, Linux)
- **Description**: Vulnerability scanner and manager
- **Example**: `openvas -h 192.168.1.1` (scan a single IP address)

### 2. Nikto (Mac, Linux)
- **Description**: Web server vulnerability scanner
- **Example**: `nikto -h http://example.com` (scan a web server)

## Penetration Testing

### 1. Metasploit (Mac, Linux)
- **Description**: Exploitation framework and penetration testing tool
- **Example**: `msfconsole` (start the Metasploit console)

### 2. Burp Suite (Mac, Linux)
- **Description**: Web application security testing tool
- **Example**: `burpsuite` (start the Burp Suite GUI)

## Encryption and Privacy

### 1. GPG (Mac, Linux)
- **Description**: Encryption and digital signature tool
- **Example**: `gpg -c file.txt` (encrypt a file)

### 2. Tor (Mac, Linux)
- **Description**: Anonymity and privacy network
- **Example**: `tor` (start the Tor service)

## System Hardening

### 1. Lynis (Mac, Linux)
- **Description**: System auditing and hardening tool
- **Example**: `lynis audit system` (audit the system)

### 2. OSSEC (Mac, Linux)
- **Description**: Host-based intrusion detection system
- **Example**: `ossec-control start` (start the OSSEC service)

## Other

### 1. ClamAV (Mac, Linux)
- **Description**: Antivirus engine
- **Example**: `clamscan -i file.exe` (scan a file for malware)

### 2. Tcpdump (Mac, Linux)
- **Description**: Network packet capture and analysis tool
- **Example**: `tcpdump -i en0` (capture packets on interface en0)

## Note

The examples provided are brief illustrations of how to use each tool. Always consult the documentation and usage guidelines for each tool to ensure proper use and understanding of its capabilities and potential impacts.
