import time
import sys

def lightning_print(text, speed=0.01):
    """Prints text with a 'flash' speed effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def show_dev():
    # Colors: Yellow (\033[93m), Blue (\033[94m), Reset (\033[0m)
    yellow = "\033[93m"
    blue = "\033[94m"
    bold = "\033[1m"
    reset = "\033[0m"

    print(f"\n{yellow}{'='*50}{reset}")
    lightning_print(f"{bold}👤 LEAD ARCHITECT: MINATO NAMIKAZE{reset}")
    lightning_print(f"{blue}🏷️ ALIAS: The Yellow Flash of the Net{reset}")
    print(f"{yellow}{'='*50}{reset}")

    info = [
        "◈ Role: Senior Security Researcher & Developer",
        "◈ Specialty: Stealth Tunneling & Network Infiltration",
        "◈ Philosophy: 'Speed is the ultimate security.'",
        "◈ GitHub: https://github.com/Minato-Namikaze",
    ]

    for line in info:
        time.sleep(0.1)
        print(f" {line}")

    print(f"\n{yellow}[⚡] Hiraishin Seal Active: System secured.{reset}\n")

if __name__ == "__main__":
    show_dev()
