import socket


def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((host, port))
    sock.close()

    if result == 0:
        return "open"

    return "closed"


if __name__ == "__main__":
    host = "127.0.0.1"

    for port in [22, 80, 443]:
        status = scan_port(host, port)
        print(f"{host}:{port} - {status}")