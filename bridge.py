from scapy.all import sniff, DNS, DNSQR, ICMP
from core.crypto import decrypt_payload

def parse_signal(pkt):
    try:
        # Check for ICMP Ghosting
        if pkt.haslayer(ICMP) and pkt[ICMP].type == 8: # Echo Request
            raw_data = pkt[ICMP].load
            print(f"🏴‍☠️ ICMP Signal: {raw_data.decode()}")
            
        # Check for DNS Ghosting
        elif pkt.haslayer(DNSQR):
            qname = pkt[DNSQR].qname.decode()
            if "updates.google.com" in qname:
                encoded = qname.split(".")[0].replace("v", "=")
                print(f"📡 DNS Signal: {encoded}")
    except Exception:
        pass

print("[-] Socket-Ghost Bridge is live. Watching the shadows...")
sniff(prn=parse_signal, store=0)
