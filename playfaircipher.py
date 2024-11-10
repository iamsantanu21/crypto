import re

def generate_key_matrix(key):
    matrix = []
    key = key.replace("J", "I")  
    key = "".join(sorted(set(key), key=lambda x: key.index(x))) 
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_matrix = key + "".join([char for char in alphabet if char not in key])
    for i in range(0, 25, 5):
        matrix.append(list(key_matrix[i:i+5]))
    return matrix

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def prepare_text(text):
    text = re.sub(r'[^A-Z]', '', text.upper())
    text = text.replace("J", "I") 
    prepared_text = ""
    i = 0
    while i < len(text):
        prepared_text += text[i]
        if i+1 < len(text) and text[i] == text[i+1]:
            prepared_text += "X"  
        elif i+1 < len(text):
            prepared_text += text[i+1]
        i += 2
    if len(prepared_text) % 2 != 0:
        prepared_text += "X"  
    return prepared_text

def encrypt(text, key):
    matrix = generate_key_matrix(key)
    prepared_text = prepare_text(text)
    result = ""
    for i in range(0, len(prepared_text), 2):
        char1, char2 = prepared_text[i], prepared_text[i+1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        if row1 == row2:
            result += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    return result

def decrypt(text, key):
    matrix = generate_key_matrix(key)
    prepared_text = prepare_text(text)
    result = ""
    for i in range(0, len(prepared_text), 2):
        char1, char2 = prepared_text[i], prepared_text[i+1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2) 
        if row1 == row2:
            result += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    return result

def main():
    while True:
        print("\nMenu:")
        print("1. Encrypt Text (3 characters)")
        print("2. Decrypt Text (3 characters)")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            text = input("Enter text: ").strip().upper()
            key = input("Enter key: ").strip().upper()
            print("Encrypted Text:", encrypt(text, key))
        elif choice == 2:
            text = input("Enter text: ").strip().upper()
            key = input("Enter key: ").strip().upper()
            print("Decrypted Text:", decrypt(text, key))
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()
