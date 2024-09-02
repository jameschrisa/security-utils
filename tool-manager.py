import json
import os
from system_utils import is_tool_installed, get_tool_version

# List of tools to install with their details
tools = {
    "nmap": {"category": "Network Security", "description": "Network scanning and exploration tool"},
    "wireshark": {"category": "Network Security", "description": "Network protocol analyzer and packet sniffer"},
    "openvas": {"category": "Vulnerability Assessment", "description": "Vulnerability scanner and manager"},
    "nikto": {"category": "Vulnerability Assessment", "description": "Web server vulnerability scanner"},
    "metasploit": {"category": "Penetration Testing", "description": "Exploitation framework and penetration testing tool"},
    "burpsuite": {"category": "Penetration Testing", "description": "Web application security testing tool"},
    "gpg": {"category": "Encryption and Privacy", "description": "Encryption and digital signature tool"},
    "tor": {"category": "Encryption and Privacy", "description": "Anonymity and privacy network"},
    "lynis": {"category": "System Hardening", "description": "System auditing and hardening tool"},
    "ossec": {"category": "System Hardening", "description": "Host-based intrusion detection system"},
    "clamav": {"category": "Other", "description": "Antivirus engine"},
    "tcpdump": {"category": "Other", "description": "Network packet capture and analysis tool"}
}

def save_installation_status(status):
    """Save the installation status to a JSON file."""
    with open('installation_status.json', 'w') as f:
        json.dump(status, f, indent=4)

def load_installation_status():
    """Load the installation status from a JSON file."""
    if os.path.exists('installation_status.json'):
        with open('installation_status.json', 'r') as f:
            return json.load(f)
    return {}

def update_tool_status():
    """Update the status of all tools."""
    status = {}
    for tool in tools:
        if is_tool_installed(tool):
            version = get_tool_version(tool)
            status[tool] = {"installed": True, "version": version}
        else:
            status[tool] = {"installed": False, "version": None}
    save_installation_status(status)
    return status

def get_tools_by_category(category):
    """Get a list of tools in a specific category."""
    return [tool for tool, info in tools.items() if info['category'] == category]

def get_tool_info(tool):
    """Get information about a specific tool."""
    return tools.get(tool, {"category": "Unknown", "description": "No description available"})

def get_all_categories():
    """Get a list of all tool categories."""
    return list(set(tool['category'] for tool in tools.values()))

