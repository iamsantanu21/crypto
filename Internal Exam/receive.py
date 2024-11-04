import socket

def Caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            ch = chr((ord(ch) - base + shift) % 26 + base)
        ciphertext += ch 
    return ciphertext

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('localhost', 5001))

    data, address = s.recvfrom(1024)
    data = data.decode()
    message ,d = data.split('|')
    d = int(d)
    d = d % 26
    print(f"\nReceived message: {message}")
    print(f"\nShift value: {d}")
    response = input("Enter the reply message: ")
    encrypted_response = Caesar_encrypt(response, d)
    s.sendto(encrypted_response.encode(), address)
    s.close()

if __name__ == "__main__":
    server()