import platform
import shutil
import subprocess
import logging
import os
import getpass
import psutil

def get_package_manager():
    """Determine the package manager to use."""
    if platform.system() == "Darwin":
        return "brew"
    elif platform.system() == "Linux":
        if shutil.which("apt"):
            return "apt"
        elif shutil.which("yum"):
            return "yum"
        elif shutil.which("dnf"):
            return "dnf"
    return None

def is_tool_installed(name):
    """Check whether `name` is on PATH and marked as executable."""
    return shutil.which(name) is not None

def install_tool(tool, package_manager, dry_run=False):
    """Install a tool using the appropriate package manager."""
    try:
        if dry_run:
            logging.info(f"Would install {tool}")
            return
        if package_manager == "brew":
            subprocess.run(["brew", "install", tool], check=True)
        elif package_manager in ["apt", "yum", "dnf"]:
            subprocess.run(["sudo", package_manager, "install", "-y", tool], check=True)
        else:
            raise Exception("Unsupported package manager")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to install {tool}: {str(e)}")
        raise

def uninstall_tool(tool, package_manager, dry_run=False):
    """Uninstall a tool using the appropriate package manager."""
    try:
        if dry_run:
            logging.info(f"Would uninstall {tool}")
            return
        if package_manager == "brew":
            subprocess.run(["brew", "uninstall", tool], check=True)
        elif package_manager in ["apt", "yum", "dnf"]:
            subprocess.run(["sudo", package_manager, "remove", "-y", tool], check=True)
        else:
            raise Exception("Unsupported package manager")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to uninstall {tool}: {str(e)}")
        raise

def check_system_requirements():
    """Check if the system meets the minimum requirements."""
    min_ram = 4 * 1024 * 1024 * 1024  # 4 GB
    min_disk_space = 20 * 1024 * 1024 * 1024  # 20 GB

    total_ram = psutil.virtual_memory().total
    _, _, disk_space = shutil.disk_usage("/")

    if total_ram < min_ram:
        logging.warning("System RAM is below the recommended minimum of 4 GB")
    if disk_space < min_disk_space:
        logging.warning("Available disk space is below the recommended minimum of 20 GB")

    return total_ram >= min_ram and disk_space >= min_disk_space

def create_backup(backup_dir):
    """Create a simple backup of important system files."""
    important_files = ["/etc/passwd", "/etc/group", "/etc/shadow"]
    os.makedirs(backup_dir, exist_ok=True)
    for file in important_files:
        if os.path.exists(file):
            shutil.copy2(file, backup_dir)
    logging.info(f"Backup created in {backup_dir}")

def check_and_install_dependencies(package_manager):
    """Check and install any required dependencies."""
    dependencies = ["curl", "wget", "git"]
    for dep in dependencies:
        if not is_tool_installed(dep):
            try:
                install_tool(dep, package_manager)
                logging.info(f"Installed dependency: {dep}")
            except Exception as e:
                logging.error(f"Failed to install dependency {dep}: {str(e)}")

def get_tool_version(tool):
    """Get the version of an installed tool."""
    try:
        result = subprocess.run([tool, "--version"], capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "Unknown"

def setup_homebrew_permissions():
    """Set up correct permissions for Homebrew directories."""
    if platform.system() != "Darwin":
        return  # This is only for macOS

    homebrew_dirs = [
        "/opt/homebrew/etc",
        "/opt/homebrew/etc/bash_completion.d",
        "/opt/homebrew/lib/pkgconfig",
        "/opt/homebrew/share/aclocal",
        "/opt/homebrew/share/doc",
        "/opt/homebrew/share/info",
        "/opt/homebrew/share/locale",
        "/opt/homebrew/share/man",
        "/opt/homebrew/share/man/man1",
        "/opt/homebrew/share/man/man3",
        "/opt/homebrew/share/man/man5",
        "/opt/homebrew/share/man/man7",
        "/opt/homebrew/share/man/man8",
        "/opt/homebrew/share/zsh",
        "/opt/homebrew/share/zsh/site-functions",
        "/opt/homebrew/var/homebrew/locks",
        "/opt/homebrew/var/log"
    ]

    current_user = getpass.getuser()

    try:
        # Change ownership
        subprocess.run(["sudo", "chown", "-R", current_user] + homebrew_dirs, check=True)
        
        # Set write permissions
        subprocess.run(["sudo", "chmod", "u+w"] + homebrew_dirs, check=True)
        
        logging.info("Homebrew permissions set up successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to set Homebrew permissions: {str(e)}")
        raise

def is_root():
    """Check if the script is running with root privileges."""
    return os.geteuid() == 0

def check_directory_permissions(package_manager):
    """Check if the script has the necessary permissions for installation directories."""
    if package_manager == "brew":
        return os.access("/opt/homebrew", os.W_OK)
    elif package_manager in ["apt", "yum", "dnf"]:
        return os.access("/usr/bin", os.W_OK)
    return False

def rollback_installation(tool, package_manager):
    """Attempt to rollback the installation of a tool."""
    try:
        uninstall_tool(tool, package_manager)
        logging.info(f"Successfully rolled back installation of {tool}")
    except Exception as e:
        logging.error(f"Failed to rollback installation of {tool}: {str(e)}")

def check_conflicting_software(tools_to_install):
    """Check for any conflicting software that might interfere with the installation."""
    conflicts = {}
    # This is a simplified check. In a real-world scenario, you'd have a more comprehensive list of conflicts.
    conflict_pairs = {
        "nmap": "zenmap",  # Example: nmap conflicts with zenmap
        "wireshark": "tshark"  # Example: wireshark conflicts with tshark
    }
    
    for tool in tools_to_install:
        if tool in conflict_pairs and is_tool_installed(conflict_pairs[tool]):
            conflicts[tool] = conflict_pairs[tool]
    
    return conflicts
