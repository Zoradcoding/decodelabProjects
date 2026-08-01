def encrypt(text: str, shift: int) -> str:
    """Encrypts text using a Caesar Cipher with the given shift value."""
    result = []
    # Normalize shift to stay within 0-25
    shift = shift % 26

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # Calculate shifted character
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(shifted_char)
        else:
            # Leave non-alphabet characters unchanged
            result.append(char)

    return "".join(result)


def decrypt(text: str, shift: int) -> str:
    """Decrypts text encoded with a Caesar Cipher."""
    return encrypt(text, -shift)


def main():
    message = input("Enter the message: ")

    # Safe shift input handling
    while True:
        try:
            shift = int(input("Enter the shift key (integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the shift key.")

    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    print("\nResults")
    print("-------------------")
    print("Encrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)


if __name__ == "__main__":
    main()
    