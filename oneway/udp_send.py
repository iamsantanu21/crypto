import socket

message = input("Enter the message: ")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(message.encode(), ('localhost', 5001))
response, server_address = s.recvfrom(1024)
print("Server response:", response.decode())
s.close()
