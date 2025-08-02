import random
import string

def generate_password():
    print("=== Password Generator ===")
    
    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print("Password should be at least 4 characters long.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    include_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
    include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include special characters? (e.g. @#$)? (y/n): ").lower() == 'y'

    character_pool = ''
    if include_upper:
        character_pool += string.ascii_uppercase
    if include_lower:
        character_pool += string.ascii_lowercase
    if include_digits:
        character_pool += string.digits
    if include_symbols:
        character_pool += string.punctuation

    if not character_pool:
        print("You must select at least one character type!")
        return

    password = ''.join(random.choice(character_pool) for _ in range(length))
    print(f"\nGenerated Password: {password}")

generate_password()