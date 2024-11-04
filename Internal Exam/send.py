import socket
import random

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_keypair():
    p = int(input("\nEnter the p value: "))
    if not is_prime(p):
        p=int(input("\n Entera prime number: "))

    q = int(input("\nEnter the q value: "))
    if not is_prime(q):
        q=int(input("\n Entera prime number: "))
    while p == q:
        q = input("Enter the q (i.e; p =! q): ")
        if not is_prime(q):
            q=int(input("\n Entera prime number: "))

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while not is_prime(e):  
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def RSAencrypt(plaintext, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in plaintext]
    encrypted_string = ','.join(map(str, encrypted_message))
    return encrypted_string


def client():
    message = input("Enter the message: ")
    public_key, private_key = generate_keypair()
    d, n = private_key
    encrypt_message = RSAencrypt(message, public_key)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(f"{encrypt_message}|{d}".encode(),('localhost', 5001))

    response, server_address = s.recvfrom(1024)

    print(f"\nReceived response:", response.decode())
    s.close()

if __name__ == "__main__":
    client()