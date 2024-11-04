#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define SIZE 3 

int letterToNumber(char letter) {
    return toupper(letter) - 'A';
}

char numberToLetter(int number) {
    return number + 'A';
}

int mod26(int a) {
    return (a % 26 + 26) % 26;
}

void Encrypt(char plaintext[], int key[SIZE][SIZE], char ciphertext[]) {
    int i, j, k;
    int plaintextVector[SIZE], cipherVector[SIZE];

    for (j = 0; j < SIZE; j++) {
        plaintextVector[j] = letterToNumber(plaintext[j]); //plaintext letter to number convart
    }
    //key matrix multiply with plaintext then mod 26 
    for (j = 0; j < SIZE; j++) {
        cipherVector[j] = 0;
        for (k = 0; k < SIZE; k++) {
            cipherVector[j] += key[j][k] * plaintextVector[k];
        }
        cipherVector[j] = mod26(cipherVector[j]);  // Modulo 26
    }
    //ciphertext number back to characters.
    for (j = 0; j < SIZE; j++) {
        ciphertext[j] = numberToLetter(cipherVector[j]);
    }
    ciphertext[SIZE] = '\0';
}
//convert the string to number
void stringToKeyMatrix(char keyString[], int key[SIZE][SIZE]) {
    int idx = 0;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            key[i][j] = letterToNumber(keyString[idx]);
            idx++;
        }
    }
}
//find determinant of key matrix
int findDeterminant(int matrix[SIZE][SIZE]) {
    int det = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
              matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
              matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);
    return mod26(det);
}
//ffind the inverse value tp multiply  with the determinant

int modInverse(int a, int m) {
    a = a % m;
    for (int x = 1; x < m; x++) {
        if ((a * x) % m == 1) {
            return x;
        }
    }
    return -1;
}

void findCofactorMatrix(int matrix[SIZE][SIZE], int cofactor[SIZE][SIZE]) {
    cofactor[0][0] = mod26(matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]);
    cofactor[0][1] = mod26(-(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]));
    cofactor[0][2] = mod26(matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);
    cofactor[1][0] = mod26(-(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1]));
    cofactor[1][1] = mod26(matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]);
    cofactor[1][2] = mod26(-(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0]));
    cofactor[2][0] = mod26(matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]);
    cofactor[2][1] = mod26(-(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]));
    cofactor[2][2] = mod26(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]);
}

void transposeMatrix(int matrix[SIZE][SIZE], int transposed[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            transposed[i][j] = matrix[j][i];
        }
    }
}

int findInverseMatrix(int key[SIZE][SIZE], int inverse[SIZE][SIZE]) {
    int det = findDeterminant(key);
    int detInv = modInverse(det, 26);
    if (detInv == -1) {
        return 0;
    }

    int cofactor[SIZE][SIZE];
    findCofactorMatrix(key, cofactor);

    int adjugate[SIZE][SIZE];
    transposeMatrix(cofactor, adjugate);

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            inverse[i][j] = mod26(adjugate[i][j] * detInv);
        }
    }

    return 1;
}

void Decrypt(char ciphertext[], int inverseKey[SIZE][SIZE], char decryptedText[]) {
    Encrypt(ciphertext, inverseKey, decryptedText);  
}

int main() {
    char keyString[10];
    char text[SIZE + 1];
    int choice;         
    char result[SIZE + 1];   
    int key[SIZE][SIZE];

    while (1) {
        // Display menu options
        printf("\nMenu:\n");
        printf("1. Encrypt Text (3 characters)\n");
        printf("2. Decrypt Text (3 characters)\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:  // Encryption
                printf("Enter a 9-character key string: ");
                scanf("%9s", keyString);
                stringToKeyMatrix(keyString, key);
                do {
                    printf("Enter 3-character plaintext: ");
                    scanf("%s", text);
                    if (strlen(text) != SIZE) {
                        printf("Error: Please enter exactly 3 characters.\n");
                    }
                } while (strlen(text) != SIZE);  // Keep asking until the input is exactly 3 characters

                Encrypt(text, key, result);
                printf("Encrypted text: %s\n", result);
                break;

            case 2:  // Decryption
                printf("Enter a 9-character key string: ");
                scanf("%9s", keyString);
                stringToKeyMatrix(keyString, key);
                do {
                    printf("Enter 3-character ciphertext: ");
                    scanf("%s", text);
                    if (strlen(text) != SIZE) {
                        printf("Error: Please enter exactly 3 characters.\n");
                    }
                } while (strlen(text) != SIZE);  // Keep asking until the input is exactly 3 characters

                // Find the inverse key matrix
                int inverseKey[SIZE][SIZE];
                if (!findInverseMatrix(key, inverseKey)) {
                    printf("Inverse of the key matrix does not exist!\n");
                    break;
                }

                Decrypt(text, inverseKey, result);
                printf("Decrypted text: %s\n", result);
                break;

            case 3:  // Exit
                printf("Exiting...\n");
                return 0;

            default:
                printf("Invalid choice, please try again!\n");
                break;
        }
    }

    return 0;
}
