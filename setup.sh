#!/bin/bash
# Socket-Ghost Advanced Setup
printf "\033[1;31m💀 Initializing Socket-Ghost Environment...\033[0m\n"

pkg update && pkg upgrade -y
pkg install python libpcap libffi openssl -y

pip install scapy cryptography colorama

# Create directory structure
mkdir -p core logs wordlists
touch logs/ghost.log

echo "[+] System Ready. Use 'python ghost.py --help' for instructions."
