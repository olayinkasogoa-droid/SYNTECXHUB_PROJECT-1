import socket

# Get target and port range from user
target = input("192.168.1.132: ")
start_port = int(input("20: "))
end_port = int(input("100: "))

# Open log file
with open("scan_results.txt", "w") as logfile:

    print(f"\nScanning {target}...\n")
    logfile.write(f"Scan Results for {target}\n")

    for port in range(start_port, end_port + 1):

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"Port {port} is OPEN")
                logfile.write(f"Port {port} is OPEN\n")
            else:
                print(f"Port {port} is CLOSED")
                logfile.write(f"Port {port} is CLOSED\n")

            sock.close()

        except Exception as e:
            print(f"Error scanning port {port}: {e}")
