import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 5001))
s.listen(1)
print("Server is waiting for a connection...")

client, address = s.accept()
data = client.recv(1024).decode()
print(f"Received message: {data}")
response = "Received"
client.sendall(response.encode()) 
s.close()  
