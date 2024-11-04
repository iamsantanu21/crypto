#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>

int main() {
    int i, j, numstr[100], numkey[100], numcipher[100];
    char str[100], key[100];

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);  // Use fgets instead of gets
    str[strcspn(str, "\n")] = '\0';  // Remove the newline character

    // Converting entered string to uppercase
    for (i = 0, j = 0; i < strlen(str); i++) {
        if (str[i] != ' ') {
            str[j] = toupper(str[i]);
            j++;
        }
    }
    str[j] = '\0';
    printf("Entered string is: %s \n", str);

    // Storing string in terms of ASCII
    for (i = 0; i < strlen(str); i++) {
        numstr[i] = str[i] - 'A';
    }

    printf("Enter a key: ");
    fgets(key, sizeof(key), stdin);  // Use fgets instead of gets
    key[strcspn(key, "\n")] = '\0';  // Remove the newline character

    // Converting entered key to uppercase
    for (i = 0, j = 0; i < strlen(key); i++) {
        if (key[i] != ' ') {
            key[j] = toupper(key[i]);
            j++;
        }
    }
    key[j] = '\0';

    // Assigning key to the string
    for (i = 0; i < strlen(str); ) {
        for (j = 0; (j < strlen(key)) && (i < strlen(str)); j++) {
            numkey[i] = key[j] - 'A';
            i++;
        }
    }

    // Vigenère encryption
    for (i = 0; i < strlen(str); i++) {
        numcipher[i] = numstr[i] + numkey[i];
    }

    // Handle wrapping around alphabet
    for (i = 0; i < strlen(str); i++) {
        if (numcipher[i] > 25) {
            numcipher[i] = numcipher[i] - 26;
        }
    }

    printf("Vigenere Cipher text is: ");
    for (i = 0; i < strlen(str); i++) {
        printf("%c", (numcipher[i] + 'A'));
    }
    printf("\n");

    // Decryption process (Reverse of encryption)
    int numdecrypted[100];
    for (i = 0; i < strlen(str); i++) {
        numdecrypted[i] = numcipher[i] - numkey[i];
    }

    // Handle wrapping around alphabet for decryption
    for (i = 0; i < strlen(str); i++) {
        if (numdecrypted[i] < 0) {
            numdecrypted[i] = numdecrypted[i] + 26;
        }
    }

    printf("Decrypted text is: ");
    for (i = 0; i < strlen(str); i++) {
        printf("%c", (numdecrypted[i] + 'A'));
    }
    printf("\n");

    return 0;  // Explicit return from main
}