import string
def check_password_strength(password: str) -> dict:
    length = len(password)

    # Boolean criteria checks
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    # Base score calculated from criteria met
    score = sum([has_upper, has_lower, has_digit, has_symbol])

    # Add extra score for good length
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1

    # Determine overall strength based on total score and minimum length rule
    if length < 8 or score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "strength": strength
    }


def main():
    password = input("Enter your password: ")
    analysis = check_password_strength(password)

    print("\nPassword Analysis")
    print("-----------------")
    print(f"Length: {analysis['length']}")
    print(f"Uppercase: {'Yes' if analysis['has_upper'] else 'No'}")
    print(f"Lowercase: {'Yes' if analysis['has_lower'] else 'No'}")
    print(f"Numbers: {'Yes' if analysis['has_digit'] else 'No'}")
    print(f"Symbols: {'Yes' if analysis['has_symbol'] else 'No'}")
    print(f"\nPassword Strength: {analysis['strength']}")


if __name__ == "__main__":
    main()