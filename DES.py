from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext, DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    unpadded_text = unpad(decrypted_text, DES.block_size)
    return unpadded_text

while True:
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    
    choice = int(input("Choose an option (1-3): "))
    
    if choice == 1:
        plaintext = input("Enter the text to encrypt: ").encode('utf-8')
        encrypted_text = des_encrypt(plaintext, key)
        print("Encrypted text (hex):", encrypted_text.hex())
    
    elif choice == 2:
        ciphertext_hex = input("Enter the hex string to decrypt: ")
        ciphertext = bytes.fromhex(ciphertext_hex)
        decrypted_text = des_decrypt(ciphertext, key)
        print("Decrypted text:", decrypted_text.decode('utf-8'))
    
    elif choice == 3:
        exit()
    
    else:
        print("Invalid option, please try again.")