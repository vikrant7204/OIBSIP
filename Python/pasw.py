import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character set should be selected.")
        return None

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password

def get_user_input():
    num_passwords = int(input("Enter the number of passwords to generate: "))
    length = int(input("Enter password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    return num_passwords, length, use_letters, use_numbers, use_symbols

def main():
    print("Welcome to the Password Generator!")

    num_passwords, length, use_letters, use_numbers, use_symbols = get_user_input()

    for _ in range(num_passwords):
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        if password:
            print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
