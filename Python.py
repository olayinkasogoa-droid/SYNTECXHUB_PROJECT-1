from scapy.all import ARP, Ether, srp

def scan_network(target_ip):
    # Create ARP request
    arp = ARP(pdst=target_ip)

    # Broadcast MAC address
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether / arp

    # Send packet and capture response
    result = srp(packet, timeout=3, verbose=0)[0]

    # List of clients
    clients = []

    for sent, received in result:
        clients.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return clients


if __name__ == "__main__":
    # Change this if your network is different
    target = "192.168.1.0/24"

    print(f"Scanning network: {target}\n")

    devices = scan_network(target)

    print("Active devices found:\n")
    print("IP Address\t\tMAC Address")
    print("-" * 40)

    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")
