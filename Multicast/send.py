import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2) 

while True:
    group = input("Send message to Group 1 or Group 2: ")
    message = input("Enter your message: ").encode()

    if group == '1':
        sock.sendto(message, ('224.1.1.1', 5005))
    elif group == '2':
        sock.sendto(message, ('224.1.1.2', 5006))
    else:
        print("Invalid group selection!")