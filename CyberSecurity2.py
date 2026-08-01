def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
    if decrypt:
        shift = -shift

    result = []
    for char in text:
        if char.isalpha():
            # Determine ASCII offset ('A' for uppercase, 'a' for lowercase)
            start = ord('A') if char.isupper() else ord('a')
            # Shift within 0-25 alphabet range using modulo 26
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(shifted_char)
        else:
            # Leave non-alphabet characters (spaces, numbers, symbols) unchanged
            result.append(char)

    return "".join(result)


def main():
    text = input("Enter text: ")
    shift = 3

    # Encrypt
    encrypted = caesar_cipher(text, shift)
    print("Encrypted:", encrypted)

    # Decrypt
    decrypted = caesar_cipher(encrypted, shift, decrypt=True)
    print("Decrypted:", decrypted)


if __name__ == "__main__":
    main()