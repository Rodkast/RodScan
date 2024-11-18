from Netscanner import NetworkScanner # Import networkScanner class from scanner.py 
from Netmonitor import Netmonitor     # Importning Netmonitor
import time 
from colorama import init, Fore, Back, Style # type: ignore


def banner():
    banner = """
        *******************************************************
        |_____________________________________________________|
        |            ~   Welcome to RodScan                   |
        |                                                     |
        |       ~  It's a Networking Project in Python.       |   
        |_____________________________________________________|
        |                                                     | 
        |                                      [version: 1.0] |
        *******************************************************
        <If you want to scan for connected devices, use an ip range>
        <For Network monitorting your internet adapter (e.g eth0,wlan)>
"""
    print(banner)
    time.sleep(1)
banner()

def main():
    network = input("Enter the network range to scan (e.g '192.168.1.0/24): ").strip()
    
    scanner = NetworkScanner(network) #scanner instance
    monitor = Netmonitor()            #monitor instance
    
    # Display menu 
    while True:
        print("\nSelect an Option: ")
        print("1. Scan the network")
        print("2. Monitor the network (Packet sniffing)")
        print("3. Exit")
    
    # Get user input for menu   
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            scanner.scan()
            scanner.display_devices()
        
        elif choice == "2":
            monitor.start_monitoring()
            monitor.save_to_html()
            monitor.save_to_pcap()
        elif choice == "3":   
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please select 1,2 or 3. ")

if __name__ == "__main__":
    main()