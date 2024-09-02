import platform
import shutil
import subprocess
import logging
import os

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

def install_tool(tool, package_manager):
    """Install a tool using the appropriate package manager."""
    try:
        if package_manager == "brew":
            subprocess.run(["brew", "install", tool], check=True)
        elif package_manager in ["apt", "yum", "dnf"]:
            subprocess.run(["sudo", package_manager, "install", "-y", tool], check=True)
        else:
            raise Exception("Unsupported package manager")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to install {tool}: {str(e)}")
        raise

def uninstall_tool(tool, package_manager):
    """Uninstall a tool using the appropriate package manager."""
    try:
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
    # This is a placeholder. You should define specific requirements for your tools.
    min_ram = 4 * 1024 * 1024 * 1024  # 4 GB
    min_disk_space = 20 * 1024 * 1024 * 1024  # 20 GB

    total_ram = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    _, _, disk_space = shutil.disk_usage("/")

    if total_ram < min_ram:
        logging.warning("System RAM is below the recommended minimum of 4 GB")
    if disk_space < min_disk_space:
        logging.warning("Available disk space is below the recommended minimum of 20 GB")

    return total_ram >= min_ram and disk_space >= min_disk_space

def create_backup(backup_dir):
    """Create a simple backup of important system files."""
    # This is a placeholder. You should define which files to backup based on your needs.
    important_files = ["/etc/passwd", "/etc/group", "/etc/shadow"]
    os.makedirs(backup_dir, exist_ok=True)
    for file in important_files:
        if os.path.exists(file):
            shutil.copy2(file, backup_dir)
    logging.info(f"Backup created in {backup_dir}")

def check_and_install_dependencies():
    """Check and install any required dependencies."""
    # This is a placeholder. You should define the dependencies for your tools.
    dependencies = ["curl", "wget", "git"]
    package_manager = get_package_manager()
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

