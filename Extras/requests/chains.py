import os
import platform
import subprocess
import pyfiglet
from termcolor import colored
import shutil
import sys

def print_ascii_art():
    ascii_art = pyfiglet.figlet_format("PsDev")
    blue_ascii_art = colored(ascii_art, "blue")
    print(blue_ascii_art)

def install_proxychains_linux():
    try:
        subprocess.run(["proxychains", "--version"], capture_output=True, check=True)
        print("ProxyChains is already installed.")
    except FileNotFoundError:
        print("ProxyChains is not installed. Installing it now...")
        if os.system("sudo apt-get install -y proxychains") == 0:
            print("ProxyChains installed successfully.")
        else:
            print("Failed to install ProxyChains. Please install it manually.")
            sys.exit(1)

        # Add proxychains to PATH environment
        os.system("echo 'export PATH=$PATH:/usr/bin' >> ~/.bashrc")
        os.system("source ~/.bashrc")

def install_proxychains_windows():
    proxychains_url = "https://github.com/haad/proxychains-ng/releases/download/v4.14/proxychains-4.14.zip"
    proxychains_zip = "proxychains-4.14.zip"
    proxychains_dir = "proxychains-4.14"
    proxychains_config = "proxychains.conf"

    try:
        subprocess.run(["proxychains", "--version"], capture_output=True, check=True)
        print("ProxyChains is already installed.")
    except FileNotFoundError:
        print("ProxyChains is not installed. Installing it now...")
        os.system(f"curl -LO {proxychains_url}")
        os.system(f"md {proxychains_dir}")
        os.system(f"Expand-Archive -Path {proxychains_zip} -DestinationPath {proxychains_dir}")

        # Move proxychains executable to a location in the system PATH
        proxychains_bin = os.path.join(proxychains_dir, "proxychains4.exe")
        system_path = os.environ["PATH"].split(";")
        for path in system_path:
            if path.lower() == proxychains_dir.lower():
                break
        else:
            shutil.move(proxychains_bin, os.path.join(os.environ["SystemRoot"], "System32"))
            print("ProxyChains installed successfully.")

        # Add proxychains to System Variables
        os.system(f"setx PATH \"%PATH%;{os.path.abspath(proxychains_dir)}\"")
        os.system("refreshenv")

    except Exception as e:
        print(f"Failed to install ProxyChains: {str(e)}. Please install it manually.")
        sys.exit(1)

def main():
    print_ascii_art()

    os_name = platform.system()

    if os_name == "Linux":
        install_proxychains_linux()
    elif os_name == "Windows":
        install_proxychains_windows()
    else:
        print("This script is intended to work on Windows and Linux only.")
        sys.exit(1)

    try:
        subprocess.run(["proxychains", "--version"], capture_output=True, check=True)
        print("ProxyChains setup completed.")
    except FileNotFoundError:
        print("ProxyChains is not installed or not in the system PATH. Please install it manually.")
        sys.exit(1)

if __name__ == "__main__":
    main()