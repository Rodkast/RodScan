from scapy import _version_from_git_describe
import scapy.all as scapy

def load_vendor_data(filename="vendor.txt"):
        vendor_dict = {}
        try:
            with open(filename, "r") as f:
                for line in f.readlines():
                    # split the into MAC PREFIX AND VENDOR
                    parts = line.strip().split()
                if len(parts) == 2:
                    mac_prefix = parts[0].strip().lower()
                    vendor_name = " ".joinparts[1].strip()
                    vendor_dict[mac_prefix] = vendor_name
        except FileExistsError:
            print(f"Error: {filename} not found. Please ensure the file exists.")
        return vendor_dict

# Devices class to present the connected one !
class Device:   
    def __init__(self, ip, mac, vendor):
        self.ip = ip
        self.mac = mac
        self.vendor = vendor
    
    def __str__(self):
        return f"{self.ip}\t\t{self.mac}\t\t{self.vendor}"


# Scanning class
class NetworkScanner:
    def __init__(self, network):
        self.network = network
        self.devices = []
        self.vendor_data = load_vendor_data()
        
    # Func. to take the IP range of the network
    def scan(self):
        print("Scanning network....")
        arp_request = scapy.ARP(pdst=self.network)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        
        # Collection of devices
        for sent, received in answered_list:
            mac_prefix = received.hwsrc[:6].lower()
            vendor = self.vendor_data.get(mac_prefix, "Unknown")
            device = Device(received.psrc, received.hwsrc, vendor)
            self.devices.append(device)

    #Display devices
    def display_devices(self):
        print("IP Address\t\tMAC Address\t\tVendor")
        print("--------------------------------------------")
        for device in self.devices: 
             print(f"{device.ip}\t\t{device.mac}\t\t{device.vendor}")
