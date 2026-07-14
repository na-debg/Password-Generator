import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase

    if use_lower:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: Select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print("=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)

try:
    length = int(input("Enter password length: "))

    upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    digits = input("Include numbers? (y/n): ").lower() == 'y'
    symbols = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, upper, lower, digits, symbols)

    print("\nGenerated Password:")
    print(password)

except ValueError:
    print("Please enter a valid number.")
