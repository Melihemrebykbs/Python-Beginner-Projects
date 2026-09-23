import random
import string

def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_characters = letters + digits + symbols
    
    # Ensure at least one character from each set
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += [random.choice(all_characters) for _ in range(length - 4)]
    random.shuffle(password)
    
    return "".join(password)

if __name__ == "__main__":
    print("=== Password Generator ===")
    try:
        pass_length = int(input("Enter password length (minimum 6): "))
        if pass_length < 6:
            print("For security, length set to minimum of 6.")
            pass_length = 6
    except ValueError:
        pass_length = 12

    generated_pass = generate_password(pass_length)
    print(f"\nGenerated Password: {generated_pass}")
