count ={}
services = {"443": "HTTPS", "53": "DNS", "22": "SSH", "8080": "HTTP-alt", "3389": "RDP"}
try:
    with open ("connections.log", "r") as f:
        for line in f:
            parts = line.split()
            port= parts[-1]
            if port in count:
                count [port]= count[port] + 1
            else:
                count[port]= 1
except FileNotFoundError:
    print("Log File Not Found. Check The File Name And Folder")
else:
    for port, total in count.items():
        name = services.get(port, "unknown")
        print(f"port {port} ({name}): {total} connections")
        if (port == "22" or port == "3389") and total >= 3:
            print(f"alert: repeated connections to port {port}({name}): {total}")