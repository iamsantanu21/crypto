SIZE = 3

def letter_to_number(letter):
    return ord(letter.upper()) - ord('A')

def number_to_letter(number):
    return chr(number + ord('A'))

def mod26(a):
    return (a % 26 + 26) % 26

def encrypt(plaintext, key):
    plaintext_vector = [letter_to_number(plaintext[j]) for j in range(SIZE)]
    cipher_vector = [0] * SIZE

    for j in range(SIZE):
        for k in range(SIZE):
            cipher_vector[j] += key[j][k] * plaintext_vector[k]
        cipher_vector[j] = mod26(cipher_vector[j])

    ciphertext = ''.join(number_to_letter(cipher_vector[j]) for j in range(SIZE))
    return ciphertext

def string_to_key_matrix(key_string):
    key = [[0] * SIZE for _ in range(SIZE)]
    idx = 0
    for i in range(SIZE):
        for j in range(SIZE):
            key[i][j] = letter_to_number(key_string[idx])
            idx += 1
    return key

def find_determinant(matrix):
    det = (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
           matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
           matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
    return mod26(det)

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def find_cofactor_matrix(matrix):
    cofactor = [[0] * SIZE for _ in range(SIZE)]
    cofactor[0][0] = mod26(matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
    cofactor[0][1] = mod26(-(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]))
    cofactor[0][2] = mod26(matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    cofactor[1][0] = mod26(-(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1]))
    cofactor[1][1] = mod26(matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0])
    cofactor[1][2] = mod26(-(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0]))
    cofactor[2][0] = mod26(matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1])
    cofactor[2][1] = mod26(-(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]))
    cofactor[2][2] = mod26(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
    return cofactor

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(SIZE)] for i in range(SIZE)]

def find_inverse_matrix(key):
    det = find_determinant(key)
    det_inv = mod_inverse(det, 26)
    if det_inv == -1:
        return None

    cofactor = find_cofactor_matrix(key)
    adjugate = transpose_matrix(cofactor)

    inverse = [[mod26(adjugate[i][j] * det_inv) for j in range(SIZE)] for i in range(SIZE)]
    return inverse

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
            key_string = input("Enter a 9-character key string: ")
            key = string_to_key_matrix(key_string)
            while True:
                text = input("Enter 3-character plaintext: ")
                if len(text) == SIZE:
                    break
                print("Error: Please enter exactly 3 characters.")
            result = encrypt(text, key)
            print("Encrypted text:", result)

        elif choice == 2:
            key_string = input("Enter a 9-character key string: ")
            key = string_to_key_matrix(key_string)
            while True:
                text = input("Enter 3-character ciphertext: ")
                if len(text) == SIZE:
                    break
                print("Error: Please enter exactly 3 characters.")

            inverse_key = find_inverse_matrix(key)
            if inverse_key is None:
                print("Inverse of the key matrix does not exist!")
                continue

            result = decrypt(text, inverse_key)
            print("Decrypted text:", result)

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()
