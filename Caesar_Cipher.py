def encrypt(plaintext, shift):
    ciphertext = ""

    for ch in plaintext:
        if ch.isalpha(): 
            base = ord('a') if ch.islower() else ord('A')
            ch = chr((ord(ch) - base + shift) % 26 + base)
        ciphertext += ch  

    return ciphertext

def decrypt(ciphertext, shift):
    return encrypt(ciphertext, 26 - shift)  
def main():
    while True:
        print("Choose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = encrypt(plaintext, shift)
            print("Encrypted Text:", encrypted_text)

        elif choice == '2':
            ciphertext = input("Enter the ciphertext: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = decrypt(ciphertext, shift)
            print("Decrypted Text:", decrypted_text)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
