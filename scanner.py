import socket


def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((host, port))
    sock.close()

    return result == 0


def scan_ports(host, ports):
    results = {}

    for port in ports:
        results[port] = scan_port(host, port)

    return results


if __name__ == "__main__":
    host = "127.0.0.1"
    ports = [22, 80, 443, 8080]

    results = scan_ports(host, ports)

    for port, is_open in results.items():
        status = "OPEN" if is_open else "CLOSED"
        print(f"{host}:{port} - {status}")
        