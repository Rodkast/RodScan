import scapy.all as scapy
from scapy.layers.l2 import ARP   # Corrected import for ARP
from scapy.layers.inet import IP  # IP is still imported from inet

class Netmonitor:
    def __init__(self):
        self.monitored_devices = []
        self.sniffed_data = []
        self.packets = []
    
    # Packet sniffing and monitoring 
    def packet_sniff(self,packet):
        if packet.haslayer(ARP):
            # Monitor ARP Packets.
            if packet[ARP].op == 1:      # ARP request
                packet_info = f"ARP request from {packet[ARP].hwsrc} ({packet[ARP].psrc})"
                print(f"Captured: {packet_info}")
            elif packet[ARP].op == 2:    # ARP reply
                packet_info = f"ARP Reply from {packet[ARP].hwsrc}({packet[ARP].psrc})"
                print(f"Captured: {packet_info}")
            self.sniffed_data.append(packet_info)
        
        
        elif packet.haslayer(IP):        #Monitor IP packets
            packet_info = f"IP Packet: {packet[IP].src} -> {packet[IP].dst}"    
            print(f"Captured: {packet_info}")
            self.sniffed_data.append(packet_info)
            #print(f"IP Packet: {packet[IP].src} -> {packet[IP].dst}")
            
        self.packets.append(packet)
        print(f"Total packets captured: {len(self.packets)}")
    def start_monitoring(self):
        print("Monitoring network.... Press Ctrl+C to stop. ")
        interface = input("Enter the network interface (e.g., eth0, wlan0): ")
        scapy.sniff(prn=self.packet_sniff, store=0, filter="ip or arp", iface=interface)
        #scapy.sniff(prn=self.package_sniff, store= 0, filter="ip or arp") #sniff IP & ARP packets.

# Save results into HTML file.
    def save_to_html(self):
        if not self.sniffed_data:
            print("No data to save.")
        # Add some basic CSS to style the page
        html_content = """
<html>
    <head>
        <title>Network Monitoring Results</title>
        <style>
            body {
                font-family: 'Courier New', Courier, monospace;
                background-color: #181818;  /* Dark background */
                color: #e5e5e5;  /* Light text color for contrast */
                margin: 0;
                padding: 0;
                line-height: 1.6;
            }
            h1 {
                color: #9b59b6;  /* Purple color for title */
                text-align: center;
                font-size: 3em;
                margin-top: 30px;
                letter-spacing: 2px;
                text-shadow: 0 0 10px rgba(155, 89, 182, 0.8); /* Neon glow effect */
            }
            .container {
                width: 85%;
                margin: 40px auto;
                padding: 30px;
                background-color: #2e2e2e;  /* Dark gray container */
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
                border-radius: 10px;
                border: 2px solid #9b59b6;  /* Purple border */
            }
            ul {
                list-style-type: none;
                padding: 0;
                margin: 0;
            }
            li {
                background-color: #333;  /* Dark gray background for items */
                margin: 10px 0;
                padding: 15px;
                border-radius: 8px;
                font-size: 1.1em;
                color: #ddd;  /* Slightly lighter text */
                word-wrap: break-word;
                border-left: 5px solid #9b59b6;  /* Purple left border for effect */
            }
            li:nth-child(odd) {
                background-color: #242424;  /* Slightly lighter background for odd items */
            }
            li:hover {
                background-color: #3a3a3a;  /* Hover effect */
                cursor: pointer;
                transform: scale(1.05);
                transition: all 0.3s ease;
            }
            .footer {
                text-align: center;
                font-size: 1em;
                color: #777;
                margin-top: 40px;
                padding: 10px 0;
                background-color: #222;
            }
            .footer p {
                color: #9b59b6;  /* Purple text for footer */
                font-size: 1em;
            }
            .container ul {
                padding-left: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Network Monitoring Results</h1>
        <div class="container">
            <ul>
"""

        
        # Append each packet sniffed to the HTML content as a list item
        for packet_info in self.sniffed_data:
            html_content += f"<li>{packet_info}</li>\n"
        
        html_content += """
                    </ul>
                </div>
                <div class="footer">
                    <p>Generated by Network Monitor</p>
                </div>
            </body>
        </html>
        """
        
        # Write the HTML content to a file
        try:
            with open("network_monitoring_results.html", "w") as html_file:
                html_file.write(html_content)
            print("Monitoring results saved to 'network_monitoring_results.html'.")
        except Exception as e:
            print(f"Error Saving HTML File: {e}")
    
    # Write the results in a .pcap file
    def save_to_pcap(self):
        if not self.packets:
            print("No packets to save to .pcap.")
            return
        
        try:
            scapy.wrpcap("network_monitoring_results.pcap", self.packets)
            print("Monitorinf results saved to 'network_monitoring_results.pcap'.")  
        except Exception as e:
            print("Error saving .pcap file: {e}")