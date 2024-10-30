import socket

message = input("Enter the message: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 5001)) 
s.sendall(message.encode()) 
response = s.recv(1024).decode()
print(response)
s.close()  
