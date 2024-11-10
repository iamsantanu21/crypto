def vigenere_cipher(text, key):
    text = text.replace(" ", "").upper()
    key = key.replace(" ", "").upper()
    encrypted = []
    decrypted = []

    for i, char in enumerate(text):
        text_num = ord(char) - ord('A')
        key_num = ord(key[i % len(key)]) - ord('A')

        encrypted_char = chr((text_num + key_num) % 26 + ord('A'))
        encrypted.append(encrypted_char)

        decrypted_char = chr((ord(encrypted_char) - ord('A') - key_num + 26) % 26 + ord('A'))
        decrypted.append(decrypted_char)

    return ''.join(encrypted), ''.join(decrypted)

text = input("Enter a string: ")
key = input("Enter a key: ")

cipher_text, decrypted_text = vigenere_cipher(text, key)
print("Vigenere Cipher text is:", cipher_text)
print("Decrypted text is:", decrypted_text)