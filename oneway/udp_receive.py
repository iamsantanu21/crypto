import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 5001))
print("UDP Server is waiting for a message...")
data, client_address = s.recvfrom(1024)
print(f"Received message: {data.decode()}")
response = "Message received"
s.sendto(response.encode(), client_address)
s.close()