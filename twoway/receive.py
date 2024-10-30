import socket
import threading
def send():
    while True:
        message = input("Enter the message: ")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 5001)) 
        s.sendall(message.encode()) 
        response = s.recv(1024).decode()
        print(f"\n{response}")
        s.close()  
        
def receive():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 5002))
    s.listen(1)
    print("Server is waiting for a connection...")
    while True:
        client, address = s.accept()
        data = client.recv(1024).decode()
        print(f"\nReceived message: {data}")
        response = "Received"
        client.sendall(response.encode()) 
        client.close()  

if __name__ == "__main__":
    threading.Thread(target=send).start()
    threading.Thread(target=receive).start()