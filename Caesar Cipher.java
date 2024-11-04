import java.util.Scanner;

public class CaesarCipher {

    // Method to encrypt the plaintext
    public static String encrypt(String plaintext, int shift) {
        StringBuilder ciphertext = new StringBuilder();

        for (int i = 0; i < plaintext.length(); i++) {
            char ch = plaintext.charAt(i);

            if (Character.isLetter(ch)) {
                char base = Character.isLowerCase(ch) ? 'a' : 'A';
                ch = (char) ((ch - base + shift) % 26 + base);
            }

            ciphertext.append(ch);
        }

        return ciphertext.toString();
    }

    // Method to decrypt the ciphertext
    public static String decrypt(String ciphertext, int shift) {
        return encrypt(ciphertext, 26 - shift);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int choice = 0;
        while (choice != 3) {
            System.out.println("Choose an option:");
            System.out.println("1. Encrypt");
            System.out.println("2. Decrypt");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            scanner.nextLine(); // Consume the newline

            switch (choice) {
                case 1:
                    System.out.print("Enter the plaintext: ");
                    String plaintext = scanner.nextLine();
                    System.out.print("Enter the shift value: ");
                    int encryptShift = scanner.nextInt();
                    scanner.nextLine(); // Consume the newline

                    String encryptedText = encrypt(plaintext, encryptShift);
                    System.out.println("Encrypted Text: " + encryptedText);
                    break;

                case 2:
                    System.out.print("Enter the ciphertext: ");
                    String ciphertext = scanner.nextLine();
                    System.out.print("Enter the shift value: ");
                    int decryptShift = scanner.nextInt();
                    scanner.nextLine(); // Consume the newline

                    String decryptedText = decrypt(ciphertext, decryptShift);
                    System.out.println("Decrypted Text: " + decryptedText);
                    break;

                case 3:
                    //System.out.println("Exiting the program.");
                    break;

                default:
                    System.out.println("Invalid choice! Please enter 1, 2, or 3.");
                    break;
            }
        }

        scanner.close();
    }
}