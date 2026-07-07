import requests
import json
import time
import sys
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

def print_banner():
    print(Fore.CYAN + "="*40)
    print(Fore.WHITE + Style.BRIGHT + "   DISCORD AUTHENTICATION TOOL v1.0")
    print(Fore.CYAN + "="*40 + "\n")

def get_discord_token(email, password):
    url = "https://discord.com/api/v9/auth/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/json"
    }
    payload = {"login": email, "password": password}

    print(Fore.YELLOW + "[*] " + Style.RESET_ALL + "Connecting to Discord...")
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        if response.status_code == 200:
            return True, data.get("token")
        else:
            return False, data.get("message", "Unknown error")
    except Exception as e:
        return False, str(e)

if __name__ == "__main__":
    print_banner()
    
    email = input(Fore.BLUE + "[?] " + Style.RESET_ALL + "Enter Email    : ")
    password = input(Fore.BLUE + "[?] " + Style.RESET_ALL + "Enter Password : ")
    print("")

    success, result = get_discord_token(email, password)

    if success:
        print(Fore.GREEN + "[+] " + Style.BRIGHT + "Login Successful!")
        print(Fore.CYAN + "-"*40)
        print(f"TOKEN: {Fore.WHITE}{result}")
        print(Fore.CYAN + "-"*40)
    else:
        print(Fore.RED + "[!] " + Style.BRIGHT + "Login Failed!")
        print(Fore.RED + f"Reason: {result}")
