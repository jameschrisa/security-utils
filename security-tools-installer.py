import os
import sys
import subprocess
import logging
from rich.console import Console
from rich.progress import Progress
from rich.panel import Panel
from rich import print as rprint
import requests
import platform

# Set up logging
logging.basicConfig(filename='security_tools_install.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

console = Console()

# List of tools to install
tools = [
    "nmap", "wireshark", "openvas", "nikto", "metasploit", "burpsuite",
    "gpg", "tor", "lynis", "ossec", "clamav", "tcpdump"
]

def is_tool_installed(name):
    """Check whether `name` is on PATH and marked as executable."""
    from shutil import which
    return which(name) is not None

def install_tool(tool):
    """Install a tool using the appropriate package manager."""
    try:
        if platform.system() == "Darwin":  # macOS
            subprocess.run(["brew", "install", tool], check=True)
        elif platform.system() == "Linux":
            if os.path.exists("/usr/bin/apt"):
                subprocess.run(["sudo", "apt", "install", "-y", tool], check=True)
            elif os.path.exists("/usr/bin/yum"):
                subprocess.run(["sudo", "yum", "install", "-y", tool], check=True)
            else:
                raise Exception("Unsupported Linux distribution")
        else:
            raise Exception("Unsupported operating system")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to install {tool}: {str(e)}")
        raise

def download_file(url, filename):
    """Download a file from a given URL."""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with Progress() as progress:
        task = progress.add_task(f"[green]Downloading {filename}...", total=total_size)
        with open(filename, 'wb') as file:
            for data in response.iter_content(chunk_size=1024):
                size = file.write(data)
                progress.update(task, advance=size)

def main():
    console.print(Panel("Security Tools Installer", style="bold magenta"))
    
    rprint("[yellow]This script will attempt to download and install the following tools:[/yellow]")
    for tool in tools:
        rprint(f"  - {tool}")
    
    proceed = console.input("\nDo you want to proceed? [y/N]: ")
    if proceed.lower() != 'y':
        rprint("[red]Installation cancelled.[/red]")
        return

    for tool in tools:
        with console.status(f"[bold green]Checking {tool}...[/bold green]"):
            if is_tool_installed(tool):
                rprint(f"[green]{tool} is already installed.[/green]")
            else:
                rprint(f"[yellow]{tool} is not installed. Attempting to install...[/yellow]")
                try:
                    install_tool(tool)
                    rprint(f"[green]{tool} has been successfully installed.[/green]")
                except Exception as e:
                    rprint(f"[red]Failed to install {tool}. Check the log file for details.[/red]")
                    logging.error(f"Error installing {tool}: {str(e)}")

    rprint("\n[bold green]Installation process completed. Please check the log file for any errors or warnings.[/bold green]")

if __name__ == "__main__":
    main()
