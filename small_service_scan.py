import socket
import sys

def check_tcp_small_services(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((host, 7))
        print("TCP small services are enabled on host: ", host)
    except socket.error:
        print("TCP small services are disabled on host: ", host)
    s.close()

def check_udp_small_services(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(5)
    try:
        s.connect((host, 7))
        print("UDP small services are enabled on host: ", host)
    except socket.error:
        print("UDP small services are disabled on host: ", host)
    s.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <host IP> <-t or -u>")
    else:
        host = sys.argv[1]
        protocol = sys.argv[2]
        if protocol == "-t":
            check_tcp_small_services(host)
        elif protocol == "-u":
            check_udp_small_services(host)
        else:
            print("Invalid protocol flag. Use -t for TCP or -u for UDP")
