import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special):
    # Character pools
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special_characters = string.punctuation if use_special else ''
    
    # Combine character pools
    all_characters = lowercase_letters + uppercase_letters + numbers + special_characters
    
    if not all_characters:
        return "Error: No character types selected! Please select at least one character type."
    
    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def password_generator():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length (minimum 6): "))
        if length < 6:
            print("Password length must be at least 6. Try again.")
            return
        
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() in ['yes', 'y']
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() in ['yes', 'y']
        use_special = input("Include special characters? (yes/no): ").strip().lower() in ['yes', 'y']
        
        # Generate and display the password
        password = generate_password(length, use_uppercase, use_numbers, use_special)
        print(f"\nYour generated password is: {password}")
        
    except ValueError:
        print("Invalid input! Please enter a valid number for the length.")
    
# Start the password generator
password_generator()
