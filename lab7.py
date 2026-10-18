def vigenere_sq():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    square = []
    for row in range(26):
        row_letters = []
        for column in range(26):
            index = (row + column) % 26
            row_letters.append(alphabet[index])
        square.append(row_letters)
    print(" |", end="")
    for letter in alphabet:
        print(f"{letter} |", end="")
    print()
    print("| ---" * 27 + "|")

    for row in range(26):
        print(alphabet[row], end=" |")

        for letter in square[row]:
            print(letter, end=" |")

        print()

def letter_to_index(letter, alphabet):
    return alphabet.index(letter)


#Part 2 encrytion
def index_to_letter(index, alphabet):
    return alphabet[index]

def vigenere_index(key_letter, plain_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plain_index = letter_to_index(plain_letter, alphabet)
    cipher_text = (key_index + plain_index) % 26
    return index_to_letter(cipher_text, alphabet)






vigenere_sq()
def encrypt_vigenere(key, plaintext, alphabet):
    ciphertext = []
    for i in range(len(plaintext)):
        plain_letter = plaintext[i]
        if plain_letter == " ":
            ciphertext.append(" ")
            continue

        key_letter = key[i % len(key)]
        encrypted_letter = vigenere_index(key_letter, plain_letter, alphabet)
        ciphertext.append(encrypted_letter)
    return "".join(ciphertext)

def decrypt_vigenere(key, ciphertext, alphabet):
        plaintext = []
        for i in range(len(ciphertext)):
            cipher_letter = ciphertext[i]
            if cipher_letter == " ":
                plaintext.append( " ")
                continue
            key_letter = key[i % len(key)]
            cipher_index = letter_to_index(cipher_letter, alphabet)
            key_index = letter_to_index(key_letter, alphabet)
            plain_index = (cipher_index - key_index) % 26
            plain_letter = index_to_letter(plain_index, alphabet)
            plaintext.append(plain_letter)
        return"".join(plaintext)
encrypted_messages = []
def cypher_menu():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    menu = [
        "1. Encrypt a message",
        "2. Decrypt a message",
        "3. Dump Encrypted Text",
        "4. Quit"
    ]

    while True:
        print("Vigenere cipher menu")
        for item in menu:
            print(item)

        choice = input("Enter your choice: ")
        if choice == "1":
            plaintext = input("Enter a message to encrypt: ").upper()
            key = input("Enter your secret key: ").upper()
            ciphertext = encrypt_vigenere(key, plaintext, alphabet)
            print(ciphertext)
            encrypted_messages.append((key, ciphertext))
        elif choice == "2":
            for key, ciphertext in encrypted_messages:
                plaintext = decrypt_vigenere(key, ciphertext, alphabet)
                print(plaintext)
        elif choice == "3":
            print(encrypted_messages)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

print(letter_to_index("C", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print(index_to_letter(3, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print(vigenere_index("D", "C", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print(decrypt_vigenere("DOG", "FOZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
cypher_menu()




