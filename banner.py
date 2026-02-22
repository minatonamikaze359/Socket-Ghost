import sys
import time
import random

def fade_text(text):
    """Applies a purple-to-blue gradient effect (Terminal RGB)."""
    lines = text.split('\n')
    for line in lines:
        # Shift colors slightly per line for a vertical gradient
        r, g, b = 150, 0, 255
        for char in line:
            # ANSI escape for true color (RGB)
            sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}")
            r = max(0, r - 2)
            b = min(255, b + 5)
        sys.stdout.write("\n")
        sys.stdout.flush()
        time.sleep(0.05)

def show_banner():
    banner = r"""
    SHADOW-PROTOCOL v2.0
     __________
    |  ______  |    SOCKET-GHOST
    | |      | |    [ STATUS: STEALTH ]
    | |      | |    [ ENGINE: ASYNC   ]
    | |______| |    [ MODE: MULTI-V   ]
    |__________|
     |        |     "In the silence, 
     |________|      the data flows."
    """
    
    fade_text(banner)
    print("\033[0m") # Reset colors
    print("-" * 45)
    
    loading_msg = "[*] Synchronizing ghost-bridge..."
    for char in loading_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print(" [OK]")
    print("-" * 45 + "\n")

if __name__ == "__main__":
    show_banner()
