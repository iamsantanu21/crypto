def vigenere_encrypt(text, key):
    text = text.replace(" ", "").upper()   # Remove spaces and convert to uppercase
    key = key.replace(" ", "").upper()
    result = []

    for i, char in enumerate(text):
        text_num = ord(char) - ord('A')
        key_num = ord(key[i % len(key)]) - ord('A')
        new_char = chr((text_num + key_num) % 26 + ord('A'))  # Encrypt character
        result.append(new_char)

    return ''.join(result)

def vigenere_decrypt(cipher_text, key):
    cipher_text = cipher_text.replace(" ", "").upper()   # Remove spaces and convert to uppercase
    key = key.replace(" ", "").upper()
    result = []

    for i, char in enumerate(cipher_text):
        cipher_num = ord(char) - ord('A')
        key_num = ord(key[i % len(key)]) - ord('A')
        new_char = chr((cipher_num - key_num + 26) % 26 + ord('A'))  # Decrypt character
        result.append(new_char)

    return ''.join(result)


# Get user input for text and key
text = input("Enter a string: ")
key = input("Enter a key: ")

# Encrypt the text
cipher_text = vigenere_encrypt(text, key)
print("Vigenere Cipher text is:", cipher_text)

# Decrypt the text
decrypted_text = vigenere_decrypt(cipher_text, key)
print("Decrypted text is:", decrypted_text)