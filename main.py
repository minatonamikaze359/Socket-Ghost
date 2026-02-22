import argparse
from core.banner import show_banner
from core.dev import show_dev
from core.engine import SocketGhost # Import your upgraded engine

def main():
    show_banner()
    
    parser = argparse.ArgumentParser(description="Socket-Ghost Framework")
    parser.add_argument("--target", help="Remote Receiver IP")
    parser.add_argument("--data", help="Payload to transmit")
    parser.add_argument("--about", action="store_true", help="Display developer info")
    
    args = parser.parse_args()

    if args.about:
        show_dev()
        return

    if args.target and args.data:
        # Implementation of your ghosting logic here
        print(f"[*] Dispatching ghost signal to {args.target}...")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
