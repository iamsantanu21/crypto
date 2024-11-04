def vigenere_cipher(text, key):
    text = text.replace(" ", "").upper()   # Remove spaces and convert to uppercase
    key = key.replace(" ", "").upper()
    encrypted = []
    decrypted = []

    for i, char in enumerate(text):
        text_num = ord(char) - ord('A')
        key_num = ord(key[i % len(key)]) - ord('A')

        # Encryption
        encrypted_char = chr((text_num + key_num) % 26 + ord('A'))
        encrypted.append(encrypted_char)

        # Decryption (based on encrypted character)
        decrypted_char = chr((ord(encrypted_char) - ord('A') - key_num + 26) % 26 + ord('A'))
        decrypted.append(decrypted_char)

    return ''.join(encrypted), ''.join(decrypted)

# Get user input for text and key
text = input("Enter a string: ")
key = input("Enter a key: ")

# Get both encrypted and decrypted text
cipher_text, decrypted_text = vigenere_cipher(text, key)
print("Vigenere Cipher text is:", cipher_text)
print("Decrypted text is:", decrypted_text)