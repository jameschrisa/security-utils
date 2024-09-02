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

# Automated Installation Script

This repository includes a Python script (`security_tools_installer.py`) that automates the process of checking for, downloading, and installing the listed security tools on Linux and Mac systems.

### Features

- Checks if each tool is already installed
- Downloads and installs missing tools using the appropriate package manager (Homebrew for macOS, apt or yum for Linux)
- Uses the Rich library for progress bars and interactive console output
- Implements error handling and logging for troubleshooting

### Prerequisites

Before running the script, ensure you have the following:

1. Python 3.x installed
2. pip (Python package manager)
3. Required Python libraries: `rich` and `requests`

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/security-tools-repo.git
   cd security-tools-repo
   ```

2. Install the required Python libraries:
   ```
   pip install rich requests
   ```

3. Run the script with sudo privileges:
   ```
   sudo python3 security_tools_installer.py
   ```

### Usage Notes

- The script will prompt for confirmation before proceeding with the installation.
- Installation progress and any errors will be displayed in the console.
- A detailed log file (`security_tools_install.log`) is created for troubleshooting.
- Some tools may require additional setup or configuration after installation. Refer to their official documentation for post-installation steps.
- Ensure you have a stable internet connection before running the script.
- Always review the log file after running the script to check for any warnings or errors.

### Caution

- Installing all these tools might take a significant amount of time and disk space.
- Some tools might conflict with existing system configurations or other installed software. Always back up your system before running this script.
- This script is provided as a starting point and may need adjustments based on your specific system configuration.

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
