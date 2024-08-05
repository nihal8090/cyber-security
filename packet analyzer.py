def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        
        # Determine the protocol and display relevant information
        if protocol == 6:  # TCP
            protocol_name = "TCP"
            if TCP in packet:
                payload = packet[TCP].payload
        elif protocol == 17:  # UDP
            protocol_name = "UDP"
            if UDP in packet:
                payload = packet[UDP].payload
        else:
            protocol_name = "Other"
            payload = packet[IP].payload

        # Print packet details
        print(f"IP Src: {ip_src} -> IP Dst: {ip_dst} | Protocol: {protocol_name} | Payload: {payload}")

def start_sniffing(interface=None):
    if interface:
        sniff(iface=interface, prn=packet_callback, store=False)
    else:
        sniff(prn=packet_callback, store=False)

# Example usage
if _name_ == "_main_":
    interface = input("Enter the interface to sniff (leave blank for default): ")
    start_sniffing(interface if interface else None)
