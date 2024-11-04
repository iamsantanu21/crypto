import numpy as np

SIZE = 3

def letter_to_number(letter):
    return ord(letter.upper()) - ord('A')

def number_to_letter(number):
    return chr(number + ord('A'))

def mod26(x):
    return x % 26

def string_to_key_matrix(key_string):
    key_matrix = np.zeros((SIZE, SIZE), dtype=int)
    idx = 0
    for i in range(SIZE):
        for j in range(SIZE):
            key_matrix[i][j] = letter_to_number(key_string[idx])
            idx += 1
    return key_matrix

def encrypt(plaintext, key):
    plaintext_vector = np.array([letter_to_number(char) for char in plaintext]).reshape(SIZE, 1)
    cipher_vector = mod26(np.dot(key, plaintext_vector))
    ciphertext = ''.join(number_to_letter(num) for num in cipher_vector.flatten())
    return ciphertext

def find_determinant(matrix):
    det = int(np.round(np.linalg.det(matrix)))
    return mod26(det)

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def find_inverse_matrix(key):
    det = find_determinant(key)
    det_inv = mod_inverse(det, 26)
    if det_inv == -1:
        return None

    cofactor_matrix = np.linalg.inv(key).T * det
    adjugate = mod26(np.round(cofactor_matrix).astype(int))
    inverse_key = mod26(adjugate * det_inv)
    return inverse_key

def decrypt(ciphertext, inverse_key):
    return encrypt(ciphertext, inverse_key)

def main():
    while True:
        print("\nMenu:")
        print("1. Encrypt Text (3 characters)")
        print("2. Decrypt Text (3 characters)")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key_string = input("Enter a 9-character key string: ").upper()
            if len(key_string) != SIZE * SIZE:
                print("Error: Key must be exactly 9 characters.")
                continue

            key = string_to_key_matrix(key_string)
            plaintext = input("Enter 3-character plaintext: ").upper()
            if len(plaintext) != SIZE:
                print("Error: Please enter exactly 3 characters.")
                continue

            ciphertext = encrypt(plaintext, key)
            print("Encrypted text:", ciphertext)

        elif choice == 2:
            key_string = input("Enter a 9-character key string: ").upper()
            if len(key_string) != SIZE * SIZE:
                print("Error: Key must be exactly 9 characters.")
                continue

            key = string_to_key_matrix(key_string)
            inverse_key = find_inverse_matrix(key)
            if inverse_key is None:
                print("Inverse of the key matrix does not exist!")
                continue

            ciphertext = input("Enter 3-character ciphertext: ").upper()
            if len(ciphertext) != SIZE:
                print("Error: Please enter exactly 3 characters.")
                continue

            decrypted_text = decrypt(ciphertext, inverse_key)
            print("Decrypted text:", decrypted_text)

        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()