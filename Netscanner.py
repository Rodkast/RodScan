import scapy.all as scapy


# Devices class to present the connected one !
class Device:   
    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac
    
    def __str__(self):
        return f"{self.ip}\t\t{self.mac}"
    
# Scanning class
class NetworkScanner:
    def __init__(self, network):
        self.network = network
        self.devices = []
        
    # Func. to take the IP range of the network
    def scan(self):
        print("Scanning network....")
        arp_request = scapy.ARP(pdst=self.network)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False, iface="eth0")[0]
        
        # Collection of devices
        for sent, received in answered_list:
            device = Device(received.psrc, received.hwsrc)
            self.devices.append(device)
        
    #Display devices
    def display_devices(self):
        print("IP Address\t\tMAC Address")
        print("-------------------------")
        for device in self.devices: 
            print(device)