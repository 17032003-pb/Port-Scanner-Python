import socket
import datetime

def scan_target(target, ports):
    print(f"\n[+] Starting Scan on Target: {target}")
    print(f"[+] Time started: {str(datetime.datetime.now())}")
    print("-" * 50)

    for port in ports:
        try:
            # Create a socket object (IPv4, TCP)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Set a timeout so we don't wait forever if the port is closed
            s.settimeout(1)
            
            # Try to connect (returns 0 if successful)
            result = s.connect_ex((target, port))
            
            if result == 0:
                print(f"  [OPEN] Port {port} is OPEN")
            else:
                print(f"  [CLOSED] Port {port}")
            
            s.close()
            
        except KeyboardInterrupt:
            print("\n[!] Exiting Program.")
            break
        except socket.gaierror:
            print("\n[!] Hostname could not be resolved.")
            break
        except socket.error:
            print("\n[!] Could not connect to server.")
            break

def main():
    # Ask user for target
    target_input = input("Enter target IP or URL (e.g., scanme.nmap.org): ")
    
    # Translate URL to IP address
    try:
        target_ip = socket.gethostbyname(target_input)
    except socket.gaierror:
        print("[!] Invalid Target.")
        return

    # List of common ports to scan
    # 21=FTP, 22=SSH, 80=HTTP, 443=HTTPS, 3389=RDP
    common_ports = [21, 22, 23, 25, 53, 80, 443, 3389, 8080]

    scan_target(target_ip, common_ports)

    input("\nScan Complete. Press Enter to exit...")

if __name__ == "__main__":
    main()
git init
git add port_scanner.py
git commit -m "Added Python Port Scanner tool"
git branch -M main
git remote add origin 
https://github.com/17032003-pb/Port-Scanner-Pythongit push -origin main