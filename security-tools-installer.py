import argparse
import logging
from rich.console import Console
from rich.panel import Panel
from rich import print as rprint
from rich.progress import Progress
import concurrent.futures
import os
from datetime import datetime

from system_utils import (
    get_package_manager, install_tool, uninstall_tool, check_system_requirements,
    create_backup, check_and_install_dependencies
)
from tool_manager import (
    tools, update_tool_status, get_tools_by_category, get_tool_info,
    get_all_categories
)

console = Console()

def setup_logging():
    """Set up logging configuration."""
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"security_tools_install_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def list_tools():
    """List all available tools."""
    console.print(Panel("Available Security Tools", style="bold magenta"))
    for category in get_all_categories():
        rprint(f"\n[bold]{category}:[/bold]")
        for tool in get_tools_by_category(category):
            info = get_tool_info(tool)
            rprint(f"  - {tool}: {info['description']}")

def show_status():
    """Show installation status of all tools."""
    status = update_tool_status()
    console.print(Panel("Installation Status", style="bold magenta"))
    for tool, info in status.items():
        if info['installed']:
            rprint(f"[green]{tool}: Installed (Version: {info['version']})[/green]")
        else:
            rprint(f"[red]{tool}: Not installed[/red]")

def install_tools(tools_to_install, package_manager):
    """Install specified tools."""
    with Progress() as progress:
        tasks = {tool: progress.add_task(f"[green]Installing {tool}...", total=1) for tool in tools_to_install}
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            future_to_tool = {executor.submit(install_tool, tool, package_manager): tool for tool in tools_to_install}
            for future in concurrent.futures.as_completed(future_to_tool):
                tool = future_to_tool[future]
                try:
                    future.result()
                    progress.update(tasks[tool], advance=1)
                    rprint(f"[green]{tool} has been successfully installed.[/green]")
                except Exception as e:
                    progress.update(tasks[tool], advance=1)
                    rprint(f"[red]Failed to install {tool}. Check the log file for details.[/red]")
                    logging.error(f"Error installing {tool}: {str(e)}")

def uninstall_tools(tools_to_uninstall, package_manager):
    """Uninstall specified tools."""
    for tool in tools_to_uninstall:
        try:
            uninstall_tool(tool, package_manager)
            rprint(f"[green]{tool} has been successfully uninstalled.[/green]")
        except Exception as e:
            rprint(f"[red]Failed to uninstall {tool}. Check the log file for details.[/red]")
            logging.error(f"Error uninstalling {tool}: {str(e)}")

def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="Security Tools Installer")
    parser.add_argument("--install", nargs="+", help="Specify tools to install")
    parser.add_argument("--uninstall", nargs="+", help="Specify tools to uninstall")
    parser.add_argument("--category", help="Install all tools in a specific category")
    parser.add_argument("--list", action="store_true", help="List all available tools")
    parser.add_argument("--status", action="store_true", help="Show installation status of all tools")
    parser.add_argument("--yes", action="store_true", help="Automatically answer yes to all prompts")
    args = parser.parse_args()

    if args.list:
        list_tools()
        return

    if args.status:
        show_status()
        return

    package_manager = get_package_manager()
    if not package_manager:
        rprint("[red]Error: Unsupported operating system or package manager not found.[/red]")
        return

    if not check_system_requirements():
        if not args.yes:
            proceed = console.input("[yellow]System does not meet minimum requirements. Do you want to proceed anyway? [y/N]: [/yellow]")
            if proceed.lower() != 'y':
                rprint("[red]Installation cancelled.[/red]")
                return

    check_and_install_dependencies()

    tools_to_process = []
    if args.install:
        tools_to_process = [tool for tool in args.install if tool in tools]
    elif args.uninstall:
        tools_to_process = [tool for tool in args.uninstall if tool in tools]
    elif args.category:
        tools_to_process = get_tools_by_category(args.category)
    else:
        tools_to_process = list(tools.keys())

    if not tools_to_process:
        rprint("[yellow]No valid tools specified for processing.[/yellow]")
        return

    action = "uninstall" if args.uninstall else "install"
    console.print(Panel(f"Security Tools {action.capitalize()}", style="bold magenta"))
    
    rprint(f"[yellow]This script will attempt to {action} the following tools:[/yellow]")
    for tool in tools_to_process:
        rprint(f"  - {tool}")
    
    if not args.yes:
        proceed = console.input(f"\nDo you want to proceed with {action}? [y/N]: ")
        if proceed.lower() != 'y':
            rprint(f"[red]{action.capitalize()} cancelled.[/red]")
            return

    backup_dir = os.path.join("backups", datetime.now().strftime('%Y%m%d_%H%M%S'))
    create_backup(backup_dir)

    if args.uninstall:
        uninstall_tools(tools_to_process, package_manager)
    else:
        install_tools(tools_to_process, package_manager)

    update_tool_status()

    rprint(f"\n[bold green]{action.capitalize()} process completed. Please check the log file for any errors or warnings.[/bold green]")
    rprint("[bold]You can view the installation status anytime by running this script with the --status flag.[/bold]")

if __name__ == "__main__":
    main()
